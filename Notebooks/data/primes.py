# generate all the non-primes (easy)
non_primes = [j for i in range (2,8) for j in range(i*2,50,i)]

# exclude anything but primes
primes = [x for x in range(2,50) if x not in non_primes]
print(primes)

# In a single line:
print([x for x in range(2,50) if not [t for t in range(2,x) if not x%t]])
