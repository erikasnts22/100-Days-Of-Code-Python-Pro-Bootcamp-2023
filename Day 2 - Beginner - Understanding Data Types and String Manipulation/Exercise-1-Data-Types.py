#Program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


two_digit_number = input("Type a two digit number: ")

#Solution 1
a = int(two_digit_number[0])
b = int(two_digit_number[1])
two_digit_number = a+b
print(two_digit_number)

#Solution 2
a = two_digit_number[0]
b = two_digit_number[1]
two_digit_number = int(a) + int(b)
print(two_digit_number)

#Solution 3
two_digit_number = int(two_digit_number[0]) + int(two_digit_number[1])
print(two_digit_number)


#Notes
#subscripting and type conversion
#'int'data type is not subscriptable
#print(type(VARIABLE NAME)) - to check the variable's data type
