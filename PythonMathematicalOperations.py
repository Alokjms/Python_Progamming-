#Here we are going to perform all mathematical operations in python
#in this code we will take two numbers and perform all mathematical operations just like
#addition,substraction,multiplication,division ,remainder etc

#first of all we will take two numbers by user input

num1=float(input("Enter the first number: "))

num2=float(input("Enter the Second number: "))

#Addition of two numbers
sum=num1+num2

print(f'the sum of {num1} and {num2} is {sum}')

#multiplcation
Mulitplication=num1*num2

print(f'the multiplication of given two numbers {num1} and {num2} is {Mulitplication}')

#Division
div=num1/num2
if num2 !=0:
    print(f'when the {num1} is divided by {num2} the quotient is {div}')
else:
    print("zero is not allowed  ")

#Remainder

rem=num1%num2
if num2 !=0:
    print(f'when the {num1} is divdided by {num2} the remainder is {rem}')
else:
    print("please enter the valid number because Zero is not allowed as Second number")