print('Loan Calculator')
amount=float(input('Enter the amount borrowed: '))
i_rate=float(input('Enter the interest rate: '))
term=float(input('Enter the term(years): '))
print('The Amount Borrowed: $',amount)
print('Interest Rate: $',i_rate)
print('\tAmount\tRemaining')
print('Pytm#   Paid\tBalance')
amount=amount+i_rate
paid=(amount)/(term*12)
print(paid)
for x in range(1,(int(term)*12)+1):
        amount=amount-paid
        amount=round(amount,2)
        print(x,'\t$',round(paid,2),'\t$',amount)

