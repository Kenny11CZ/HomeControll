import sys
import glob
sys.path.insert(0, 'Objects')
from thermometer import Thermometer
from db import DB


def FirstRun():
    device_folders = glob.glob("/sys/bus/w1/devices/" + "28*")
    for folder in device_folders:
        id = folder.split('/')[-1]
        description = raw_input("ID: " + id + " | Description: ")
        t = Thermometer(id, description)
        thermometers.append(t)


database = DB
thermometers = []
thermometers = list(thermometers)


FirstRun()

for x in thermometers:
    print(x.GetTemp())

