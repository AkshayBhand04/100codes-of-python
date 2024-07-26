def prime_in_range(start,end):
    for i in range(start,end+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count==2:
            print(f"prime numberes are:-{i}")










while True:
    start=int(input("Enter the starting"))
    end=int(input("Enter the ending"))
    prime_in_range(start,end)
