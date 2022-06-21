# tuple
t = (1, 2, 4, 5)

t1 = () # Empty tuple
t1 = (1) # Wrong way to declare a Tuple with Single element
t1[1] = 2 # Tuple with Single element
print(t1)

# Printing the elements of a tuple
print(t[0])

# Cannot update the values of a tuple
t[0] = 34 # throws an error

#tuple methods

t = (1, 2, 4, 5, 4, 1, 2,1 ,1)

print(t.count(1))
print(t.index(5))


#Change the value in tuple
a = (2,4,5,3,2)
a[0] = 45
