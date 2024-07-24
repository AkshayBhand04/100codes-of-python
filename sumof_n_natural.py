def sum_n_natural(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("The sum of n natural numbers is :-",sum)    
 


while True:
    n=int(input("Enter the number"))
    sum_n_natural(n)

