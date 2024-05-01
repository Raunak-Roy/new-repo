#Find Maximum of two numbers in Python
#approach>>1
a = 10
b = 29
c = (a,b)
print(max(a,b))

def maxvalue(a,b):
    if a>b:
        return a
    else:
        return b

print(maxvalue(56,85))
#approach>>2
def maxx(c):
    return max(c)
print(maxx(c))
#using list
L = [22,44,55,77,88,99]
def maximum(L):
    return max(L)

print(maximum(L))


print(a if a>b else b)