myDict = {
    "Fast": "In a Quick Manner",
    "kiran": "A developer",
    "Marks": [1, 2, 5],
    "anotherdict": {'kiran': 'gamer'}
}

# print(myDict['Fast'])
# print(myDict['kiran'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['kiran'])


#Methods
myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'kiran': 'gamer'},
    1: 2
}

# Dictionary Methods

print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "kiran": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("kiran")) # Prints value associated with key "kiran"
print(myDict["kiran"]) # Prints value associated with key "kiran"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("kirankumar")) # Returns None as kirankumar is not present in the dictionary
print(myDict["kiarankumar"]) # throws an error as kirankumar is not present in the dictionary