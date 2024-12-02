age1 = int(input("Enter the First Age: "))
age2 = int(input("Enter the Second Age: "))
age3 = int(input("Enter the Third Age: "))

if age1 > age2 and age1 > age3:
    print(f"Age: {age1} is greater than others...")
elif age2 > age1 and age2 > age3:
    print(f"Age: {age2} is greater than others...")
else:
    print(f"Age: {age3} is greater than others...")