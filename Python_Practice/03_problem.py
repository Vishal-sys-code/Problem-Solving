num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("------------ Before Swapping ------------")
print(f"Numbers are => a: {num1} and b: {num2}")

num1, num2 = num2, num1

print("------------ After Swapping (Approach: #1) ------------")
print(f"Numbers are => a: {num1} and b: {num2}")

# Here, num1: 2 and num1: 1

# temp -> num1, num1 -> num2, num2 -> temp
temp = num1
num1 = num2
num2 = temp
print("------------ After Swapping (Approach: #2) ------------")
print(f"Numbers are => a: {num1} and b: {num2}") # this will reverse the above number num1 : 2 and num2: 1

# Inputs taken: num1 = 1 and num2 = 2