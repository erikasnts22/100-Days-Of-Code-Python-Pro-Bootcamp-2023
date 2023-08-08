height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#Solution 1
height = float(height)
weight = int(weight)
bmi = weight / (height ** 2)
print(int(bmi))

#Solution 2
bmi = int(weight) / float(height) ** 2
print(int(bmi))

#Solution 3
bmi = int(weight) / (float(height) * float(height))
print(int(bmi))
