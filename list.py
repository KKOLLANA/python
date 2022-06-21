
a = [1, 2 , 4, 56, 6]
# Access using index using a[0], a[1], a[2]
print(a[2])

# Change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "kiran", False, 6.9]
print(c)


friend = ["Apple","Akash","rohan",7,False]
print(friend)

#added value to the list
list=[1,2,3,4,5]
list[0]=7
print(list)

#List indexing
l1=[7,9,"kiran"]
print(l1[0])
print(l1[0:2])


#List Methods

l2=[1,8,7,2,21,15]
l2.sort()
print(l2)
l2.reverse() # reverses the list
print(l2)
l2.append(45) # adds 45 at the end of the list
print(l2) 
l2.insert(2, 544) # inserts 544 at index 2
print(l2)
l2.pop(2) # removes element at index 2
print(l2)
l2.remove(21) # removes 21 from the list
print(l2)


# sum of list values
a = [2, 4, 56, 7]

#Two ways to DO sum
print(a[0] + a[1] + a[2] + a[3])
print(sum(a))
