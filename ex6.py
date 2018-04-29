types_of_people = 10 # defines types_of_people as 10

x = f"There are {types_of_people} types of people." # defines x as a formated string that prints out the string and adds the varibable in there

binary = "binary" # defines the variable with the string

do_not = "don't" # defines the variable with the string

y = f"Those who know {binary} and those who {do_not}" # defines the variable y with a formated string with the above variables inserted

print(x) # prints out the string variable x
print(y) # prints out the string variable y

print(f"I said: {x}") # prints out the formated string, with the variable x inserted
print(f"I also said: '{y}'") # prints out the formated string with the variable y inserted

hilarious = False # sets the variable hilarious as false
joke_evaluation = "Isn't that joke so funny?! {}" # sets the variable with the string, and a open spot for another variable to be inserted later

print(joke_evaluation.format(hilarious)) # prints out the variable, formatted with the other variable inserted into it

w = "This is the left side of..." # defines variable w as a string
e= "a string with a right side." # defines variable e as a astring

print(w + e) # prints out both strings added together, possible becasue they're both strings
