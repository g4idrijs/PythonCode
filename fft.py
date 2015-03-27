#!/usr/bin/python
import numpy as np
x = np.random.rand(8)
print x
xf = np.fft.fft(x)
print xf
print np.fft.ifft(xf)
n = 10
print "\n"
print np.fft.fft(np.ones(n))/n