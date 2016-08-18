def oddTuples(aTup):
    newTup = []
    for i in range (len(aTup)):
        if i%2 == 0:
            newTup.append(aTup[i])
    return tuple(newTup)
def mul5 (i):
    return 5*i
def absi (i):
    return abs(i)
def add1 (i):
    return i+1
def square (i): return i*i
def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def howMany(aDict):
    sum = 0
    list = aDict.values()
    for i in list:
        sum += len(i)
    return sum
def biggest(aDict):
    value = 0
    for i,j in aDict.items():
        if len(j) > value:
            value = len(j)
            key = i
    return key
#------------------------------------------
print (oddTuples((3,5,3,4,3,2)))
testList = [1, -4, 8, -9]
print (applyToEach(testList, mul5))
testList = [1, -4, 8, -9] 
print (applyToEach(testList, absi))
testList = [1, -4, 8, -9] 
print (applyToEach(testList, add1))
testList = [1, -4, 8, -9] 
print (applyToEach(testList, square))
animals = {'a':['asd'],'b':['bcd'],'c':['cde']}
animals['d'] = ['def']
animals['d'].append('dog')
animals['d'].append('dingo')
print (animals)
print (howMany(animals))
print (biggest(animals))
