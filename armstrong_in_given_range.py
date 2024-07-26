def armstrong_num_givenrange(start,end):
 
    for i in range(start,end+1):
        sum=0
        n=len(str(i))
        for j in str(i):
            sum=sum+int(j)**n
        if(sum==i):
            print(f"The armstrong number is:-{i}")
            print("")
        else:
            print(f"{i} is not a armstrong number")     
            print("")     
                

            



while True:
    start=int(input("enter the starting number"))
    end=int(input('enter the ending number'))
    armstrong_num_givenrange(start,end)