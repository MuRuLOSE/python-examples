# Strings...

# You cant modify strings, but can replace letters, actually replace CANNOT replace something, that is, the string is an immutable sequence

a = "Hello world" # string type variable

print(a) # Print variable
print("Hello World!") # print string

b = "Some string..."

print(b.capitalize()) # The first letter is big, the rest are small

print(b.lower()) # All letters lower

print(b.title()) # Like capitalize

print(b.upper()) # All letters caps-lock

b.replace("S","o") # Replaced the first S with an o 

print(b)