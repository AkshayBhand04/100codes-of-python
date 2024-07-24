def sum_of_digits(num):
    sum=0
    for i in num:
        sum=sum+int(i)
    print("The sum of digits in number is:-",sum)


while True:
    num=input("Enter the number")
    sum_of_digits(num)        