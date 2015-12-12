__author__ = 'Kenny'
import datetime
import threading
import os
import json

#Modes
def statistics(thermometers, time):
    iteration = [None]
    iteration[0] = 0
    def LogTemperatures(thermometers, f):
        #with open('output.txt', 'a+') as f:
        #    f.write("#####\n"+str(datetime.datetime.now())+"\n")
        #    for x in thermometers:
        #        f.write("{0}({1}):{2}\n".format(x.description, str(x.file_id), str(x.GetTemp())))


        data = [None]
        data[0] = {"time":str(datetime.datetime.now())}
        therms = [None]
        therms = list(therms)
        for i, t in enumerate(thermometers):
            therms.append({"id": t.file_id, "name": t.description, "temp": t.GetTemp()})
        data[0]["thermometers"] = therms
        print(json.dumps(data))
        threading.Timer(time, LogTemperatures, [thermometers, f]).start()
        iteration[0] = iteration[0] + 1
        print("{0} iteration".format(iteration[0],))
    print("Start measurement")
    with open('output2.txt', 'ra+') as f:
        threading.Timer(time, LogTemperatures, [thermometers, f]).start()

def pastebin():
    import requests, urllib
    with open('output.txt', 'r') as f:
        data = f.read()

        values = { 'api_dev_key' : "1321323",
                    'api_option' : "paste",
                    'paste' : "13213132131" }
        r = requests.post('http://requestb.in/1l28i7t1', params=urllib.urlencode(values), headers={'content-type':'application/x-www-form-urlencoded', 'Content-Length': 80})
        print "Output from pastebin.org: "
        print(r.text)






