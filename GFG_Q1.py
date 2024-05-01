#Python program to interchange first and last elements in a list

#1st approach

list1 = [22,44,66,77]
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)

#2nd approach
list2 = [33,55,66,77]

def swapp(list2):
    list2[0], list2[-1] = list2[-1], list2[0]
    return swapp

print(swapp(list2))

#3rd approach
a= 5
b =6

k = a
a = b
b = k
print("old value of a is 5 and now:", a, "old value of b is: 6 and now:",b)