def iterPower(base, exp):
    mul = 1
    for i in range (exp):
        mul *= base
    return mul
def recurPower(base,exp):
    if exp < 0:
        return 0
    if exp is 0:
        return 1
    if exp is 1:
        return base
    return base * recurPower(base,exp-1)
def recurPowerNew(base,exp):
    if exp < 0:
        return 0
    if exp is 0:
        return 1
    if exp is 1:
        return base
    if exp > 0 and exp % 2 == 0:
        return (base*base)**(exp/2)
    if exp > 0 and exp % 2 == 1:
        return base * recurPower(base,exp-1)
def gcdIter(a, b):
    if a < 0 or b < 0:
        return 0
    minim = min(a,b)
    for i in reversed(range(minim+1)):
        if ((a % i) is 0) and ((b % i) is 0):
            return i
def gcdRecur(a, b):
    if a < 0 or b < 0:
        return 0
#    return a if b == 0 else gcdRecur(b, a % b)
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
def lenIter(aStr):
    length = 0
    for i in aStr:
        length += 1
    return length
def lenRecur(aStr):
    global length
    if aStr is '':
        length = 0
        return 1
    else:
        lenRecur(aStr[1:])
        length += 1
        return length
def isIn(char,aStr):
    if len(char)>1:
        return False
    i = int(len(aStr) / 2)
    if len(aStr) == 1 and char != aStr[i]:
        return False
    if char == aStr[i]:
        return True
    elif char < aStr[i]:
        return isIn(char,aStr[:-i])
    else:
        return isIn(char,aStr[i:])
def semordnilap(str1,str2):
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return True
    elif len(str1) == 1 and len(str2) == 1 and str1 != str2:
        return False
    else:
        return semordnilap(str1[1:],str2[:-1])
def semordnilapWrapper(str1,str2):
    if len(str1) == 1 or len(str2) == 1:
        return False
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return False
    return semordnilap(str1,str2)
#------------------------------------------
print (iterPower(3,5))
print (recurPower(3,5))
print (recurPowerNew(3,5))
print (gcdIter(9,12))
print (gcdRecur(9,12))
print (lenIter('qwer'))
print (lenRecur('qwer'))    #как обойтись без глобальной переменной???
print (isIn('c','abcde'))
print (semordnilapWrapper('asdf','fdsa'))
