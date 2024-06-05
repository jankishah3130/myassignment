# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence 
# on a single line.
for i in range(2000,3201):
    while(i%7==0 and i%5!=0):
        print(i,end=',')
        i=i+1

# Q-1 User will input 3 ages. find the oldest one. 
a1=int(input("enter age 1: "))
a2=int(input("enter age 2: "))
a3=int(input("enter age 3: "))
if(a1>a2 and a1>a3):
    print(f'oldest age:{a1}')
elif(a2>a1 and a2>a3):
    print(f'oldest age:{a2}')
elif(a3>a1 and a3>a2):
    print(f'oldest age:{a3}')

# Q-2 Write a program that will convert celsius value to fahrenhit.
c=int(input("enter the celsius value: "))
f=((9/5)*c)+32
print(f'fahrenhit:{f}')

# Q-3 User will input 2 numbers. write a program to swap the numbers.
a1=int(input("enter the number 1: "))
a2=int(input("enter the number 2: "))
temp=a1
a1=a2
a2=temp
print(f'a1:{a1}')
print(f'a2:{a2}')

# Q-4 Write a program that will give you the sum of 3 digits.
a=int(input("enter the number: "))
if(a>=100 and a<1000):
    sum=0
    while(a>0):
        sum=sum+a%10
        a=a//10
    print(f'Total sum of 3 digit number is: {sum}')
else:
    print('Kindly enter 3 digit number.')

# Q-5 Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
a=int(input("enter the number: "))
temp=a
if(a>=1000 and a<10000):
    rev=0
    while(a>0):
        rev=rev*10+a%10
        a=a//10
    print(f'Reverse a four digit number is : {rev}')
else:
    print('Kindly enter 4 digit number.')
if(temp==rev):
    print('The reverse is true.')
else:
    print("The reverse is not true.")

# Q-6 Write a program that will tell whether the number entered by the user is odd or even.
# check the number if it is odd or even.
a=int(input("enter the number: "))
if(a%2==0):
    print('the number is even')
else:
    print('tne number is odd')

