def string_times(str,n):
    strout=''
    for i in range(n):
        strout+=str
    print strout
#-------------------------------------------
def cat_dog(str):
    cat = 0
    dog = 0
    for i in range (len(str)-2):
        if str.find('cat',i,i+3)>=0:
            cat += 1
        elif str.find('dog',i,i+3)>=0:
            dog += 1
    return str.count('cat') == str.count('dog')
#-------------------------------------------      
def double_char(str):
    strOut = ''
    for i in range(len(str)):
        strOut += str[i]*2
    print strOut
#--------------------------------------------
def array_front9(nums):
    for i in range (len(nums)):
        if i == 4:
            break
        if nums[i] == 9:
            return True
    return False
#--------------------------------------------
def big_diff(nums):
    if len(nums) == 1:
        return 0
    minNum = nums[0]
    maxNum = nums[0]
    for i in range (1,len(nums)):
        minNum = min(minNum,nums[i])
        maxNum = max(maxNum,nums[i])
    return maxNum - minNum
#--------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    num = 1
    for i in range (2,n+1):
        num *= i
    return num
def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n-1)   
#--------------------------------------------
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib (n-1) + fib (n-2)
#cache = dict() == cache = {0:0,0:1}
#if n in cache:
#   return cache[n]
#else:
#    result = fib(n-1) + fib (n-2)
#    cache [n] = result
#    return result
#--------------------------------------------
def pascal(n):
    if n is 1:
        print '1'
        return [1]
    else:
        line = []
        line.append (1)
        prev_line = pascal(n-1)
        for i in range (len(prev_line)-1):
            line.append (prev_line[i] + prev_line[i+1])
        line.append (1)
        print str(line)
        return line

#--------------------------------------------
def leap (n):
    if (n%4 is 0 and n%100 is not 0) or (n%100 is 0 and n%400 is 0):
        print 'leap year'
    else:
        print 'not leap year'
#--------------------------------------------
def bubble_sort (list):
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            if list[j]>list[j+1]:
                buf = list[j+1]
                list[j+1] = list[j]
                list[j] = buf
    return list        
#--------------------------------------------
def big_number(list):
    str_out = ''
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            str1=str(list[j])
            str2=str(list[j+1])
            if str1[0]<str2[0]:
                buf = list[j+1]
                list[j+1] = list[j]
                list[j] = buf
    for i in range (len(list)):
        str_out += str(list[i])
    return int(str_out)
#--------------------------------------------
string_times('Kir',3)
print cat_dog('catdogcatdog')
double_char('the')
print array_front9([1,2,3,2,9])
print big_diff([2,10])
print factorial(4)
print factorial1(4)
print fib(4)
pascal (4)
for i in range (10):
    print fib (i)
leap (1996)
print bubble_sort([4,3,9,1,5,0])
print big_number([2,45,111,5])