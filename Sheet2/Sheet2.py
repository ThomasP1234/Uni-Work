# # Computational Mathematics
# ## Problem sheet 2
# ## 2025-11-11
# ## Thomas Preston (thomas.preston@wadham.ox.ac.uk>)
# ## Wadham College

#
# ***
# ### Question 1.
#

import numpy
def primes(N):
    prime = numpy.array([True for n in range(N+1)])
    prime[0]=prime[1]=False # Settting 0 and 1 to not prime
    n=2
    counter = 0
    while n**2<=N:
        possiblePrimes=numpy.where(prime == True)[0]
        n=possiblePrimes[counter]
        for i in range(2*n,N+1,n):
            prime[i]=False
        counter+=1
    return numpy.where(prime == True)[0]
N=1000000
print(len(primes(N)))

#
# ***
# ### Question 2.
#

import numpy
N=2001 # As p<2000 p+2<2002
p=primes(N) # defined in Q2
twinPrimes = [(p[i],p[i]+2) for i in range(len(p)-3) if p[i]+2 in p]
print(f"There are {len(twinPrimes)} twin primes where p is less than {N-1}:")
for pair in twinPrimes:
    print(f"{pair[0]}, {pair[1]}")

#
# ***
# ### Question 3.
#

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

#
# ***
# ### Question 4.
#

import numpy
import matplotlib.pyplot as plt

a=0.3
b=23
x_axis = numpy.linspace(-2,2,10000) # increase 10000 for higher precision
# x_axis = numpy.array(numpy.arange(-2,2,0.001))
k_range = numpy.array(range(0,101))
y_axis=0
for k in k_range:
    y_axis+=numpy.pow(a,k)*numpy.cos(numpy.pow(b,k)*numpy.pi*x_axis)
plt.plot(x_axis, y_axis)
plt.gcf().set_dpi(300)
plt.show()