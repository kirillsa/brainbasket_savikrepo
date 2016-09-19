x = "pi"
y = "pie"
x, y = y, x
print (y,x)
tup = ([1,2],3)
print (tup)
L = [1,2,3]
d = {'a':'b'}
def f(x):
    return 3
#for i in range (101,-1,-2):
 #   print (f)
staff = "iQ"
for thing in staff:
    if thing == "iQ":
        print ("yes")
def pal(s):
    if len(s)<=1:
        return True
    if s[0] == s[-1]:
        return pal(s[1:len(s)-1])
    else:
        return False
print (pal('asabasa'))
def dotProd(listA, listB):
    if len(listA) is not len(listB):
        return False
    sum = 0
    for i in range (len(listA)):
        sum += listA[i]*listB[i]
    return sum
print (dotProd([1,2,3],[4,5,6]))
def f(s):
    return 'a' in s
def satisfies(L,f):
    global L
    res = []
    sum = 0
    for i in L:
        if f(i):
            res.append(i)
            sum += 1
    L = res
    return sum
L = ['a','b','a']
print (satisfies(L,f))
print (L)
            
    
