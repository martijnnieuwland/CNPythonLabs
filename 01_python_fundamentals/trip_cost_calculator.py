# Receive arguments from the user

kilometers = float(input("Please enter the number of kilometers you will drive: "))
usage = float(input("How many liters does your car use per kilometer?: "))
price = float(input("What is the price of fuel per liter?: "))

# Calculate the cost of the trip and display it to the user in the console

cost = (kilometers * usage * price)

print("Your trip will cost you:", cost)
