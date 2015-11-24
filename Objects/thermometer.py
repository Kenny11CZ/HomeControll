import os
import glob
import time
from Objects.db import DB

class Thermometer():
    def __init__(self, file_id, description):
        self.db = DB()
        self.cursor = self.db.cursor
        result = self.db_save(file_id, description)
        self.file_id = result[0]
        self.descripton = result[1]

        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        self.base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(self.base_dir + self.file_id)[0]
        self.device_file = device_folder + '/w1_slave'

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def GetTemp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def db_save(self, file_id, description):
        self.cursor.execute("INSERT INTO thermometers VALUES (?,?)", (file_id, description))
        self.cursor.execute("SELECT * FROM thermometers WHERE file_id = ?", (file_id,))
        self.db.connection.commit()
        return self.cursor.fetchone()
