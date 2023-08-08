#Program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


two_digit_number = input("Type a two digit number: ")

#Solution 1
a = int(two_digit_number[0])
b = int(two_digit_number[1])
c = a+b
print(c)

#Solution 2
a = two_digit_number[0]
b = two_digit_number[1]
c = int(a) + int(b)
print(c)

#Solution 3
c = int(two_digit_number[0]) + int(two_digit_number[1])
print(c)


#Notes
#subscripting and type conversion
#'int'data type is not subscriptable
#print(type(VARIABLE NAME)) - to check the variable's data type
