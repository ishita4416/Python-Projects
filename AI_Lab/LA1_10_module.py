
def calc_compound_interest(pr, ir, t):
    x = pr * (pow((1 + ir / 100), t))
    compound_int = x - pr
    return compound_int


# principal_int = int(input("Enter the principal interest: "))
# interest_rate = int(input("Enter the interest rate: "))
# time = int(input("Enter the time: "))
#
# CI = calc_compound_interest(principal_int, interest_rate, time)
# print("The compound interest is: ", CI)
