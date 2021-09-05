# DataTypes, Conditions, Loops, In-build data structures with operations
# Python 3.9v


####################################################################################################
####################################################################################################
#### Data Types ####################################################################################
####################################################################################################
####################################################################################################

###############
### Integers ##
###############
x = 5
print(x, "is of type:", type(x))

# Basic arthematic to do on integers
a = x + 2
print('x + 2 adding a value to existing int x results: ', a) # adding

b = x - 2
print('x - 2 subtracting a value to existing int x results: ', b) # sub

c = x * 2
print('x * 2 multiply a value to existing int x results: ', c) # multi

d = x ** 2
print('x ** 2 exponential to a int x results: ', d) # expo

e = x / 2
print('x / 2 to get results of dividing a value to existing int x results: ', e) # divide and gives float

f = x // 2
print( 'x // 2 dividing and rounding a value to existing int x results: ', f) # divide and round or floor division

g = x % 2
print('x % 2 to get reminder of division =', g) # Finding reminder

h = x/float(5)
print(h) # type casting to convert a number to float to get floating point result

x += 5
print(x) # adding inplace
x -= 5
print(x) # subtracting inplace
x *= 5
print(x) # multiplying inplace, similarly

print(-x) # negate
print(+x) # unchanged 
del(x) # deletes the integer



#############
### Floats ##
#############

# all the operations are similar to ints

# floating point representaion error
print(0.1+0.2)


###########
### Char ##
###########





#############
### String ##
#############
s = 'sss'
ss = "ssss"
print(s, "is of type:", type(s))
print(ss, "is of type:", type(ss))

# indexing



####################################################################################################
####################################################################################################
#### Data Structures ###############################################################################
####################################################################################################
####################################################################################################


############
### Lists ##
############
l = [1, 2, 3]
print(l, type(l)) 
l = [1, 2, 3]
# lists are mutable
# allows duplicates
# allows different data types
dictionary = {1 : 2, 2 : 3}




#append, to add elements
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
l.append(6)
l.append(-1.2)
l.append('a')
l.append((5,6))
l.append({3:4, 5:6})
l.append(dictionary)
print(l)
print()

# extends to concatinate another list/tuple/dict/set
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
e = [1, 2, 3]
e.extend(l) # take mutable object as input
e.extend(dictionary) # Dictionary keys are added not values
e.extend((2,3)) # adding a tuple
e.extend('String') # string is inserted one letter at a time
e.extend('c') # integer,float is not mutable
print(e)

#insert
#Insert an item at a given position. The first argument is the index of the element before which to insert,
#so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
l.insert(3, 4) # index = 3, value = 4
l.insert(4,'String') # index = 4, value = String
l.insert(5, {'x':'y', 'z':'a'})
l.insert(6, ['x','y','z','a'])
l.insert(7, ('x','y','z','a'))


# remove
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
print(l, "before")
l.remove(4)
print(l, "after")

# pop
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
# (The square brackets around the i in the method signature denote that the parameter is optional,
# not that you should type square brackets at that position. You will see this notation frequently in the
# Python Library Reference.)
l.pop()
l.pop(0)
print(l)

# index

new_l = [1,2,3,4]
new_l2 = ['hi', 'there', 'python', 'user', 'python', 'is', 'so', 'much', 'python', 'fun']
print(e.index(2), "e.index(2)")
print(new_l.index('python',0,2), "e.index(2)")


#############
### Tuples ##
#############




###################
### Dictionaries ##
###################




############
### Sets ###
############




######################
### Lists as Queues ##
######################


######################
### Lists as Stacks ##
######################


#[[row[i] for row in matrix] for i in range(4)]


