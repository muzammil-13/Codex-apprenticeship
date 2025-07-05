list1=[1,2.5,"item", True]
print(list1)

# print("Length of the list1: ",len(list1))

# print(list1[1])
# print(list1[-1])

list1.append(12)

# print(list1)

list2=["wow","cool"]

list1.extend(list2)
print(list1)

print("Value removed from list1: ",list1.pop())