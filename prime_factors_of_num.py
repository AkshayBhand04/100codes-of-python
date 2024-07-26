def prime_factors_of_num(num):
    arr=[]#finding the factors of the number and storing inside arr
    for i in range(1,num+1):
        if num%i==0:
            arr.append(i)
    
    
    for num in arr:#checking the factors are prime or not by iteratind on the array 
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count=count+1
        if count==2:
            print(num,end=" ")        









while True:
    print("")
    num=int(input("Enter the number"))
    prime_factors_of_num(num)
