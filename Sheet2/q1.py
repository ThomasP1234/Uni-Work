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