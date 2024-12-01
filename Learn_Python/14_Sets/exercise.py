#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#Solution 1
# Membership task
print('Eric' in friends)
print('John' in friends)
print('Eric' in friends and 'John' in friends)

# Solution 2
print(friends.union(my_friends))
print(friends | my_friends)

# Solution 3
print(friends.intersection(my_friends))
print(friends & my_friends)

# Solution 4
print(friends.difference(my_friends))

# Solution 5
print(my_friends.difference(friends))

# Solution 6
car_set = set(cars)
print(car_set)