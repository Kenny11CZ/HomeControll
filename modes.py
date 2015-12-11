import time
import threading
__author__ = 'Kenny'

#Modes
def statistics(time):
    threading.Timer(time, LogTemperatures()).start()
    print("Start measurement")
    def LogTemperatures():
        with open('output.txt', 'w+') as f:
            f.write("#####\n"+time.strftime("%d %m %Y %H:%M:%S")+"\n")
            for x in thermometers:
                print(x.description + "(" + x.file_id + "):" + x.GetTemp())

