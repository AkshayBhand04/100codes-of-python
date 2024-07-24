def armstrong_num(num,n):
    sum=0
    for i in num:
        sum=sum+int(i)**n
    print(sum)  
    if(sum==int(num)):
        print("THe number ",num,"is a armstrong number")
    else:
        print("The number",num," is not a armstrong number")    



while True:
    num=input("ENter the number")
    length=len(num)
    print(length)
    armstrong_num(num,length)