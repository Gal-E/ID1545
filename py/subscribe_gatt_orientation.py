#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
from dotenv import load_dotenv  # To load the environment variables from the .env file
from time import sleep


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

cur_loc = (-666, -666, -666)
degreesRotated = 0
increment = 5

measuredAngle = 0
initialAngle = 10
absoluteAngle = 0
circleCounter = 0

activator = True
initialAngle = 0

old_val = 0
cur_val = 0

checkpoint = 0
checkpointCheck = True
pause = True

rotationDirection = "right"

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
    print(F"BNOvalues {values}")
    #find_or_create("Left Wheel Orientation",
    #PropertyType.THREE_DIMENSIONS).update_values(values)

    cur_loc = values
    calCircle(cur_loc[0])

def calCircle(new_val):
    global measuredAngle
    global initialAngle
    global absoluteAngle
    global circleCounter

    global old_val
    global cur_val

    global degreesRotated
    global rotationDirection
    global checkpoint
    global increment
    global activator
    global pause

    if old_val-new_val>increment:
        measuredAngle = old_val
        absoluteAngle = measuredAngle-initialAngle+circleCounter*360
        print(measuredAngle=" "+round(absoluteAngle*10)/10.0)
        activator = True

            if old_val>360-increment:
                circleCounter+=1

    elif old_val-new_val<-1*increment:
        measuredAngle=old_val
        absoluteAngle=measuredAngle-initialAngle+circleCounter*360
        print(measuredAngle+" "+round(absoluteAngle*10)/10.0)

    if old_val<increment and new_val>(360-increment) and activator:
        circleCounter+=1
        activator=False
    elif old_val>(360-increment) and new_val<increment and activator:
        circleCounter-=1
        activator=False

    if absoluteAngle < 0:
        if round(absoluteAngle/10.0)%36 == 0 and round(absoluteAngle/10.0) != 0 :
            print("circle to the left complete!!")
            pause = True
    elif absoluteAngle>0:
        if round(absoluteAngle/10.0)%36 == 0 and round(absoluteAngle/10.0) != 0 :
            print("circle to the right complete!!")
            pause = True

    old_val = new_val


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
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)


# Instantiate a thing with its credential, then read its properties from the DCD Hub
#my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
#my_thing.read()

# Start a BLE adapter
bleAdapter = pygatt.GATTToolBackend()
bleAdapter.start()

# Use the BLE adapter to connect to our device
left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)

# Subscribe to the GATT service
left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION, callback=handle_orientation_data)

# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

while True :
    sleep(5)