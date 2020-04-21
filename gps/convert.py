import math

def nm(km):
    return precision(km * 0.539957, 4)


def mi(km):
    return precision(km * 0.621371, 4)


def dms(ddeg):

    (r, d) = math.modf(math.fmod(ddeg, 360))
    (s, m) = math.modf(math.fmod(r*60, 60))

    return [int(d), int(m), int(s*60)]


def ddeg(d, m, s):

    deg = d + (m/60) + (s/3600)

    return precision(deg, 4)


def latitude(ddeg):
    return


def longitude(ddeg):

    lon_mod = math.fmod(ddeg, 360)

    lon = 0
    if lon_mod < -180:
        lon =  180 + (lon_mod + 180)
    elif lon_mod >= 180:
        lon = -180 + (lon_mod - 180)
    else:
        lon = lon_mod

    return lon

def precision(num, numdec):

    return math.trunc(num * 10 ** numdec + .5) / (10 ** numdec)


    
