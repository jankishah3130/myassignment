# Question 1 : write a python program to check if a number is positive, negative or zero.
number=int(input("Enter the number which you want to check: "))
if(number>0):
    print(f'{number} is positive')
elif(number<0):
    print(f'{number} is negative')
elif(number==0):
    print(f'{number} is zero')
else:
    print("Try Again")

# Question 2 : write a python program to get the factorial number of given number.
number=int(input("Enter the number: "))
factorial=1
while(number>0):
    factorial=number*factorial
    number -= 1
print(f'The factorial number is: {factorial}')

# Question 3 : write a python program to get the fibonacci series of given range.
number=int(input("Enter the number: "))
a,b=0,1
if(number<=0):
    print(a)
else:
    print(a,',',b,end=",")
    for i in range(2,number):
        c=a+b
        print(c,end=",")
        a=b
        b=c

# Question 4 : write python program that swap two number with temp variable and without temp variable.
# Ans 4 : with temp variable
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
temp=0
if(a!=b):
    temp=a
    a=b
    b=temp
    print(f'swap numbers are: {a,b}')
else:
    print(f'swap numbers are: {a,b}')
# Ans 4 : without temp variable
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
a=a+b
b=a-b
a=a-b
print(a,b)

# Question 5 : write a python program to find whether a given number is even or odd, print out an appropriate
# message to the user.
number=int(input("Enter the number which you want to check: "))
if(number%2==0):
    print(f'{number} is even number.')
else:
    print(f'{number} is odd number.')

# Question 6 : write a python program to test whetehr a passed letter is a vowel or not.
# Ans 6 : first method
alphabet=input("enter the alphabet: ")
if(alphabet=="a" or alphabet=="e" or alphabet=="i" or alphabet=="o" or alphabet=="u" or 
   alphabet=="A" or alphabet=="E" or alphabet=="I" or alphabet=="O" or alphabet=="U"):
    print(f"{alphabet} is a vowel")
else:
    print(f"{alphabet} is not a vowel")
# Ans 6 : second method
vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
alphabet = input("Enter a alphabet: ")
if alphabet in vowels:
  print(f"{alphabet} is a vowel")
else:
  print(f" {alphabet} is not a vowel")

# Question 7 : write a python program to sum of three given integers. however, if two values are equal sum 
# will be zero.
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if(a==b or b==c or c==a):
    sum=0
    print(f"Sum will be:{sum}")
else:
    sum=a+b+c
    print(f"Sum of 3 numbers are:{sum}")

# Question 8 : write a python program that will return true if the two given integer values are equal or their
# sum or difference is 5.
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
sum=a+b
difference=abs(a-b)
print(a is b or sum==5 or difference==5)

# Question 9 : write a python program to sum of the first n positive integers.
n=int(input("enter the number: "))
sum=(n*(n+1)/2)
if(n<=0):
    print("Please enter positive number.")
else:
    print(f'Sum of positive interger is:{sum}')

# Question 10 : write a python program to calculate the length of a string.
string=input("enter the values: ")
print(len(string))
