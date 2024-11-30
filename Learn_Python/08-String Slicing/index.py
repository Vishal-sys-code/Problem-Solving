msg = 'Welcome to Python 101: Strings'
print(msg + msg)
print(msg * 2)
print(msg, msg)

print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())

print(len(msg))
print(msg.count('Python'))
print(msg.count('python'))
print(msg.count('o'))
print(msg.count('1'))

# Slicing
print(msg[0])
print(msg[5])
print(msg[-1])
print(msg[-3])
print(msg[2:])
print(msg[2:7])
print(msg[0:8])
print(msg[0:7])
print(msg[:7])