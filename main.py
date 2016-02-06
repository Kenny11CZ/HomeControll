__author__ = 'Kenny'
import os
import sys
import glob
import argparse
import modes
from thermometer import Thermometer
from db import DB

database = DB
thermometers = []
thermometers = list(thermometers)

//def FirstRun():
//    device_folders = glob.glob("/sys/bus/w1/devices/" + "28*")
//    for folder in device_folders:
//        id = folder.split('/')[-1]
//        description = raw_input("ID: " + id + " | Description: ")
//        t = Thermometer(id, description)
//        thermometers.append(t)
def Initialize():
    for t in Thermometer.LoadThermometers():
        thermometers.append(t);

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--mode', help='select mode(statistics, init, send_statistics)', dest='mode', required=True)
parser.add_argument('--time', help='set delay', dest='time', type=int)
results = parser.parse_args()

//if not os.path.isfile("HomeControll.db"):
//    FirstRun()
else:
    Initialize()

active = None

if results.mode == "statistics":
    print("Starting in mode {0} and time {1}".format(results.mode, results.time))
    active = modes.statistics(thermometers, results.time)
elif results.mode == "send_statistics":
    print("Uploading to pastebin.org")
    modes.pastebin()
elif results.mode == "init":
    exit(0)
