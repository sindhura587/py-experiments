
# Append and remove
# step 1
beatles=[]
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 2
print("Step 2:", beatles)
for i in range(2):
    beatles.append(input("Enter new band member : "))

# step 3
print("Step 3:", beatles)
length = len(beatles)
for i in range(1,3):
    # print("i : ",i)
    # print("len(beatles)-i : ",len(beatles)-i)
    del beatles[length-i]
# step 4
print("Step 4:", beatles)
beatles.insert(0,"Ringo Starr")
# step 5
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))
