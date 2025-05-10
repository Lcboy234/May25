print("Welcome to the tip calculator!")

Total = input("What was the total bill? £")

Tip = input("How much tip would you like to give? 10, 12, or 15? ")

People = input("How many people to split the bill?")

Total_With_Tip = float(Total) + (float(Total) * int(Tip)/ 100)

Final = round(Total_With_Tip/ int(People), 2)

print(f"Each person should pay: £{Final}")