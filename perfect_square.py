import math
def perfect_square_or_not(num):
    squrt=math.isqrt(num)
    if squrt*squrt==num:
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")    
    






while True:
    num=int(input("ENter the number"))
    perfect_square_or_not(num)
