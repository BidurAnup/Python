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
