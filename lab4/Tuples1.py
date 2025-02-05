# Part 1 - Tuples
t2 = (1, 2, 3, 4, 5)
t3 = t2[2:3]
print(t3)  # Output: (3,)

t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
for item in t1:
    print('item: ' + item)
# Output:
# item: Prime
# item: Ix
# item: Secundus
# item: Caladan

# Part 2 - Sets
s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

# Attempt to Access Set by Index
try:
    print(s1[0])  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'set' object is not subscriptable

# Check Existence in Set
print('Ix' in s1)  # Output: True
print('Geidi' in s1)  # Output: False

# Combine Sets
print(s2 | s3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(s2.union(s3))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of Sets
print(s2 & s3)  # Output: {4, 5}
print(s2.intersection(s3))  # Output: {4, 5}

# Difference of Sets
print(s2 - s3)  # Output: {1, 2, 3}
print(s2.difference(s3))  # Output: {1, 2, 3}

# Symmetric Difference of Sets
print(s2 ^ s3)  # Output: {1, 2, 3, 6, 7, 8}
print(s2.symmetric_difference(s3))  # Output: {1, 2, 3, 6, 7, 8}

# Convert Lists to Sets and Back
l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)
print(new_list)  # Output: [4, 5]