#row = [WHITE_PAWN for i in range(8)]
#print("row : ",row)

squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]
odds = [x for x in squares if x % 2 != 0 ]
evens = [x for x in squares if x % 2 == 0 ]


print("result : odds :",odds)
print(" Evens : ",evens)
print("squares :",squares)
print("twos :",twos)
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.


highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

cubed = [num ** 3 for num in range(5)]
print(cubed) 

# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

i = 0
while i <= 5 :
    i += 1
    
    if i % 2 == 0:
      break
    print("*")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")




my_list = [1, 2, 3]
for v in range(len(my_list)):
    print(my_list[v])
    my_list.insert(1, my_list[v])
print(my_list)

my_list = [i for i in range(-1, 2)]
print(my_list)







