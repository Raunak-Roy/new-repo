#Python program to find the sum of all items in a dictionary

dictioanry = {'a':100,
              'b':300,
              'c':800,
              'd':400}

# print(dictioanry)

# def returnsum (dictionary):
#     sum = 0
#     for i in dictioanry.values():
#         sum = sum+1
#     return sum

# returnsum(dictioanry)

def returnv(disctioanry):
    return sum(dictioanry.values())

print("sum is ", returnv(dictioanry))