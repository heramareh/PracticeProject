#encoding=utf-8

import A
print A.add(2, 3)

import A as mymath
print mymath.subtract(3, 2)

from A import *
print multiply(2, 3)

from A import divide
print divide(3, 2)