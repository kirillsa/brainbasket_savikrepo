# -*- coding: utf-8 -*-
#Savitskiy Kirill
#Problem set 2
#
#Problem 1
balance = 5000
annualInterestRate = 18
monthlyPaymentRate = 2
monthlyInterestRate= annualInterestRate / 12.0
totalPaid = 0
for i in range (12):
    minimumMonthlyPayment = monthlyInterestRate / 100 * balance
    totalPaid += minimumMonthlyPayment
    balance -= minimumMonthlyPayment
    print ('Month:', i+1)
    print ('Min monthly payment:', round(minimumMonthlyPayment,2))
    print ('Ramaining balance:', round(balance,2))
    if i is not 11:
        balance += monthlyInterestRate / 100 * balance
print ('Total paid: ', round(totalPaid,2))
print ('Remaining balance: ', round(balance,2))
#
#Problem 2
print 
balance = 5000
updatedBalance = balance
annualInterestRate = 18
monthlyInterestRate = annualInterestRate / 12.0
lowPaiment = round(balance / 12 + 5, -1)
lowPaiment -= 10
while updatedBalance > 0:
    updatedBalance = balance
    lowPaiment += 10
    for i in range (12):
        updatedBalance -= lowPaiment
        updatedBalance += monthlyInterestRate /100 * updatedBalance
print ('Lowest Payment: ', int(lowPaiment))
#
#Problem 3
print 
eps = 0.1
balance = 5000
annualInterestRate = 18
monthlyInterestRate = annualInterestRate / 12.0
updatedBalance = balance * (1 + monthlyInterestRate / 100)**12
loPaim = balance / 12
upPaim = round (balance * ( 1 +monthlyInterestRate / 100) ** 12 / 12, 2)
while abs(updatedBalance) >= eps:
    updatedBalance = balance
    lowPaiment = round((upPaim+loPaim)/2, 2)
    for i in range (12):
        updatedBalance -= lowPaiment
        updatedBalance += monthlyInterestRate /100 * updatedBalance
    if updatedBalance < 0:
        upPaim = lowPaiment
    else:
        loPaim = lowPaiment
print ('Lowest Payment: ', lowPaiment, updatedBalance)
