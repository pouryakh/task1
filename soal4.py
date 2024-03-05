while 1:
    print('give us current temp(f or c): ')
    a=input()
    if a=='c' or a=='f':
        break
    else:
        print('invalid')
if a=='c':
    print('give us temp : ')
    c=input()
    try:
        c=int(c)
    except ValueError:
        c=float(c)
    rez= 1.8 * c + 32
    print('temp in fahrenheit isssssss = ',rez)
else:
    print('give us temp : ')
    c=input()  
    try:
        c=int(c)
    except ValueError:
        c=float(c)
    rez= (c-32) / 1.8
    print('temp in fahrenheit isssssss = ',rez) 
