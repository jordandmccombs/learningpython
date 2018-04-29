# defines formatter as 4 {}s that will allow variables or values to be inserted later
formatter = "{} {} {} {}"

# prints the formatter variable, with 1,2,3,4 in place of the {}
print(formatter.format(1,2,3,4))
# prints the formatter variable, with one two three and four in place of the {}
print(formatter.format("one","two","three","four"))
# prints the formatter variable, with the values True False False True in place of the {}
print(formatter.format(True, False, False, True))
# prints the formatter variable with the formatter variable in place of the {}
print(formatter.format(formatter,formatter,formatter,formatter))

# prints the formatter varibale with the strings listed below in place of the {}
print(formatter.format(
    "Try your"
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
