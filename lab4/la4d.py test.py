course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445

print(course_name)
print(course_code)
print(str(course_number))
print(course_name + ' ' + course_code + ' ' + str(course_number))

print('Line 1\nLine 2\nLine 3\n')

print(course_name.lower())         # Returns a string in lower-case letters
print(course_name.upper())         # Returns a string in upper-case letters
print(course_name.swapcase())      # Returns a string with upper-case and lower-case letters swapped
print(course_name.title())         # Returns a string with upper-case first letter of each word, lowercase for remaining text
print(course_name.capitalize())    # Returns a string with upper-case first letter only, lowercase for remaining text

lower_name = course_name.lower()
print(lower_name)
lower_name.split(' ')

list_of_strings = lower_name.split(' ')
print(list_of_strings)
print(list_of_strings[0])

print(course_code[0])                          # Print the first character in course_code
print(course_code[2])                          # Print the third character in course_code
print(course_code[-1])                         # Print the last character in course_code
print(str(course_number)[0])                   # Turn the integer into a string, return first character in that string, and print it
print(course_code[0] + course_code[1] + course_code[2])

print(course_name[0:4])                 # Print the first four characters (values of index numbers 0,1,2, and 3)
first_word = course_name[0:4]           # Save this substring for later use
print(course_code[0:3])                 # Print the first three characters (values of index numbers 0,1,and 2)

print(course_name[12:])                        # Print the substring from index 12 to the end of the string
print(course_name[5:])                         # Print the substring from index 5 to the end of the string
print(course_name[-1])                         # Print the last character

print(course_name[-1])
print(course_name[-2])

print(course_name[-10:])                            # Return the last ten characters
print(course_name[-10:-6])                          # Try and figure out what this is returning
print(course_name[0:4] + course_name[-10:-6])       # Combine substrings together
substring = course_name[0:4] + course_name[-10:-6]  # Save the combined substring as a new string for later
print(substring)