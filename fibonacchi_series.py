def fiboo_upto_n(n,n1,n2):
    print("fibonacchi series:-",n1,n2,end=" ")
    for i in range(2,n):#due to zero and 1 we nedd to satrt from 2
        n3=n1+n2#this eqn because numbers in fibonacchi series ae the addition of previous two numbers
        n1=n2
        n2=n3
        print(n3,end=" ")    
    

n1,n2=0,1#in fibonacchi 0 and 1 are always there i the starting 
while True:
    print("")
    n=int(input("Enter the number"))
    fiboo_upto_n(n,n1,n2)