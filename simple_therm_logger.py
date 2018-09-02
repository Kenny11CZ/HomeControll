import os
import sys
import glob
import time
import datetime
import json
import mysql.connector
 
dictionary_file = "doc/dictionary.json"
base_dir = '/sys/bus/w1/devices/'

# create_dictionary()

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='monitoring')

def create_dictionary():
	d = {"thermometers": [{
			"device_id": "28-0000067d28e2", 
			"name": "komin",
		},{
			"device_id": "28-0000067d2091", 
			"name": "nad krbem u strechy",
		},{
			"device_id": "28-0000067d3bd0", 
			"name": "odtah nad krbem nahore"
		},
	]}
	try:
		cursor = cnx.cursor()
		add_dict = ("INSERT INTO dictionary (device_id, name) VALUES (%s, %s)")
		for t in d["thermometers"]:
			data_dict = (t["device_id"], t["name"])
			cursor.execute(add_dict, data_dict)
		cnx.commit()
		cursor.close()	
	except Exception as e:
		print("cannot save dict to database")
	
	try:
		f = open(dictionary_file, 'w')
		f.write(json.dumps(d))
		f.close()	
	except Exception as e:
		print("cannot save dict to file")
	
def init():
	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

def get_dictionary():
	f = open(sys.argv[0].split("simple_therm_logger.py")[0] + dictionary_file, 'r')
	return json.load(f)

init()

dictionary = get_dictionary()

def read_data():
	res = {"time": (int)(time.time()), "data": []}
	for t in dictionary["thermometers"]:
		d = {}
		try:
			filename = base_dir + "/" + t["device_id"] + "/w1_slave"
			f = open(filename, "r")
			d = {t["device_id"]: (float)(f.read().split("t=")[1])/1000}
		except Exception as e:
			d = {t["device_id"]: "-99"}
		res["data"].append(d)
	return res

def save_data(data):
	try:
		cursor = cnx.cursor()
		add_temp = ("INSERT INTO thermometers (time, device_id, value) VALUES (%s, %s, %s)")
		for t in data["data"]:
			key = list(t.keys())[0]
			time = datetime.datetime.fromtimestamp(data["time"]).strftime('%Y-%m-%d %H:%M:%S')
			data_temp = (time, key, t[key])
			cursor.execute(add_temp, data_temp)
		cnx.commit()
		cursor.close()
		print("saved data")	
	except Exception as e:
		print("error: " + e)
	

def cycle():
	while True:
		d = read_data()
		save_data(d)
		time.sleep(2)

cycle()
# device_file = device_folder + '/w1_slave'