#While loop
i = 0
while i<10:
    print("Yes " + str(i))
    i = i + 1

print("Done")

#printing list using While loop
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1

#For loop
for i in range(10):
    print(i)
else:
    print("This is inside else of for")

#range function
for i in range(1, 8, 1):
    print(i)


#Continue
for i in range(10):
    if i == 5:
        continue
    print(i)

#Break
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")


#Example 
#Star pattern
n = 4

for i in range(4):
    print("*" * (i+1))

#Factrioal

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")

#Prime number
num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

# Pattern
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()


for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()