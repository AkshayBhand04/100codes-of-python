def factorial_of_n(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"The factorial of {n} is {fact}")    





while True:
    n=int(input("Enter the num for finding factorial"))
    factorial_of_n(n)
