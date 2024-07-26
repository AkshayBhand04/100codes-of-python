def perfect_num(num):
        arr=[]
        for i in range(1,num+1):
          if num%i==0:
            arr.append(i)
        j=0
        sum=0
        while j<len(arr)-1:
            sum=sum+arr[j]
            j=j+1
        if sum==num:
            print("entered number is a perfect number")
        else:
            print("not a perfect number")    



while True:
    num=int(input("Enter the number"))
    perfect_num(num)
