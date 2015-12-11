import os
import sys
import glob
import argparse
sys.path.insert(0, 'Objects')
from thermometer import Thermometer
from db import DB


database = DB
thermometers = []


def FirstRun():
    device_folders = glob.glob("/sys/bus/w1/devices/" + "28*")
    for folder in device_folders:
        id = folder.split('/')[-1]
        description = raw_input("ID: " + id + " | Description: ")
        t = Thermometer(id, description)
        thermometers.append(t)
def Initialize():
    thermometers = Thermometer.LoadThermometers()

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)

if not os.path.isfile("HomeControll.db"):
    FirstRun()
else:
    Initialize()



for x in thermometers:
    print(x.description + x.GetTemp())

