# -*- coding: utf-8 -*-

import math

v0 = 15 #Km/h
tetha = 60 #graus
x = 0.5 #m
y0 = 1 #m
g = 9.81 #m/s²

#Conversão km/h para m/s
v0 = v0 / 3.6

#Conversão de tetha para radiano
tetha = tetha * 3.17 / 180

y = x*(math.tan(tetha)) - (1/(2*v0)) * (g*(x**2)/(math.cos(tetha)**2)) + y0

print("y = {:.3f} m".format(y))
