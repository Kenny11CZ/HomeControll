__author__ = 'Kenny'
import datetime
import threading


#Modes
def statistics(thermometers, time):
    def LogTemperatures():
        with open('output.txt', 'w+') as f:
            f.write("#####\n"+str(datetime.datetime.now())+"\n")
            for x in thermometers:
                print(x.description + "(" + x.file_id + "):" + x.GetTemp())


    threading.Timer(time, LogTemperatures).start()
    print("Start measurement")


