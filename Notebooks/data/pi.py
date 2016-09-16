'''
File: pi.py
Functions that can be used to approximate pi.
'''

def leibniz(N):
    '''Compute pi via an accelerated Leibniz summation.'''
    lpi = 0.0
    for n in range(1,N):
        if n % 2:
            sign = 1
        else:
            sign = -1
        lpi += 1.0*sign/(2*n-1)
    return 4.0*lpi

def sharp(N):
    '''Compute pi via the Sharp summation.'''
    spi = 0.0
    for n in range(N):
        if n % 2:
            sign = -1
        else:
            sign = 1
        num = 2*sign*3**(0.5-n)
        denom = 2*n+1
        spi += num/denom
    return spi

def monte_carlo(N):
    '''Compute pi via Monte Carlo.'''

    import random,math
    inCircle = 0

    for n in range(N):
        x = -0.5 + random.random()
        y = -0.5 + random.random()
        r = math.sqrt(x**2 + y**2)

        if r <= 0.5:
            inCircle += 1

    mcpi = 4.0*inCircle / (1.0*N)
    return mcpi

def main():
    # The order of our pi approximations
    N = 5*10**6
    
    # output to the terminal
    print('Leibniz     π = %16.14f' % leibniz(N))
    print('Sharp       π = %16.14f' % sharp(N))
    print('Monte Carlo π = %16.14f' % monte_carlo(N))

if __name__ == '__main__':
    main()

