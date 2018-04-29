# imports argv from sys
from sys import argv

# assigns the variabls script and filename to the arguments you provide
script, filename = argv

# prints out the filename you put in the argument
print(f"We're goign to erase {filename}.")
# prints out the message
print("If you don't want that, hit CTRL-C (^C).")
# prints out the message
print("If you do want that, hit RETURN.")

# asks for input with an ?
input("?")

# prints the text
print("Opening the file...")
# assigns the variable target to open the filename variable, with the write permission ('w')
target = open(filename, 'w')

# prints out the text
print("Truncating the file. Goodbye!")
# clears out anything in the target variable if there is anything
target.truncate()

# prints out text
print("Now I'm going to ask you for three lines.")

# creats 3 variables, each based off of an input that is asked for asfter the text
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writes the text stored in each variable, then does tne \n to go to theo next line and start on the left
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")


# prints text and closes file
print("And finally, we close it.")
target.close()
