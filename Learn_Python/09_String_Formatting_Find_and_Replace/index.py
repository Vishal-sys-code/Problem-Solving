msg = "Welcome to Python 101: Strings"
msg_triple_quotes = """Dear Tyler,,
You must cut down the mightiest
tree in the forest with...
a herring! <3"""
print(msg)
print(msg_triple_quotes)

print(msg.find('h'))
print(msg.find('Python'))

print(msg.replace('Python', 'Java'))
print(msg.replace('Java', 'Ruby'))

# Strings are immutable, so that mean that you can't change them when you have created them.
msg1 = msg.replace('Python', 'Ruby')
print(msg1)

print('Python' in msg)
print('Ruby' in msg1)
print('Python' in msg1)


# String Formatting
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f"[{name.title()}] loves the color {color.lower()}!"
msg2 = f"[{name.capitalize()}] loves the color {color.lower()}!"
print(msg)
print(msg1)
print(msg2)