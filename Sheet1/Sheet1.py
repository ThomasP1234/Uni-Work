# # Computational Mathematics
# ## Problem sheet 1
# ## 2025-10-27
# ## Thomas Preston (thomas.preston@wadham.ox.ac.uk)
# ## Wadham College

#
# ***
# ### Question 1.
#

def getCubes(maxSize, numberToGenerate):
    cubes = [] # store seen ones to avoid cubes that can be written in multiple ways
    for d in range(1,maxSize):
        cubeD=d**3
        for c in range(1,d): # c<d as b,a≠0
            cubeC=c**3
            for b in range(1,c): # b<c to avoid duplicate solutions
                cubeB=b**3
                for a in range(1,b):
                    cubeA=a**3
                    if (cubeD==cubeA+cubeB+cubeC) and not(d in cubes):
                        print(f"{a}³\t+{b}³\t+{c}³\t={d}³")
                        cubes.append(d)
                        if len(cubes)==numberToGenerate:
                            return
maxSize = 50
cubesToGenerate=5
getCubes(maxSize, cubesToGenerate)

#
# ***
# ### Question 2.
#

import fractions
root2 = fractions.Fraction(2**(0.5))
approximations = set()
n=1
while len(approximations)<10:
    x=root2.limit_denominator(n)
    if not(x in approximations): 
        approximations.add(x)
        print(f"{x}\t={float(x)}")
    n+=1

#
# ***
# ### Question 3.
#

import mpmath
mpmath.mp.dps = 100
def newGuess(x, s):
    return (x + (s/x))/2
s=mpmath.mpf("2")
x =mpmath.mpf('0') # inital value just to start the while loop
next_x=mpmath.mpf("1.4")
while not(mpmath.almosteq(x-next_x,0,1e-50)):
    x=next_x
    next_x=newGuess(x,s)
print(next_x)
# requires 5 iterations for 50dp
# requires 7 iterations for 100dp
# requires 8 iterations for 200dp
# obtained by changing line 3 to = number greater than required dps and line 12 to 1e-(dps required)