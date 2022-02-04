l1 = []
l2 = []

n1 = int(input("Enter the number of elements in list 1: "))
n2 = int(input("Enter the number of elements in list 2: "))

for i in range(0, n1):
    x = int(input())
    l1.append(x)

for j in range(0, n2):
    y = int(input())
    l2.append(y)

val = [value for value in l1 if value in l2]

print("The common numbers are: ", val)

