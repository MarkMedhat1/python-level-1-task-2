import math
loanAmount = 100000
monthlyInterstrate = 0.01
notears =7
monthlypayment = (loanAmount*monthlyInterstrate)/(1-(1/math.pow(1+monthlyInterstrate, notears*12)))
totalpayment = monthlypayment*notears*12
print(monthlypayment)
print(totalpayment)