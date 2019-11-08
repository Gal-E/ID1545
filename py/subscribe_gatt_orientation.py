#!/usr/bin/env python3

# Import required libraries
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
from threading import Thread
from dotenv import load_dotenv  # To load the environment variables from the .env file
from time import sleep

from flask import Flask, request, render_template, render_template, request
from flask_socketio import SocketIO, emit, send

from pydub import AudioSegment
from pydub.playback import play

# DCD Hub
from dcd.entities.thing import Thing
from dcd.entities.property import PropertyType

# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']

# Instantiate a thing with its credential that are stored in the .env file
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
my_thing.read()
my_property = my_thing.find_or_create_property("angle_data",PropertyType.ONE_DIMENSION)

# Create thet audiosegment that will be played once assignment has been completed
complete = AudioSegment.from_wav("complete.wav")

# Import Bluetooth UUID to access Adafruit Feather from .env file
BLUETOOTH_DEVICE_MAC = os.environ['BLUETOOTH_DEVICE_IMU']

# UUID of the GATT characteristic to subscribe
#GATT_CHARACTERISTIC_ORIENTATION = "MY_GATT_ORIENTATION_SERVICE_UUID"
GATT_CHARACTERISTIC_ORIENTATION = "02118833-4455-6677-8899-aabbccddeeff"

# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

# ==== ==== ===== == =====  Web server

app = Flask(__name__)
sensors = ['sensor1', 'sensor2', 'sensor3']

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# ==== ==== ===== == =====  Initializing Values

cur_loc = (-666, -666, -666)
degreesRotated = 0
increment = 10
increment2 = increment + 5

initialAngle = 20
absoluteAngle = 0
circleCounter = 0

activator = True

old_val = 0
cur_val = 0

avgList = []
avgListLength = 10
avgListCounter = 0

checkpoint = 0

completionDetectionLeft = False
completionDetectionRight = False

playedOnce = True

rotationDirection = "right"

# Attempt at creating a reset function that would be triggered once the assignment had been completed.
# Didn't get this to work.

'''

def reset():
    initialAngle = cur_val
    old_val = cur_val
    initialAngle = 30
    absoluteAngle = 0
    avgAbsoluteAngle = 0
    circleCounter = 0
    checkpoint = 0
    activator = True
    playedOnce = True
    completionDetectionLeft = False
    completionDetectionRight = False

'''

# Function that initiates my_thing on the DCD Hub.
# If the Thing with this property isn't found on the server, this piece of code will create a new Thing.

def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)

# Handler that get's triggered everytime new data is received from the Adafruit over Bluetooth

def handle_orientation_data(handle, value_bytes):

    global my_property

    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    values = [float(x) for x in value_bytes.decode('utf-8').split(",")]

    # This makes sure that the Terminal gets wiped everytime, to only show most up to date data.
    myCmd = 'clear'
    os.system(myCmd)

    # Here, the edge computing on the received data is done in the calCircle functiono and
    # subsequently pushed to the DCD Hub.
    values[0] = calCircle(values[0])
    my_property.update_values((values[0],))

# CalCircle makes sure the right angular data is being forwarded to the web-interface.
# I will now explain how it does that.

