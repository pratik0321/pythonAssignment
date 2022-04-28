a = 2
b = 2
add = a + b
print(add)

c = 1.3
d = 3.4

name = "sam"

is_valid_user = False #snakecase

isValidUser = "good"#camelcase

#variables name cannot have white spaces
#can't use special characters
#good to have lowercases
#avoid using built keyword --> list, int, float
#case sensitive
#use snakecasing to define variable names

#to cal tax
income = 10000
tax_percentage = 0.2
tax = income * tax_percentage
print(tax)

#strings - ordered sequence of characters

name = "BOB"
first_name = 'bob'

#indexing and slicing
print(name[0])
print(name[1])
print(name[2])
#indexing 0 1 2.....0 -2 -1

#slicing
str_alphabets = "abcdefg"
print(str_alphabets[0:3])
print(str_alphabets[:3])
print(str_alphabets[2:])
print(str_alphabets[0:7:2])
#string[start:stop:step]

#string is immutable
name = "tim"
#name[1] = "0"#this is not possible
name1 = name[0] + "o" + name[-1]
print (name1)

