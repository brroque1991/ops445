t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

# Accessing elements and slices from tuples
print(t1[0])  # Output: Prime
print(t2[2:4])  # Output: (3, 4)

# Membership testing in the tuple
print('Ix' in t1)  # Output: True
print('Geidi' in t1)  # Output: False

# Working with a list
list2 = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
list2[0] = 'ica100'
print(list2[0])  # Output: ica100
print(list2)  # Output: ['ica100', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# If you want to modify the contents of 't2', convert it to a list first:
t2 = list(t2)  # Tuples are immutable, so we convert it to a list
t2[1] = 10  # Modify the second element
print(t2)  # Output: [1, 10, 3, 4, 5, 6]

