l1 = [31,4,355,355,"Harry"]

#List is mutable
#String is not mutable

print(type(l1))
print(l1)
l1.remove("Harry")
print(l1)
l1.sort()
l1.pop()
l1.append(49)
#l1.clear()
l1.extend([12,34,54,56])
print(l1)