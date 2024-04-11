print("Welcome to the tip calculator")
total_bill = input("What was the total bill?")
print(total_bill)
tip_percentage = input("How much bill would you like to give? 10, 12, or 15?")
print(tip_percentage)
number_of_people = input("How many people to split the bill?")
print(number_of_people)
bill_per_person = float(total_bill) / int(number_of_people) * (1 + float(tip_percentage) / 100)
total = "{:.2f}".format(round(bill_per_person,2 ))
print(f"Each person should pay: {total}")
