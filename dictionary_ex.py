
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
print(v)

for k in range(len(dictionary)-1):
    print("ret",v)
    v = dictionary[v]
    print("ret1",v)
print(v)

#sorted 

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Insert your code here.
    print(k[0])
