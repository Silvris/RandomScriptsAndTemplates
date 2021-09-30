import math

def genericSeries(a,r,n): #a = x-naut, r = ratio, n = number of terms
    S = a * (1 - pow(r,n)) / (1 - r)
    return S

depth = 7

result = genericSeries(1,4,depth)
print(result)