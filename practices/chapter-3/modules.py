# __builtins__ module hosts common objects that are always accessible.

# to show the list of objects in __builtins__ module, run the dir command:
print("dir command for __builtins__ module:", dir(__builtins__))

anObject = 1
print("dir command for an integer:", dir(anObject))

# to get the documentation of an object, run the help command:
print("help command for an integer:", help(anObject))

# to get the type of object, use type function:
print("type of anObject:", type(anObject))

# to get information a module, first import it
import math
print("dir command for math module:", dir(math))

# Package installation
# $ pip install package_name
# Package update
# $ pip install --upgrade package_name
# Package removal
# $ pip uninstall package_name
# Package listing
# $ pip list
# Packet search
# $ pip show package_name

# List outdated existing packages:
# $ pip list --outdated --format=columns

# pip is updated just like any other library. To update pip:
# $ pip install --upgrade pip
