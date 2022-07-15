from distutils.spawn import spawn


print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")
tip_pct = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

pct_as_float = int(tip_pct)/100
bill_with_tip = float(bill_total)*(1+pct_as_float)
# split_total = round(bill_with_tip/int(people),2)
split_total = "{:.2f}".format(bill_with_tip/int(people))

print(f"Each person should pay: ${split_total}")