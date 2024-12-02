# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
four_digit_number = int(input("Enter a four digit number: "))
string_converted_number = str(four_digit_number)
reversed_number = string_converted_number[::-1]
print(f"The reverse of the four digit number is: {reversed_number}")

