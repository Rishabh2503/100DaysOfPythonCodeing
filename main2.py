#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people split the bill?"))
tip_as_persecnt = tip /100
total_tip_amount = bill * tip_as_persecnt
total_bill = bill + total_bill/people
final = round()

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