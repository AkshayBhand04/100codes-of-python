def check_palindrome(num):
    rev_num=num[::-1]
    if(num==rev_num):
        print("Entered number",num,"is palindrome")
    else:
        print("Entered number",num,"is not a palindrome")



while True:
    num=input("Enter the number for checkintg it is palindrome or not")
    check_palindrome(num)
