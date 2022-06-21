a="kirankumar"
b='kiran'
c='''kiran'''
print(a,b,c)

print(a[0]) #indexing
print(a[-1])

#slicing
print(a[1:6:2])
print(a[:4])
print(a[4:])

#String fUNCTIONs
print(len(a)) #length of the string
print(a.endswith("ar")) #it gives output has True or False
print(a.count("k")) #counts the number of k's
print(a.capitalize()) #convert small to capital
print(a.replace(a,"alekhya")) #replace the name

#Excercise
name=input("enter your name")
print("good afternoon" +name)

a = input("Enter a number: ")
a = int(a) # Convert a to an Integer(if possible)
print(type(a))

