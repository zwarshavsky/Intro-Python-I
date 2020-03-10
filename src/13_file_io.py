import random
import string

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open("./foo.txt", "r")
print(f.read())
f.close()

# # Open up a file called "bar.txt" (which doesn't exist yet) for
# # writing. Write three lines of arbitrary content to that file,
# # then close the file. Open up "bar.txt" and inspect it to make
# # sure that it contains what you expect it to contain

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

L = [randomString(100) + "\n",randomString(100) + "\n",randomString(100)]

f = open("./bar.txt", "w+")
f.writelines(L)
f.close()

f = open("./bar.txt", "r")
print(f.read())
f.close()
