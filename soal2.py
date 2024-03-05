
acount={'bank':0}
while 1:
    print('what do you want to do')
    print('help center | rize , withdraw , credit')
    x=input()
    if(x == 'rize'):
        print('give us how much')
        rized_money=input()
        try:
            x=int(x)
        except ValueError:
           x=float(x)
        acount['bank']+=rized_money
    elif(x == 'withdraw'):
        print('give us how much')
        whithdraw_money=input()
        acount['bank']-=whithdraw_money
    elif(x == 'credit'):
        print(acount['bank'])
    else:
        print('invalid')

        

    
