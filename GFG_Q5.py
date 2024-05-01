#Different ways to clear a list in Python
#approach1
L = [22,33,45,77,88,99]
print("before clear the list looks like :", L)
clear = L.clear()
print("after clear the list looks like:",clear)

#approach2
L1 = [22,12,3,4,6,5]
print("before pop", L1)

pop = L1.pop(0)
print("after pop the",pop)
print(L1)

del L1[0:]
print("after using del with the index", L1)