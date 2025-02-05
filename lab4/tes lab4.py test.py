# Define the dictionary
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}

# Print values and keys
print(dict_york.values())  # Output: dict_values(['70 The Pond Rd', 'Toronto', 'M3J3M6', 'ON'])
print(dict_york.keys())  # Output: dict_keys(['Address', 'City', 'Postal Code', 'Province'])

# Access specific items
print(dict_york['Address'])  # Output: 70 The Pond Rd
print(dict_york['Postal Code'])  # Output: M3J3M6

# Modify the dictionary
dict_york['Province'] = 'BC'
dict_york['Country'] = 'Canada'
print(dict_york)
# Output: {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'BC', 'Country': 'Canada'}

print(dict_york.values())  # Output: dict_values(['70 The Pond Rd', 'Toronto', 'M3J3M6', 'BC', 'Canada'])
print(dict_york.keys())  # Output: dict_keys(['Address', 'City', 'Postal Code', 'Province', 'Country'])

# Revert the change
dict_york['Province'] = 'ON'
print(dict_york)
# Output: {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON', 'Country': 'Canada'}

print(dict_york.values())  # Output: dict_values(['70 The Pond Rd', 'Toronto', 'M3J3M6', 'ON', 'Canada'])
print(dict_york.keys())  # Output: dict_keys(['Address', 'City', 'Postal Code', 'Province', 'Country'])

# Convert keys to a list and access the first item
list_of_keys = list(dict_york.keys())
print(list_of_keys[0])  # Output: Address

# Iterate over keys and values
list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
# Output:
# Address
# City
# Postal Code
# Province
# Country

for value in dict_york.values():
    print(value)
# Output:
# 70 The Pond Rd
# Toronto
# M3J3M6
# ON
# Canada
