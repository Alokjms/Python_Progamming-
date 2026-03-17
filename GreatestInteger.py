#Here we will see which is greatest integer among three integers
num1=int(input("Enter the first integer: "))       
num2=int(input("Enter the second integer: "))   
num3=int(input("Enter the third integer: ")) 

if num1>num2 and num1>num3:
    print(f'The number{num1} is greatest number')
elif num2>num1 and num2>num3:
    print(f'the number {num2} is greatest number ')
else:
    print(f'the number {num3} is greatest number ')