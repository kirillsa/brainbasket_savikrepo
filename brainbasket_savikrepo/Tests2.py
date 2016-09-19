L = [1,2,3]
d = {1:2,2:4,3:9}
print (d[1])
d[1] = 1
print (d[1])
def dict_invert(d):
    res = {}
    for key,val in d.items():
        i = res.keys()
        if val in i:
            if type(res[val]) is list:
                res[val].append(key)
            else:
                res[val] = [res[val],key]
        else:
            res[val] = key
    return res
print (dict_invert({1:10,2:20,3:30, 4:10, 5:10}))
def getSublists(L,n):
    if L is []:
        return -1
    if n > len(L) or n < 0:
        return -1
    res = []
    for i in range (len(L)-n+1):
        res.append(L[i:i+n])
    return res
print (getSublists([1,2,3,4],3))
def longestRun(L):
    if L is []:
        return -1
    run = 1
    maxrun = 0
    for i in range (len(L)-1):
        if L[i] < L[i+1]:
            run += 1
            if maxrun < run:
                maxrun = run
        else:
            run = 1
    return maxrun
print (longestRun([1,2,3,4,1,2,1,4,5,6,7]))
