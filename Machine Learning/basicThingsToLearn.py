import numpy
from scipy import stats
import matplotlib.pyplot as plt
#Mean
speed = [98,86,87,88,111,86,103,87,94,78,77,85,86]
a = numpy.mean(speed)
print(a)
#Median
b = numpy.median(speed)
print(b)
#Mode
c = stats.mode(speed)
print(c)
#Standard Deviation
d = numpy.std(speed)
print(d)
#Variance
e = numpy.var(speed)
print(e)
#Percentiles
f = numpy.percentile(speed, 69)
print(f)
#how to create random data set
g = numpy.random.uniform(0.0, 5.0, 250)
print(g)
# Histogram to draw 
plt.hist(g, 5)
plt.show()
