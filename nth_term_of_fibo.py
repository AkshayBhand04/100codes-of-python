def nth_term_of_fib(n,n1,n2):
    arr=[n1,n2]
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
        arr.append(n3)
    print(f"the fibonacchi series is {arr}")  


    large=arr[0]
    i=0
    while i<len(arr):
        if arr[i]>large:
            large=arr[i] 
        i=i+1
    print(f"The nth term of the series is {large}")   

    #another logic
    # for num in arr:
    #     if num>large:
    #         large=num
    # print(large)        

        

n1,n2=0,1
while True:
    n=int(input("Enter the number"))
    nth_term_of_fib(n,n1,n2)
