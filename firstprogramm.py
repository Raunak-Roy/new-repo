mydict = {'name': 'raunak', 'age': 29, 'home': 'delhi', 'work': 'datra analys'}
# print(mydict)
# print(mydict.keys())
# print(mydict.values())

#question1

mysorted_keys = list(mydict.keys())

mysorted_keys.sort()
sorted_dict = {i: mydict[i] for i in mysorted_keys}
print(sorted_dict)