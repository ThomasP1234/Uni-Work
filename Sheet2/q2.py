import numpy
def primes(N):
    prime = numpy.array([True for n in range(N+1)]) # This generates an array where prime[index] returns whether index is prime or not
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
N=2001 # As p<2000 p+2<2002
p=primes(N)
twinPrimes = [(p[i],p[i]+2) for i in range(len(p)-3) if p[i]+2 in p]
print(f"There are {len(twinPrimes)} twin primes where p is less than {N-1}:")
for pair in twinPrimes:
    print(f"{pair[0]}, {pair[1]}")