# 3 using single apostrophe inside double quotes
string1 = "Now I'm ready to use the single quotes inside a string!"

print(string1)

print("USe \n to print a new line'")


# String indexing
s = "Hello World!"
print(s[0])
print(s[:])
print(s[1:])
print(s[:9])
print(s[:100] + "did it work")  # no out of bound error in python
print(s[:])
print(s[-1])  # prints last alphabet

print(s[:-1])  # print everything but the last letter

print(s[::1])  # grab everything at a step size of 1
print(s[::2])  # Everything in a step size of 2
print(s[::-1])  # print string reverse/backwards


# String PROPERTIES
# STRINGS ARE IMMUTABLE

################
#   s[0] = 'x'
##################

# String concatenation and reassiging to a new variable is possible

print(s+'concatenated strings')
s = s+'further concatenation and assigning to same variable is possible so if need to change anything in a string it is better to re assign BUT STILL CANT CHANGE WHAT WAS ON S'

print(s)

# BUILT IN STRING METHODS
print(s.upper())
print(s.lower())
print(s.split())  # GIVES LIST OF SLPITTED WORDS
# splititng by an element, but doesnt take the split location element with it
print('\n\n\n')
print(s.split('e'))


# STRING FORMATTING
print('pring another string with curly brackets: {}'.format('the inserted string'))
