import sys
sys.path.insert(0, 'Objects')
from Objects.thermometer import Thermometer
from Objects.db import DB

database = DB
thermometers = []
thermometers = list(thermometers)
test = Thermometer("28-0114539cw2ff", "popisek")
thermometers.append(test)
for x in thermometers:
    print(x.GetTemp())