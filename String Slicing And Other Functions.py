#Functions

'''
a="Hello World"
b="hello world"
c="HELLO WORLD"
print(b.capitalize())       
print(c.lower())            
print(b.upper())            
print(a.count("l"))         
print(a.isalnum())          # TRUE-if no space  FALSE-if space is there
print(a.isalpha())          # Checks for only alphabets in the string
print(a.endswith("d"))
print(a.find("e"))
print(a.replace("World","Suman"))
'''

#String Slicing

'''
a="Good Morning Suman"
print(a[0])
print(a[0:5])
print(a[0:])
print(a[0:25:2])
'''

#Advanced Slicing

a="Good Morning Suman"
print(a[7:9])    # If you want specific parts of the string
print(a[-4:-2])  # for negative index it starts from the end towards start so the last element will be -1 then the next will be -2 and so on
print(a[::-1])   # to reverse the string
print(a[::-2])   # reverse string skipping letters