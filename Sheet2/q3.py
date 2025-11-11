import numpy
import matplotlib.pyplot as plt

data = { # semi-major axis in AU
    0: 0.39, # mercury
    1: 0.72, # venus
    2: 1.00, # earth
    3: 1.52, # mars
    4: 2.77, # cerus
    5: 5.20, # jupiter
    6: 9.50, # saturn
    7: 19.2, # uranus
    8: 30.1, # neptune
    9: 39.5 # pluto
}

# I have chosen to draw mercury x=-inf at x=-1 to have the planets evenly spaced but set the y-values as if it were -inf
x_values=numpy.array(list(range(-1,9)))
y_values=numpy.array([data[i] for i,value in enumerate(x_values)])

x_approx = numpy.linspace(-1,8,1000)
y_approx=numpy.array([0.4+0.3*(numpy.power(2.0, x)) for x in x_values])
y_approx[0]=0.4

plt.plot(x_values, y_values, color = "blue", label="Actual Distance")
plt.plot(x_values, y_values, 'o', markersize=4, color="blue")
plt.plot(x_values, y_approx, color = "red", label="T-B Rule Prediction")
plt.plot(x_values, y_approx, 'o', markersize=4, color = "red")

plt.legend()
plt.xticks(list(range(-1,9)), ["Mercury", "Venus", "Earth", "Mars", "Cerus", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
plt.gcf().set_dpi(300)

plt.show()