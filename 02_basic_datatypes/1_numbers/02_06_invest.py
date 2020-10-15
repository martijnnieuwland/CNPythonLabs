'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = float(input("What amount would you like to invest?: "))
interest = float(input("What percentage is the interest rate?: "))/100
years = float(input("How many years are you going to invest?: "))
income = amount * interest * years

print("You will increase your investment with: ", income)
