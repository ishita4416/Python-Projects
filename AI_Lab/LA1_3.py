plist = []
x = int(input("Enter starting of range: "))
y = int(input("Enter end of range: "))
for i in range(x, y):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            plist.append(i)

print("The prime numbers between ", x, " and ", y, " are \n", plist)
