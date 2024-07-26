def prime_num(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(f"number {num} is a prime number")
    else:
        print(f"number {num} is not a prime number")    








while True:
    num=int(input("enter the number"))
    prime_num(num)
