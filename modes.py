__author__ = 'Kenny'
import datetime
import threading



#Modes
def statistics(thermometers, time):
    def LogTemperatures(thermometers):
        with open('output.txt', 'a+') as f:
            f.write("#####\n"+str(datetime.datetime.now())+"\n")
            for x in thermometers:
                f.write("{0}({1}):{2}".format(x.description, str(x.file_id), str(x.GetTemp())))
        threading.Timer(time, LogTemperatures, [thermometers]).start()


    threading.Timer(time, LogTemperatures, [thermometers]).start()
    print("Start measurement")


