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
        print("{0} iteration".format(i[0],))
    print("Start measurement")
    threading.Timer(time, LogTemperatures, [thermometers]).start()

def paastebin():
    import httplib
    with open('output.txt', 'r+') as f:
        httpServ = httplib.HTTPConnection("pastebin.com", 80)
        httpServ.connect()
        httpServ.request('POST', '/api/api_post.php',
                         'api_user_key={1}&api_paste_private={2}&api_paste_name={3}&api_paste_expire_date={4}&api_dev_key={5}&api_paste_code={6}'
                         .format("paste", "", "0", str(datetime.datetime.now()) + " Temps", "10M", "e8ef585291dc675b7bf9e7b66e340326", f.read()))

        response = httpServ.getresponse()
        print(response.status)
        if response.status == httplib.OK:
            print "Output from pastebin.org: "
            print(response.read())

        httpServ.close()





