def factors_num(num):
    for i in range(1,num+1):
        if num%i==0:
            print(f"This are the factors:-{i}")




while True:
    num=int(input("ENter the numberto find factor"))
    factors_num(num)