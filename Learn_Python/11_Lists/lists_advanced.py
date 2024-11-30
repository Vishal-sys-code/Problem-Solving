friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911, 130, 328, 535, 740, 308]
print(friends)
print(cars)

# Sort a list
friends.sort()
print(friends)
friends.sort(reverse=True) # Reverse the sort
print(friends)
friends.reverse() # Reversing the list
print(friends)

cars.sort()
print(cars)
cars.sort(reverse=True) # Reverse the sort
print(cars)
cars.reverse() # Reversing the list
print(cars)

# ------------------------------------------------------
# Minimum and Maximum
print(min(cars))
print(max(cars))
print(sum(cars))
print(min(friends))
print(max(friends))

# Adding or change something to the list
friends.append('Vayishu')
print(friends)
friends.insert(1, 'Ruzina')
print(friends)
friends[3] = 'Zayn'
print(friends)

# Extends the list
friends.extend(cars)
print(friends)

# Remove and deletion
friends.remove('Zayn')
print(friends)
friends.pop() # Remove last one
print(friends)
friends.pop(2)
print(friends)
friends.pop(-1)
print(friends)

# friends.clear() # It empty the list 
# print(friends)
# del friends # Use carefully
# print(friends)

# Copy the Lists
new_friends = friends[:] # copy of the list
print(new_friends)
new_friends = friends.copy()
print(new_friends)
new_friends = list(friends)
print(new_friends)