# Q-7 Write a program that will tell whether the given year is a leap year or not.
year=int(input('Enter the year : '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

# Q-8 Write a program to find the euclidean distance between two coordinates.
x1=int(input('The coordinates of one point "x1" is : '))
y1=int(input('The coordinates of one point "y1" is : '))
x2=int(input('The coordinates of other point "x2" is : '))
y2=int(input('The coordinates of other point "y2" is : '))
import math
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(f'The euclidean distance between two coordinates is : {d}')

# Q-9 Write a program that take a user input of three angles and will find out whether it can 
# form a triangle or not.
a1=int(input("enter the value of 1st angle : "))
a2=int(input("enter the value of 2nd angle : "))
a3=int(input("enter the value of 3rd angle : "))
if(a1+a2+a3==180):
    print('It can form a triangle.')
else:
    print('it can not be form a triangle.')

# Q-10 Write a program that will take user input of cost price and selling price and determines whether its a 
# loss or a profit.
cost_price=int(input("enter the value of cost price: "))
selling_price=int(input("enter the value of selling price: "))
if(cost_price<selling_price):
    print('Its a profit.')
else:
    print('Its a loss.')

# Q-11 Write a program to find the simple interest when the value of principle,rate of interest and time period 
# is given.
p=int(input("enter the value of principle: "))
r=int(input("enter the value of roi: "))
n=int(input("enter the value of time period: "))
si=(p*r*n)/100
print(f'simple intrest:{si}')

# Q-12 Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk 
# is 40Rs.
r=int(input("Enter the value of the radius of the circular base: "))
h=int(input("Enter the value of the height of the cylinder: "))
import math
v=(math.pi)*(r**2)*h               # v value is in meter cube. (1 meter cube=1000 litre)
print(f'The volume of the cylinder is : {v}')
cost=v*1000*40
print(f'Cost of the milk is : {cost}')

# Q-13 Write a program that will tell whether the given number is divisible by 3 & 6.
a=int(input("enter the value: "))
if(a%3==0 and a%6==0):
    print('number is divisible')
else:
    print('number is not divisible')

# Q-14 Write a program to find the angle between hour and minute hand.
h=int(input("Enter the value of hour: "))
m=int(input("Enter the value of minute: "))
angle=abs((h*30)-((11/2)*m))
min_angle=min(360-angle,angle)
print("{}:{} makes the min.angle of {}°".format(h,m,min_angle))

# Q-15 Write a program to find if the given two rectangles are overlap or not.
r1_b=int(input("Enter the botton size value of rec 1 : "))
r1_t=int(input("Enter the top size value of rec 1 : "))
r1_l=int(input("Enter the left side value of rec 1 : "))
r1_r=int(input("Enter the right size value of rec 1 : "))
r2_b=int(input("Enter the botton size value of rec 2 : "))
r2_t=int(input("Enter the top size value of rec 2 : "))
r2_l=int(input("Enter the left side value of rec 2 : "))
r2_r=int(input("Enter the right size value of rec 2 : "))
if(r1_b>=r2_t or r2_b>=r1_t or r1_r<=r2_l or r2_r<=r1_l):
    print("Rectangles are not overlap.")
else:
    print("Rectangles are overlap.")

# Q-16 Write a program that will determine weather when the value of temperature and humidity is provided 
# by the user.
# TEMPERATURE(C)	HUMIDITY(%)	  WEATHER
#     >=30	           >=90	      Hot and Humid
#     >=30	            <90	      Hot
#      <30	           >=90	      Cool and Humid
#      <30	            <90	      Cool
t=int(input("Enter the value of temperature: "))
h=int(input("Enter the value of humidity: "))
if(t>=30 and h>=90):
    print("Weather is Hot and Humid.")
elif(t>=30 and h<90):
    print("Weather is Hot.")
elif(t<30 and h>=90):
    print("Weather is Cool and Humid.")
elif(t<30 and h<90):
    print("Weather is Cool.") 

# Q-17 Write a program that will take three digits from the user and add the square of each digit.
n=int(input("Enter three digit number: "))
rem=0
add=0
while(n>0):
    rem=(n%10)**2
    add=add+rem
    n=n//10
print(f'Addition of the square of each digit is : {add}')

# Q-18 Write a program that will check whether the number is armstrong number or not.
n=int(input("Enter the number: "))
temp=n
l=len(str(n))
sum=0
while(n!=0):
    a=n%10
    sum=sum+(a**l)
    n=n//10
if(temp==sum):
    print(f"Your given number {temp} is armstrong number.")
else:
    print(f"Your given number {temp} is not armstrong number.")

# Q-19 Write a program that will take user input of (4 digits number) and check whether the number is narcissist 
# number or not.
# Narcissistic number and Armstrong number are the same. It is just different terms referring to the same thing.
n=int(input("Enter the number: "))
temp=n
l=len(str(n))
sum=0
while(n!=0):
    a=n%10
    sum=sum+(a**l)
    n=n//10
if(temp==sum):
    print(f"Your given number {temp} is narcissist number.")
else:
    print(f"Your given number {temp} is not narcissist number.")

# Q-20 Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%) and 
# tax(if salary is between 5-10 lakh–10%),(10-20lakh–20%),(20<above-30%)and(0-5lakh print k).
ctc = int(input("Enter your CTC : "))
hra = ctc * 0.1
da = ctc * 0.05
pf = ctc * 0.03
remaining_ctc = ctc - (hra + da + pf)
if (remaining_ctc<=500000):
    print("k")
elif (remaining_ctc>500000 and remaining_ctc<=1000000):
    remaining_ctc = remaining_ctc - (remaining_ctc * 0.1)
    print(f"Your CTC after deduction : {remaining_ctc}")
elif (remaining_ctc>1000000 and remaining_ctc<=2000000):
    remaining_ctc = remaining_ctc - (remaining_ctc * 0.2)
    print(f"Your CTC after deduction : {remaining_ctc}")
elif (remaining_ctc>2000000):
    remaining_ctc = remaining_ctc - (remaining_ctc * 0.3)
    print(f"Your CTC after deduction : {remaining_ctc}")
