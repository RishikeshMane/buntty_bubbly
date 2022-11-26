num=int(input("enter the number:- "))

if (num<0):
    print("enter positive number")

elif(num==0):
    print("factorial is 1")

else:

    for i in range(1,num):
        num=num*i
    print("factorial is",num)