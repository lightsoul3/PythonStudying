#not right
first = [1, 2, 3, 4, 5]
print(first)
second = first
print(second)

second.append(6)
print(second)
print(first)

#right
third = second.copy()
print(second)
print(third)

third.append(7)
print(second)
print(third)
