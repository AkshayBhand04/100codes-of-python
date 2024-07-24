def check_positive_or_negative(n):
       if n>=0:
           print("The number is positive")
       elif n<0:
           print("The number is negative") 
      
     
while True:#while loop is for repeatedly asking the input and printing the output
    num=float(input("Enter the number"))
    check_positive_or_negative(num)
    print("")


