from numpy import *

from PIL import Image


ar = ones((100,100),float32)

ar = ar * 100

for i in range(0,100):
    ar[i,:] = 100 + (i * 1.5)

im = Image.fromarray(ar,"F")
