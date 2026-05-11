

my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


def my_list1(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list)
print(my_list1(my_list))

print(my_list)



def func(a, b):
    return a ** a


print(func(2))



print(None+1)
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, b=2)    # Syntax Error

def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")


def is_prime(num):
    cnt=0
    for i in range(1,num+1):
        if num%i==0: cnt +=1
    if cnt==2: 
        
        return True      

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)


my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

empty_tuple = ()
print(type(empty_tuple))

#tuple creation
my_tuple_1 = 1, 
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>

#Tuples are immutable,

# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

#for i in range(count(tup)):
 #   if(i==2) : duplicates +=1

print(duplicates)    # outputs: 4


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
d4={}

print("D4",d4)
for item in (d1, d2):
    d3.update(item)
print(d3)

#list to tuple

my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)

#tuple to dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)



