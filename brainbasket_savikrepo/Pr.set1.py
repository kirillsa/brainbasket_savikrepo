#Savitskiy Kirill
#Problem set 1
#
#Problem 1
s = 'dfsefqwfdsaweo'
vow = 'euoai'
n = 0
for i in vow:
    for j in s:
        if i == j:
            n += 1
print (n)
#
#Problem 2
s = 'bobazcbobobegghaklbob'
w = 'bob'
n = 0
for i in range (0,len(s)-2):
    if (s.find(w,i,i+3)>=0):
        n += 1
print (n)
#
#Problem 3
def item_order(order):
    #order = 'salad water hamburger salad hamburger'
    s = order.split(' ')
    meal = ['salad', 'hamburger', 'water']
    count = [0,0,0]
    ind = 0
    for i in meal:
        for j in s:
            if (i == j):
                count[ind] = count[ind]+1
        ind += 1
    print ('salad:', count[0], ' hamburger:', count[1], ' water:', count[2])
item_order('salad water hamburger salad hamburger')
