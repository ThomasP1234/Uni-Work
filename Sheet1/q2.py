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