def calCircle(new_val):

    # ==== ==== ===== == =====  Initializing Values

    global initialAngle
    global absoluteAngle
    global circleCounter

    global old_val

    global degreesRotated
    global rotationDirection
    global checkpoint
    global increment
    global increment2
    global activator

    global avgList
    global avgListLength
    global avgListCounter
    global avgAbsoluteAngle

    global completionDetectionRight
    global completionDetectionLeft

    global complete

    global playedOnce

    # ==== ==== ===== == ===== The Calculations

    '''
    The boolean activator makes sure that the first angle received from
    the Adafruit is stored as the initial orientation of the system. The
    initialAngle is then used as a reference to measure by how many degrees
    the wheelchair has rotated since the code has started running.

    Since the code uses a moving average to smoothen the jumpiness of the
    IMU data, the list that is used to calculate this moving average is
    also being filled up with this initial orientation data.

    activator then gets switched to False and isn't switched to True
    anywhere in the code, hence this initialising code is run only once.
    '''

    if activator:
        initialAngle = new_val
        old_val = new_val
        for i in range(avgListLength):
            avgList.append(initialAngle)

        activator = False

    '''
    One of the main challenges in calculating the amount of degrees the
    wheelchair had rotated was that the IMU only sends an angle somewhere
    between 0 and 360 degrees. As a work-around, we had to come up with a
    system that would somehow know that once the system went below 0 degrees
    or beyond 360 degrees, it would note that one circle in a certain
    direction had been completed.

    We managed to do that by constantly measuring a value 'new_val' and then
    comparing this against the value that was measured before, 'old_val'. If
    the measured difference exceeds a threshhold, called an 'increment' of a
    few degrees, we would consider that a significant change and register it
    as actual movement. We do that the same way in both directions.
    '''

    if old_val-new_val>increment:
        old_val = new_val
        absoluteAngle = old_val-initialAngle

    elif old_val-new_val < (-1)*increment :
        old_val = new_val
        absoluteAngle=old_val-initialAngle

    '''
    If old_val is close to 0 and the new_val is already measured to be close
    to 360, we can assume that the system is about to transition this
    threshhold and subtract 1 of the circleCounter. This means a transition
    has been made to the left.

    If old_val is instead close to 360 and new_val is measured to be close
    to 0, we can assume that the system is about to transition the threshhold
    the other way round, and we add 1 to the circleCounter. This means a
    transition has been made to the right.
    '''

    if old_val < increment2 and new_val > (360-increment2):
        circleCounter = circleCounter-1

    if old_val > (360-increment2) and new_val < increment2:
        circleCounter = circleCounter+1

    '''
    By then combining the 'circleCounter', multiplying it by 360 and adding this
    measured value to the absoluteAngle calculated in the previous step, we can
    prevent that the absoluteAngle, which is the progress made compared to
    the initialAngle measured at the start of the code, jumps to a value
    outside the 0 to 360 range.
    '''

    absoluteAngle = absoluteAngle+(circleCounter*360)

    '''
    We then store this most recent 'absoluteAngle' in a list of averages, called
    'avgList', which we can then use to calculate a moving average called
    'avgAbsoluteAngle'
    '''

    if avgListCounter < avgListLength - 1:
        avgListCounter = avgListCounter + 1
    else:
        avgListCounter = 0

    avgList[avgListCounter] = absoluteAngle
    avgAbsoluteAngle = 100*(sum(avgList)/avgListLength)/360

    '''
    This last value can then finally be used to keep track of the progress
    made in rotating a full circle. If it is completed, we trigger the final
    action this prototype is supposed to make as soon as the circle has been
    completed, by setting 'completionDetectionLeft' or
    'completionDetectionRight' to True.
    '''

    if avgAbsoluteAngle < 0:
        if round(avgAbsoluteAngle/5.0)%20 == 0 and round(avgAbsoluteAngle/5.0) != 0 :
            print("circle to the left complete!!")
            completionDetectionLeft = True
    elif absoluteAngle>0:
        if round(avgAbsoluteAngle/5.0)%20 == 0 and round(avgAbsoluteAngle/5.0) != 0 :
            print("circle to the right complete!!")
            completionDetectionRight = True

    '''
    This in turn will freeze the avgAbsoluteAngle to be set fixed at '100',
    which then gets pushed directly to the HTTP server using socketio.emit,
    which was a requirement for preventing the web-interface from updating
    once a circle has been completed.

    Subsequently, the music file that was initialized at the beginning is
    played, and the boolean 'playedOnce' is deactivated, to prevent the
    sound from being played over and over again.
    '''

    if completionDetectionRight and playedOnce:
        avgAbsoluteAngle = 100
        try:
            socketio.emit('angle', '{"angle": "%s"}' % str(round(avgAbsoluteAngle)), broadcast=True)
        except:
            print("No socket?")
        play(complete)
        playedOnce = False
    elif completionDetectionLeft and playedOnce:
        avgAbsoluteAngle = -100
        try:
            socketio.emit('angle', '{"angle": "%s"}' % str(round(avgAbsoluteAngle)), broadcast=True)
        except:
            print("No socket?")
        play(complete)
        playedOnce = False
    elif playedOnce:
        try:
            socketio.emit('angle', '{"angle": "%s"}' % str(round(avgAbsoluteAngle)), broadcast=True)
        except:
            print("No socket?")

    '''
    Once playedOnce has been activated, the code then knows that everything
    it had to do has been done, the program is put to rest for 5 seconds
    and the reset-function was intended to trigger. This, we however couldn't
    get to work.
    '''

    if playedOnce == False:
        sleep(5)
        #reset()

    '''
    Lastly, 'avgAbsoluteAngle' is returned to then be posted to the DCD hub.
    '''

    return avgAbsoluteAngle


# Checks whether bluetooth connection is live.

def discover_characteristic(device):
    """List characteristics of a device"""

    for uuid in device.discover_characteristics().keys():
        try:
            print("Read UUID" + str(uuid) + "   " + str(device.char_read(uuid)))
        except:
            print("Something wrong with " + str(uuid))

def read_characteristic(device, characteristic_id):
    """Read a characteristic"""
    return device.char_read(characteristic_id)


def keyboard_interrupt_handler(signal_num, frame):
    """Make sure we close our program properly"""
    print("Exiting...".format(signal_num))
    wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)


#============= HTTP server set-up

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gauge')
def gauge():
    return render_template('gauge.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/donut')
def donut():
    return render_template('donut.html')

@app.route('/api/sensors', methods = ['GET'])
def list():
    return str(sensors)

@app.route('/api/sensors/<path:sensor_id>', methods = ['GET'])
def read(sensor_id):
    global sensors
    return sensors[sensor_id]

@app.route('/api/sensors', methods = ['POST'])
def create():
    sensors.append(request.json["sensorName"])
    return 'Added sensor!'

@socketio.on('json')
def handle_json(json):
  #print('received json: ' + str(json))
  emit('json', json, broadcast=True)

@socketio.on('angle')
def handle_orientation(json):
  print("I'm sending data")

# Instantiate a thing with its credential, then read its properties from the DCD Hub
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
my_thing.read()


def connect_bluetooth():
    print("Starting Bluetooth...")
    # Start a BLE adapter
    bleAdapter = pygatt.GATTToolBackend()

    print("connecting to Bluetooth device...")
    # Use the BLE adapter to connect to our device

    try:
        bleAdapter.start()
        wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)

        wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                callback=handle_orientation_data)
    except:
        connect_bluetooth()

# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

#connect_bluetooth()

if __name__ == '__main__':
    thread = Thread(target=connect_bluetooth)
    thread.start()

    socketio.run(app, host = '0.0.0.0')
