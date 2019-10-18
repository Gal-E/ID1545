#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
from threading import Thread
from dotenv import load_dotenv  # To load the environment variables from the .env file
from time import sleep

from flask import Flask, request, render_template, render_template, request
from flask_socketio import SocketIO, emit, send


# DCD Hub
#from dcd.entities.thing import Thing
#from dcd.entities.property import PropertyType

# The thing ID and access token
load_dotenv()
#THING_ID = os.environ['THING_ID']
#THING_TOKEN = os.environ['THING_TOKEN']
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

measuredAngle = 0
initialAngle = 20
absoluteAngle = 0
circleCounter = 0

activator = True
activator2 = True

old_val = 0

avgList = []
avgListLength = 10
avgListCounter = 0

checkpoint = 0
checkpointCheck = True

rotationDirection = "right"

def reset():
    initialAngle = cur_val
    old_val = cur_val
    measuredAngle = 0
    initialAngle = 30
    absoluteAngle = 0
    circleCounter = 0
    checkpoint = 0

def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)


def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    values = [float(x) for x in value_bytes.decode('utf-8').split(",")]

    myCmd = 'clear'
    os.system(myCmd)
    #print(F"BNOvalues {values}")
    #find_or_create("Left Wheel Orientation",
    #PropertyType.THREE_DIMENSIONS).update_values(values)

    cur_loc = values
    calCircle(cur_loc[0])
    try:
        socketio.emit('orientation', '{"orientation": "%s"}' % str(abs(round(avgAbsoluteAngle,0))), broadcast=True)
    except:
        print("No socket?")
    return avgAbsoluteAngle


def calCircle(cur_val):
    global measuredAngle
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
    global activator2

    global avgList
    global avgListLength
    global avgListCounter
    global avgAbsoluteAngle

    '''
    print(str(activator))

    print("absoluteAngle " + str(absoluteAngle))
    print("circleCounter " + str(circleCounter))
    print("measuredAngle " + str(measuredAngle))
    print("initialAngle " + str(initialAngle))
    print("old_val " + str(old_val))
    print("cur_val " + str(cur_val))
    '''

    if activator2:
        initialAngle = cur_val
        old_val = cur_val
        activator2 = False
        for i in range(avgListLength):
            avgList.append(initialAngle)


    if old_val < increment2 and cur_val > (360-increment2):
        #circleCounter+=1
        circleCounter = circleCounter+1
        activator=False

    if old_val > (360-increment2) and cur_val < increment2:
        #circleCounter-=1
        circleCounter = circleCounter-1
        activator=False

    if old_val-cur_val>increment:
        old_val = cur_val
        measuredAngle = old_val
        absoluteAngle = measuredAngle-initialAngle-(circleCounter*360)
        #print(str(measuredAngle)+" "+str(round(absoluteAngle)*10/10.0))
        activator = True

    elif old_val-cur_val < (-1)*increment :
        old_val = cur_val
        measuredAngle=old_val
        absoluteAngle=measuredAngle-initialAngle-(circleCounter*360)
        #print(str(measuredAngle)+" "+str(round(absoluteAngle)*10/10.0))
        activator = True

    if absoluteAngle < 0:
        if round(absoluteAngle/10.0)%36 == 0 and round(absoluteAngle/10.0) != 0 :
            print("circle to the left complete!!")
            sleep(3)
            reset()
    elif absoluteAngle>0:
        if round(absoluteAngle/10.0)%36 == 0 and round(absoluteAngle/10.0) != 0 :
            print("circle to the right complete!!")
            sleep(3)
            reset()


    if avgListCounter < avgListLength - 1:
        avgListCounter = avgListCounter + 1
    else:
        avgListCounter = 0

    avgList[avgListCounter] = absoluteAngle
    avgAbsoluteAngle = 100*(sum(avgList)/avgListLength)/360



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

# ===================== this is where we copied in the code from that other group: ===============

'''
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/distance')
def distance():
    distBar = distVal
    return render_template('distanceVis.html', distBar=distBar)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    emit('json', json, broadcast=True)

@socketio.on('distance')
def handle_distance(json):
    print( float(json['distance']))
'''

#============= so down here i'm adding our own server.py code to see whether I can make some frankenstein combination that implements our angular data.




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gauge')
def gauge():
    return render_template('gauge.html')

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
  print('received json: ' + str(json))
  emit('json', json, broadcast=True)

@socketio.on('orientation')
def handle_orientation(json):
  print(float(json['orientation']))



# Instantiate a thing with its credential, then read its properties from the DCD Hub
#my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
#my_thing.read()


def connect_bluetooth():
    print("Starting Bluetooth...")
    # Start a BLE adapter
    bleAdapter = pygatt.GATTToolBackend()
    bleAdapter.start()

    print("connecting to Bluetooth device...")
    # Use the BLE adapter to connect to our device
    wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)

    # Subscribe to the GATT service
    wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
            callback=handle_orientation_data)

# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

#connect_bluetooth()

if __name__ == '__main__':
    thread = Thread(target=connect_bluetooth)
    thread.start()
    socketio.run(app, host = '0.0.0.0')

app.use("/scripts", express.scripts('./scripts/'));

#let's hope this works...

#while True :
#    sleep(5)