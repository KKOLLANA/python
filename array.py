from array import*

vals = array('i',[1,4,2,5,3,])
print(vals)

#functions
print(vals.buffer_info())  #OUTPUT woll be in tuple form 
print(vals.reverse())
print(vals.typecode())

#printing one by one value
vals = array('i',[1,4,2,5,3,])
for i in range(5):
    print(vals[i])


#length og vals
for e in vals:
    print(e)


#printing charaters in array
vals = array("u",['a','b','c','d'])
for i in range(4):
    print(vals[i])

#printing values by using while loop
vals =array("i",[2,3,1,5])
newArray = array(vals.typecode,(a for a in vals))
for i in newArray:
    print(i)

#printing square values
vals =array("i",[2,3,1,5])
newArray = array(vals.typecode,(a*a for a in vals))
for i in newArray:
    print(i)

#same conceptwith WHILE LOOP
vals= array("i",[1,5,34,4])
newArray = array(vals.typecode,(a for a in vals))
i=0
while i<len(newArray):
    print(newArray[i])
    i+=1

#values getting from the user
vals = array('i',[])

n = int(input("Enter the length of the array"))  #we have to give the size of the array

for i in range(n):
    x=int(input("Enter the next value"))
    vals.append(x)

print(vals)

