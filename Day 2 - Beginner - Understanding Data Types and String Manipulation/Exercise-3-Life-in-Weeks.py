#Program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#OR

#message = f"You have {days} days, {weeks} weeks, and {months} months left."
#print(message)