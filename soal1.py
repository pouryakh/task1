while 1: 
    print('enter your input')
    x=input()
    try:
       x=int(x)
    except ValueError:
       try:
           x=float(x)
       except ValueError:
            a=len(x)
            a-=1
            if x[0]=='['and x[a]==']':
                x=list(x)
            
print(type(x))
