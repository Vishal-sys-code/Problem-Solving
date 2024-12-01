friends = ['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']
friends_tuple = ('Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian')
friends_set = {'Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}

# Set is blazingly fast unordered lists
# Set is faster to search
# It doesnot have duplicacy
print(friends_set)
print(my_friends_set)
print(friends_set.intersection(my_friends_set))
print(friends_set.difference(my_friends_set))
print(friends_set.union(my_friends_set))


# =================================================================
# Empty Lists
empty_lists = []
empty_lists = list()

# Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This is wrong this is the dictionary
empty_set = set()

# =================================================================