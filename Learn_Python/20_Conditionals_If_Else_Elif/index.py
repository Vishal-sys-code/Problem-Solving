print("Conditionals: IF Statements")
print("=======================================")

# if I can't hold my breath anymore = True
# then stop holding breath and come up

is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring an Umbrella or jacket or both")
elif is_raining and not(is_cold):
    print("Bring Umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Shirt is Fine")

print("==================================")

amount = 10
if amount <= 50:
    print("Purchase Approved")
else:
    print("Please Enter your PIN")