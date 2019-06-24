
# Tuplas nombradas
from collections import namedtuple
Punto = namedtuple("Punto", "x y")
p=Punto(1,2)
print(p)
print(p.x, p.y)
print(p[0], p[1])

from collections import OrderedDict

d = {3:3,2:2,1:1,5:5,8:8,6:6}
print(d)
d = OrderedDict(d)

print(d[8])

