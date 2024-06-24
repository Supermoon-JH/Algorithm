array = []

array.append('a')
array.append('b')
array.extend(['c', 'd', 'e', 'f'])

print(array)    # ['a', 'b', 'c', 'd', 'e', 'f']
print(array.count('a'))     # 1
print(array.index('c'))     # 2
print(array.index('c', 2, 4))   # 2

array.insert(3, 'z')
print(array)    # ['a', 'b', 'c', 'z', 'd', 'e', 'f']

array.pop()
print(array)    # ['a', 'b', 'c', 'z', 'd', 'e']

array.remove('c')
print(array)    # ['a', 'b', 'z', 'd', 'e']

array.reverse()
print(array)    # ['e', 'd', 'z', 'b', 'a']