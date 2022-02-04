
x = int(input("Input the value of x: "))
n = int(input("Input the number of terms: "))
Sum = 1
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact = fact*j
    term = x**i/fact
    Sum = Sum + term
print("The sum is ", Sum)
