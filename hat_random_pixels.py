#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random 
sense = SenseHat()
#random pixel below
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
x = random.randint(0,7)
y = random.randint(0,7)
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
sense.set_pixel(x, y, (r, g, b))
time.sleep(1)
sense.clear()

