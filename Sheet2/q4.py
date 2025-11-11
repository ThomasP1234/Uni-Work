import numpy
import matplotlib.pyplot as plt

a=0.3
b=23

x_axis = numpy.linspace(-2,2,10000) # increase 10000 for higher precision
y_axis=0
k_range = numpy.array(range(0,101))

for k in k_range:
    y_axis+=numpy.pow(a,k)*numpy.cos(numpy.pow(b,k)*numpy.pi*x_axis)

plt.plot(x_axis, y_axis)
plt.gcf().set_dpi(300)

plt.show()