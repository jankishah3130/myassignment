l=int(input("enter the length of the two equal sides: "))
w=int(input("enter the length of the unequal side: "))
from math import sqrt
s=sqrt((l**2)-(w**2)/4)
area_of_isosceles_triangle=(0.5*(s*w))
perimeter_of_isosceles_triangle=((2*l)+w)
print(f'area of isosceles triangle:{area_of_isosceles_triangle}')
print(f'perimeter of isosceles triangle:{perimeter_of_isosceles_triangle}')
