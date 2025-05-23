print("welcome to the tip calculator!")
bill=float(input("what was the total bill? $"))

tip=int(input("what is percentage tip would you like to give? 10 12 15 "))

people=int(input("How many people to split the bill"))

bill_with_tip=bill+(tip/100)*bill

bill_per_person=bill_with_tip/people
final =round(bill_per_person,2)
print(f"Each person should pay ${final}")







