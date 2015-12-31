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
        filename = datetime.datetime.now().strftime("%Y-%m-%d")
        def WriteDaily(thermometers, text):
            try:
                if not os.path.isfile(filename+".csv"):
                    if not os.path.isdir("server/public/daily"):
                        os.system("mkdir server/public/daily")
                    os.system("touch server/public/daily/"+filename+".csv")
                    firstline = "Time"
                    for t in thermometers:
                        firstline += "," + t.description
                    firstline += ";\n"
                    with open('server/public/daily/'+filename+'.csv', 'w+') as f:
                        f.write(firstline)
            except:
                print "error while initialising daily log file: " + sys.exc_info()[0]
            try:
                with open('output.csv', 'a+') as f:
                    f.write(text)
            except:
                print "error while writing into daily log file: " + sys.exc_info()[0]


        now = datetime.datetime.now()
        try:
            if now.strftime("%Y-%m-%d") != filename:
                filename = now.strftime("%Y-%m-%d")
        except:
            print "error with daily logs: " + sys.exc_info()[0]
        with open('output.txt', 'r+') as f:
            try:
                data = json.load(f)
            except:
                data = list()
        temp = [None]
        temp[0] = {"time":str(now)}
        therms = list()
        for i, t in enumerate(thermometers):
            therms.append({"id": t.file_id, "name": t.description, "temp": t.GetTemp()})
        temp[0]["thermometers"] = therms
        data.append(temp)
        with open('output.txt', 'w+') as f:
            f.write(json.dumps(data))
        result = str(datetime.datetime.now())
        for t in thermometers:
            result += "," + str(t.GetTemp())
        result += ";\n"
        with open('output.csv', 'a+') as f:
            f.write(result)

        WriteDaily(thermometers, result)
        os.system('cp output.txt server/public/temperatures.txt')
        os.system('cp output.csv server/public/temperatures.csv')
        threading.Timer(time, LogTemperatures, [thermometers]).start()
        iteration[0] = iteration[0] + 1
        print("{0} iteration".format(iteration[0],))


    print("Start measurement")
    #Inicializace soubooru
    if not os.path.isfile("output.txt"):
        os.system("touch output.txt")
    if not os.path.isfile("output.csv"):
        os.system("touch output.csv")
        firstline = "Time"
        for t in thermometers:
            firstline += "," + t.description
        firstline += ";\n"
        with open('output.csv', 'w+') as f:
            f.write(firstline)


    LogTemperatures(thermometers)

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






