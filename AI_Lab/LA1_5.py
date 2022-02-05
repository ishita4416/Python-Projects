
start = int(input("Enter starting year"))
end = int(input("Enter ending year"))

print("The leap years in between ", start, " and ", end, " are:\n")
for year in range(start, end):
    if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year)
