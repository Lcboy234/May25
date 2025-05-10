print("Welcome to the tip calculator!")

Total = float(input("What was the total bill? £"))

Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

People = int(input("How many people to split the bill? "))

Total_With_Tip = Total + (Total * Tip/ 100)

Final = round(Total_With_Tip/ People, 2)

print(f"Each person should pay: £{Final}")