"""
Take two inputs from user
Take the name and the distance in km
Print: 
Greet user by naame and show km and miles values

1 mile is 1.609 kms
Hint: Use correct types for calculating and print
Note: Did you capitalize the name.
"""

name = input("Enter you name?: ")
distance_km = float(input("Enter your distance: "))
distance_miles = (distance_km/1.609)
print(f"Hello {name.capitalize()}, You walked: {distance_km} kms it is almost {round(distance_miles)} miles.")