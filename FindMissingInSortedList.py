from random import randint
from re import M

iterations = 0

sortedList = list()

for i in range(10):
    sortedList.append(i)

sortedList.remove(randint(0,9))

#print(len(sortedList))
#print(sortedList)

def FindMissingInSorted(sorted,l,r):
    global iterations
    m = (r-l)//2 + l
    print(m+1)
    print(sorted[m])
    iterations += 1
    if(m == l):
        if (sorted[m] == m):
            return m+1
        else:
            return m
    elif (m+1 == sorted[m]):
        return FindMissingInSorted(sorted,l,m)
    else:
        return FindMissingInSorted(sorted,m,r)

missing = FindMissingInSorted(sortedList,0,9)
print("Missing = {}".format(missing))
print("Iterations = {}".format(iterations))