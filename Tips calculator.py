print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tips_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person=int(input("How many people to split the bill? "))
perhead=(bill*(100+tips_percentage)/100)/person
print(f"Each person should pay: ${round(perhead,2)}")