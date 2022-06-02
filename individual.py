#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a=int(input("Enter the length of the larger base a: "))
b=int(input("Enter the length of the smaller base b: "))
alpha=int(input("Enter the angle at a larger base in degrees: "))
alphar=alpha*math.pi/180
print("The area of the trapezoid is equal to ",(a**2-b**2)/4*math.tan(alphar))
