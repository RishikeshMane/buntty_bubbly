def fac(x):
    if x==1:
        return 1;
    elif x<0:
        return ('not defined');
    else:
        return(x * fac(x-1))
num=int(input("enter the number:- "))
result=fac(num)
print("factorial of",num, "is" ,result)