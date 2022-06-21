a = 8

#1. if-elif-else ladder in Python
if(a<3): 
     print("The value of a is greater than 3")
elif(a>13):
     print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
     print("The value of a is greater than 17")
else:
     print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")

#Excercise
#1,printing greater age
age = int(input("Enter your age: "))

if age>18:
    print("Yes")
else:
    print("No")

#2.
a = 6
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")


#in and is concpet
a = None
if (a is None):
     print("Yes")
else:
     print("No")

a = [45, 56, 6]
print(435 in a)

#Excercise
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")

#2.
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")