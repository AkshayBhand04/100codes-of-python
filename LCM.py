num1 = 5
num2 = 3
num3=8

# Calculating HCF here
for i in range(1, min(num1, num2,num3)+1):
    if num1 % i == num2 % i == 0:
        hcf = i    
print(hcf)          

# LCM formula
lcm = (num1*num2*num3)//hcf #the meanig of the // is simply dividing the multiplication but if any remainder is there then ignoring it and only taking quotient value

print("LCM of", num1, "and", num2,"and",num3, "is", lcm)
