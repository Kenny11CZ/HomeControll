import os
import glob
import time
import json
import mysql.connector
 
dictionary_file = "doc/dictionary.json"
base_dir = '/sys/bus/w1/devices/'

# create_dictionary()

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
	f = open(dictionary_file, 'w')
	f.write(json.dumps(d))
	f.close()

def init():
	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

def get_dictionary():
	f = open(dictionary_file, 'r')
	return json.load(f)

init()

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='monitoring')

dictionary = get_dictionary()

def read_data():
	res = {"time": (int)(time.time()), "data": []}
	for t in dictionary["thermometers"]:
		d = {}
		try:
			filename = base_dir + "/" + t["device_id"] + "/w1_slave"
			f = open(filename, "r")
			d = f.read()
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
			data_temp = (data["time"], key, t[key])
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