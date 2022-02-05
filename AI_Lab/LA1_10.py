import LA1_10_module as comp

principal_int = int(input("Enter the principal interest: "))
interest_rate = int(input("Enter the interest rate: "))
time = int(input("Enter the time: "))

CI = comp.calc_compound_interest(principal_int, interest_rate, time)
print("The compound interest is: ", CI)
