def strong_num(num):
    sum=0
    for i in num:
        fact=1
        for j in range(1,int(i)+1):
            fact=fact*int(j)
        print(fact)    
        sum=sum+fact
    print(sum)
    
    if sum==int(num):
        print("strong number")        
    else:
        print("not a strong num")



while True:
    num=input("Enter the number to find it is strong or not:-")
    strong_num(num)