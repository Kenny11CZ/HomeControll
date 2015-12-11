__author__ = 'Kenny'
import datetime
import threading

#Modes
def statistics(thermometers, time):
    i = [None]
    i[0] = 1
    def LogTemperatures(thermometers):
        with open('output.txt', 'a+') as f:
            f.write("#####\n"+str(datetime.datetime.now())+"\n")
            for x in thermometers:
                f.write("{0}({1}):{2}\n".format(x.description, str(x.file_id), str(x.GetTemp())))
        threading.Timer(time, LogTemperatures, [thermometers]).start()
        i[0] = i[0] + 1
        printf("{0} iteration".format(i[0],))
    print("Start measurement")
    threading.Timer(time, LogTemperatures, [thermometers]).start()



