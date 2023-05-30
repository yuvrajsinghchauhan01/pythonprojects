#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("WElcome to tip Calculator.")
total_bill = float(input("What is the total bill? $"))
percentage_tip = int(input("Tip kitna doge 10, 12 ya 15 " ))
split_bill = int(input("Kitne log bill share karenge? " ))
total_bill_with_tip = total_bill + (total_bill * percentage_tip/100)
final_calc = round(total_bill_with_tip/split_bill,2)
print(f"Each person should pay: {final_calc}")