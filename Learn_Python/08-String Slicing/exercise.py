"""
From the string "Welcome to Python 101: Strings", extract text and create print a new string says:
    * "1 Welcome Ring To Tyler"
    * Every first letter in a word should be capitalized (title format)
Print the same string backwards [Hint: Google is your friend...]
"""
msg = "Welcome to Python 101: Strings"
lengthOfString = len(msg)

word1 = msg[-10]
word2 = msg[0:7]
word3 = msg[25 : lengthOfString - 1]
word4 = msg[8:10]
word5 = msg[-18:-16] #ty
word6 = msg[-29:-27] #le
word7 = msg[-5] #r
word_name = word5[::-1]+word6[::-1]+word7
string = (word1 + " " +  word2 + " " + word3 + " " + word4 + " " + word_name)
print(string.title())
# Print the string in the reverse order
print(string[::-1])