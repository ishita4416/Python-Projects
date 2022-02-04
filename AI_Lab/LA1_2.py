import random


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start,end))
    return res


num = 100
start = 100
end = 900
List = Rand(start,end,num)

ec = 0
oc = 0
elist = []
olist = []
for num in List:
    if num%2 == 0:
        ec += 1
        elist.append(num)
    else:
        oc += 1
        olist.append(num)

plist = []
pc = 0
for i in olist:
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            pc += 1
            plist.append(i)
print("number of even numbers in the list: ", ec)
print("even numbers: ", elist, "\n")
print("number of odd numbers in the list: ", oc)
print("odd numbers: ", olist, "\n")
print("number of prime numbers in the list: ", pc)
print("prime numbers: ", plist)




