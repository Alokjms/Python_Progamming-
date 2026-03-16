#in this section we are going to discuss finding Area,perimeter and diagonal of a rectangle 
#the length and breadth are given by user input

import math #since i will use mathmatical module 

l=float(input("Enter the lenght of rectangle : "))
b=float(input("Enter the breadth of rectanlge : "))

if l>0 and b>0:
    area=l*b
    perimeter=2*(l+b)
    diagonal=math.sqrt(l*l+b*b)
    print(f'the area of Rectangle is {area} , the perimeter is {perimeter} and diagonal is {diagonal}')
else:
    print("Enter the positive length or breadth ")