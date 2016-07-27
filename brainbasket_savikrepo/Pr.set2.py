balance = 460
annualInterestRate = 0.4
balanceWithAnualRate = balance + balance * annualInterestRate
lowPaiment = round(balance / 12 + 5, -1)
calculatedBalance = lowPaiment * 12
while balanceWithAnualRate > calculatedBalance:
    lowPaiment += 10
    calculatedBalance = lowPaiment * 12
print ('Lowest Payment: ', int(lowPaiment))
