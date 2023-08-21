import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Get the total number of items in list
random_names = random.randint(0, len(names))
# print(len(names))
# print(random_names)

if random_names ==  0:
    random_names += 1

choice = random_names - 1
# print(choice)
# print(names[choice])

print(f"{names[choice]} is going to buy the meal today!")

# Better Solution
item_list = len(names)
random_choice = random.randit(0, item_list - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to bu the meal today!")

# NOTES
# program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.