#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:28:01 2022

@author: craigrupp
"""

playlist_ratings = [10,9.5,10, 8, 7.5, 5, 10, 10]
i = 0
while i < len(playlist_ratings) and playlist_ratings[i] > 6:
    print(playlist_ratings[i])
    i += 1
    
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1

print(new_squares)

# sorted is a function and returns a new list, it does not change the list L

L=[1,3,2]
sorted(L)
[L, sorted(L)]

# sort method or list method mutates the array in place
L.sort()
L

# Operator order
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
print(c1)
# Order (2 * a1 = 8, result * b1 = 40, + a1 = 44, + b1 = 49, - 1 = 48)

# Extend
animals = ['Python', 'Viper', 'Cobra'] 
def add_snake(snake_type):
    animals.extend(snake_type)
    print(animals)

# The extend() method adds the specified list elements (or any iterable) to the end of the current list
add_snake("Boa")
add_snake([['Copperhead'], ['Mocassin']])
add_snake("Mocas  iin")


# All Elements in List
def PrintList(the_list):
    for element in the_list:
        print((element, type(element)))
        
PrintList(['1', 1, 'the man', "abc", {'2', '5'}, [3,4], (5,6)])

for x in {'3', '4'}:
    print(x)


# Global Variables
# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
printer1(internal_var1) 
# It's because all the variables we create in the function is a local variable, meaning that the variable assignment does not persist outside the function


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

# internal_var defined is given a global scope within the function

# Unknown number of arguments
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args), type(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(key + " : " + kwargs[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')



# =============================================================================
# Exception Catching
# Good Refershers
# =============================================================================
print(1/0) # Zero Division Error
a = [1, 2, 3]
a[10] # Index Error (list index out of range)


# =============================================================================
# # Try/Except
# # A try except will allow you to execute code that might raise an exception 
# # and in the case of any exception or a specific one we can handle or catch the exception and execute specific code. 
# # This will allow us to continue the execution of our program even if there is an exception.
# =============================================================================

# Examples
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
    
    

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
    
    
# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
    
# potential code before try catch

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing complete")
        
















