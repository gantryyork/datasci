def fibinaccis( N ):
    return

def primes( N ):
    return

def factoral( n ):
    return

def factors( n ):
    return

def is_number( n ):
    try:
        float(n)
    except ValueError:
        return False

    return True
    

def is_prime( n ):

    #print( 'checking {0}'.format(n) )

    if n == 4:
        return False

    for divisor in range(2, int(n/2 + .5) ):
        #print( 'divisor {0}'.format(divisor) )
        if n/divisor == int(n/divisor):
           return False
    return True


def is_odd( n ):

    if n == 0:
        return False

    if n/2 == int(n/2):
        return False

    return True


def is_even( n ):

    if n/2 == int(n/2):
        return True

    return False
