
def nb_year(p0, percent, aug, p):
    year = 0
    temp = p0
    while temp < p:
        temp = int(temp * (percent / 100 + 1) + aug)
        year += 1
    return year