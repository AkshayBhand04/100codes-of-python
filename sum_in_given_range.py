def sum_of_num_in_given_range(start,end):
    sum=0
    for i in range(start,end+1):
        sum=sum+i
    print("The sum of the numbers in given range is:-",sum)    



while True:
    start=int(input("Enter the initial number"))
    end=int(input("Enter the end number"))
    sum_of_num_in_given_range(start,end)
