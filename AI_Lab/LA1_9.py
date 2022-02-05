D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# i)
D.update({6: "Six"})
print("Added new element- 6")
print(D)
# ii)
D.pop(2)
print("removed key=2")
print(D)
# iii)
if 6 in D:
    print("key=6 is present")
if not 6 in D:
    print("key is not present")
# iv)
print("Number of elements: ", len(D))
# v)
Sum = 0
for i in D:
    Sum += i

print("The sum is: " + str(Sum))

