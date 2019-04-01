#!/usr/bin/python
from phue import Bridge
import time
b = Bridge('xxxxxx')
b.connect()
lights = b.get_light_objects('name')
for i in lights:
    print(i)
for i in range(1,100):
    if i % 3 == 0:
        b.set_light(3,'on', True)
        b.set_light(1, 'bri', 254)
        time.sleep(1)
    elif i % 5 == 0:
        b.set_light(3,'on', False)
        time.sleep(1)
    else:
      time.sleep(1)
      b.set_light(3,'on', True)
      b.set_light(3, 'bri', 127)

#print(b.get_light(3, 'on'))
#b.set_light(4,'on', False)
b.set_light(3,'on', False)