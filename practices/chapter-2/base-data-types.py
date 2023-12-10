# to concatination different data types we need to use str() type casting
print("letter:" + str(5))

# we can access a character in a string
data = "asdfg"
print("index 3:", data[3])

# we can define a string data in more than one row
data = """first row
second row
third row
"""  # additional empty row
print("data:", data)

# To print raw string data to the console, the r prefix must be used when assigning variables:

data = r"this a paragraph for a long text\n and this is its second row"
print("data:", data)

# we can not assign a new value to a character in a string
# data[0] = "A"  # TypeError: 'str' object does not support item assignment

# print function has some parameters
# sep: seperator between arguments
# end: end of the print function
# file: file to write the output
# flush: flush the output buffer

print("first", "second", "third", sep=" ", end="\n", file=None, flush=False)

# string methods
# .lower(): reduces the letters to lowercase
print("lowercase:", "HELLO WORLD".lower())

# .upper(): converts the letters to uppercase
print("uppercase:", "hello world".upper())

# .strip(): removes the spaces at the beginning and end of the string
print("strip:", "   hello world   ".strip())

# .startswith(): checks if the string starts with the given string
print("startswith:", "hello world".startswith("hello"))

# .endswith(): checks if the string ends with the given string
print("endswith:", "hello world".endswith("world"))

# .find(): returns the index of the given string
print("find:", "hello world".find("world"))  # returns -1 if the searched String is not found.

# .replace(): replaces the given string with the given string
print("replace:", "hello world".replace("world", "python"))

# .split(): splits the string with the given string and returns a list
print("split:", "hello world".split(" "))

# .join(): joins the given list with the given string
print("join:", " ".join(["hello", "world"]))

# .isspace(): checks if the string contains only spaces
print("isspace:", "   ".isspace())

# .format(): formats the string with the given arguments
print("format:", "hello {} {}".format("world", "python"))
print("format:", "hello {1} {0}".format("world", "python"))
print("format:", "hello {name} {surname}".format(name="world", surname="python"))

# string slices (substring) [start:end:step]
# start: start index of the substring
# end: end index of the substring (not included)
# step: step size of the substring (default: 1)
data = "hello world"
print("slice:", data[0:5])  # hello

# if the start index is not given, it starts from the beginning
print("slice:", data[:5])  # hello

# if the end index is not given, it goes to the end
print("slice:", data[6:])  # world

# step size can be given
print("slice:", data[::2])  # hlowrd

# % operator
# %s: string
# %d: integer
# %f: float
print("format:", "hello %s" % "world")
print("format:", "hello %s" % 5)
print("format:", "hello %d" % 5)
print("format:", "hello %s %d" % ("world", 2023))

# f-string (formatted string literals) (python 3.6+) (recommended, this is the fastest way)
# f: format
# {}: placeholder
name = "world"
year = 2023
print(f"hello {name} {year}")

# When performing arithmetic operations on variables of different types,
# Python converts all variables to the most inclusive type.
# int < float < complex
# int + float = float
print("int + float:", 5 + 5.5, type(5 + 5.5))
# int + complex = complex
print("int + complex:", 5 + 5j, type(5 + 5j))
# float + complex = complex
print("float + complex:", 5.5 + 5j, type(5.5 + 5j))
# int + bool = int
print("int + bool:", 5 + True, type(5 + True))
# float + bool = float
print("float + bool:", 5.5 + True, type(5.5 + True))
# complex + bool = complex
print("complex + bool:", 5j + True, type(5j + True))
# bool + bool = int
print("bool + bool:", True + True, type(True + True))

# operator // returns the integer part of the division
print("integer division:", 5 // 2)

# round function rounds the given number
print("round:", round(5.5))
print("round:", round(3.1415))
print("round:", round(3.1415, 2))  # second parameter is the number of digits after the decimal point

# Assign the String '6,15,22,35,19' to a variable. How do you parse the numbers in the variable?
data = "6,15,22,35,19"
numbers = data.split(",")
print("numbers:", numbers)

# Code the Python program that edits the e-mail address of the student named Ali Veli as aliveli@ogr.duzce.edu.tr
# and prints it to the console.
name = "Ali Veli"
email = name.replace(" ", "").lower() + "@ogr.duzce.edu.tr"
print("email:", email)

# alternative solution
name = "Ali Veli"
email = f"{name.replace(' ', '').lower()}@ogr.duzce.edu.tr"
print("email:", email)

# In Python, for numeric values, 0 is False and all other values are True
print("bool:", bool(0))
print("bool:", bool(1))

# In Python, for string values, empty string is False and all other values are True
print("bool:", bool(""))
