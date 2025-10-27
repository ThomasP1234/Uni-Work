import mpmath

mpmath.mp.dps = 100

def newGuess(x, s):
    return (x + (s/x))/2

s=mpmath.mpf("2")
x =mpmath.mpf('0')
next_x=mpmath.mpf("1.4")

while not(mpmath.almosteq(x-next_x,0,1e-50)):
    x=next_x
    next_x=newGuess(x,s)
print(next_x)

# requires 5 iterations for 50dp
# requires 7 iterations for 100dp
# requires 8 iterations for 200dp

# obtained by changing line 3 to = number greater than required dps and line 12 to 1e-(dps required)