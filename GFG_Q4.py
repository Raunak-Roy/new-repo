#Check if element exists in list in Python
#approach1
L = [22,33,44,55,66]
findmy_number = 44
if findmy_number in L:
    print("yes existing")
else:
    print("not")

#approach2
for i in L:
    if i == 66:
        print("yes exist here ")
    else:
        print("not available in L")