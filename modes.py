__author__ = 'Kenny'
import datetime
import threading
import os
import json

#Modes
def statistics(thermometers, time):
    iteration = [None]
    iteration[0] = 0
    def LogTemperatures(thermometers):
        with open('output.txt', 'r+') as f:
            try:
                data = json.load(f)
            except:
                data = list()
        temp = [None]
        temp[0] = {"time":str(datetime.datetime.now())}
        therms = list()
        for i, t in enumerate(thermometers):
            therms.append({"id": t.file_id, "name": t.description, "temp": t.GetTemp()})
        temp[0]["thermometers"] = therms
        data.append(temp)
        with open('output.txt', 'w+') as f:
            f.write(json.dumps(data))
        os.system('cp output.txt server/temperatures.txt')
        threading.Timer(time, LogTemperatures, [thermometers]).start()
        iteration[0] = iteration[0] + 1
        print("{0} iteration".format(iteration[0],))
    print("Start measurement")
    if not os.path.isfile("output.txt"):
        os.system("touch output.txt")
    threading.Timer(time, LogTemperatures, [thermometers]).start()

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






