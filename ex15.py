#imports the argv function from sys
from sys import argv

# assigns the variabls script and filename to your arguments
script, filename = argv

# assigns the variable txt, to open whatever you've put in for the file name
txt = open(filename)

#prints out the text and the filename
print(f"Here's your file {filename}:")
#prints out the txt variable, but reads it
print(txt.read())

# prints out the text
print("Type the filename again:")
# asks for input and assigns it to the variable
file_again = input("> ")

# creats and assigns the variable to open the input you put in for file_again
txt_again = open(file_again)

#prints out the text in the file you assigned to the variable above
print(txt_again.read())

txt.close()
txt_again.close()
