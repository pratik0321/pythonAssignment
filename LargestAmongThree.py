n1 = 2
n2 = 4
n3 = 1

if (n1>=n2) and (n2>=n3):
    largest = n1
elif (n2>=n1) and (n2>=n3):
    largest = n2
else:
    largest = n3

print("the largest number is = ", largest)