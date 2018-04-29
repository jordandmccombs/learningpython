# defines cheese_and_crackers as a function needing 2 varibales. it then takes
# the variables and prints out strings with them. At the end it drops down to a new line
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(">>>>>> cheese_count=", cheese_count, "boxes_of_crackers=", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    print("<<<<<< exit cheese_and_crackers")


# shows that you can give the function arguments directly
print("We can just give the function numbiers directly:")
cheese_and_crackers(20, 30)

#shows taht you can assign the variables from the function values, and still have the function work
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# shows that we can call the function, and do math to provide the argumetns
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 +  6)

# shows that you can use the arguments and the values they have, and still do math ontop of that
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("And we can ask the user for the input")
user_cheese = int(input("How many slices of cheese do you have? "))
user_crackers = int(input("How many boxes of crackers? "))
cheese_and_crackers(user_cheese, user_crackers)
