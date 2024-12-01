msg = 'Welcome to Python 101: Split and Join'
msg1 = 'Welcome  to  Python  101 :  Split  and  Join '
csv = 'Eric, John, Michael, Terry, Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

print("Listing the String")
print(list(msg))

print()
print("Splits")
print(msg.split())
print(msg1.split(' '))
print(type(msg1.split(' ')))
print(csv.split(','))
print(friends_list)

print()
print("Joining Strings")
print(str(friends_list))
print('-'.join(friends_list + friends_list))
print(''.join(friends_list + friends_list))

print()
print(''.join(msg.split()))
print(msg.replace(' ', ''))