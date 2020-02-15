import math


def fibinacci_series(N):

    series = list()
    for i in range(1, N+1):

        if len(series) < 2:
            series.append(i)
        else:
            a = series[len(series)-1]
            b = series[len(series) - 2]
            series.append(a+b)

    return series


def fibinacci(N):

    return fibinacci_series(N).pop()


def is_fibinacci(n):

    if fibinacci_score(n) > 0.95:
        return True

    return False


def fibinacci_score(n):

    if n in [1, 2, 3, 5, 8, 13, 21]:
        score = 1
    else:
        d = math.log(math.sqrt(5)*n, 10) / math.log((1 + math.sqrt(5))/2, 10)
        nearest_int = int(d+0.05)
        score = 1 - abs(d - nearest_int)

    return score


def prime_series(N):

    series = list()
    for i in range(0, N+1):

        if is_prime(i):
            series.append(i)

    return series


def factoral(n):

    x = 1
    for i in range(1, n+1):
        x = x*i

    return x


def factors(n):
    return


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False

    return True


def is_prime(n):

    #print( 'checking {0}'.format(n) )

    if n == 4:
        return False

    for divisor in range(2, int(n/2 + .5)):
        #print( 'divisor {0}'.format(divisor) )
        if n/divisor == int(n/divisor):
            return False
    return True


def is_odd(n):

    if n == 0:
        return False

    if n/2 == int(n/2):
        return False

    return True


def is_even(n):

    if n/2 == int(n/2):
        return True

    return False
