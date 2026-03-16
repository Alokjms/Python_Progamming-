#in this section we will find Area,circumference and diameter of circle if radius is given
import math

r=float(input("Enter the radius of circle : "))

if r>0:
    area=math.pi*r*r
    circumference=2*math.pi*r
    diameter=2*r
    print(f'the area of circle is : {area} ,the circumference is : {circumference} and diameter is {diameter}')
else:
    print("Please enter the positive radius")