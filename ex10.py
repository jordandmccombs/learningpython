# defines tabby_cat as I'm tabbed in, the \t will tab it in
tabby_cat = "\tI'm tabbed in."
# defines persian_cat as I'm split on a line, with the \n splitting it on 2 lines, stays to the left
persian_cat = "I'm split\non a line."
# defines backslash cat as I'm a cat, with an \ before and after the a
backslash_cat = "I'm \\ a \\ cat."

# makes a list for fat_cat, each is tabbed in and on a sperate line thanks to """ and the \n
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# prints all the variables.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
