a=int(input("enter the side a of triangle: "))
b=int(input("enter the side b of triangle: "))
c=int(input("enter the side c of triangle: "))
from math import sqrt
s=(a+b+c)/2
area_of_scalene_triangle=sqrt(s*(s-a)*(s-b)*(s-c))
perimeter_of_scalene_triangle=a+b+c
print(f'area of scalene triangle:{area_of_scalene_triangle}')
print(f'perimeter of scalene triangle:{perimeter_of_scalene_triangle}')
