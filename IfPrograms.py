#If Related programs
#Check the given number is positive or negative
i=int(input("Enter a number: "))

if i>0:
    print("given NUmber is Positive")
elif i==0:
    print("given Number is Zero")
elif i<0:
    print("given Number is Negative")

#Check the number is even or odd
if i%2==0:
    print("given Number is Even")
else:
    print("given Number is Odd")

#check whether the person is eligible for vote or not
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")

#To check whether the student is passed or failed
if i>=35:
    print("Student is Pass")
else:
    print("Student is Fail")

#Largest of 2 numbers
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))

if num1>num2:
    print("Given Number is Largest number")
else:
    print("Given Number is Smallest number")


#check if the number is divisible by 2 and 3
if i%2==0 and i%3==0:
    print("given number is divisible by both 2 and 3")
else:
    print("given number is not divisible by both 2 and 3")


