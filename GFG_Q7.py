# #Python | Count occurrences of an element in a list
#
# L = [22,33,44,44,66,44,88,44]
#
# a = 44
# def countx(L, a):
#     count = 0
#     for ele in L:
#         if ele == a:
#             count = count+1
#     return count
#
# print("{} has occured {} times".format(a,countx(L,a)))

A = [22,33,44,33,55,33]
x = 33

def checknum(A, x):
    count = 0
    for ele in A:
        if ele == 33:
            count = count+1
    return count

print('{} is occured {} times'.format(x,checknum(A,x)))