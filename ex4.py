#This is defining the variable cars as 100
cars = 100
#This is defining the variable space_in_a_car as 4.0
space_in_a_car = 4.0
#This is defining the variable drivers as 30
drivers = 30
#This is defining the variable passengers as 90
passengers = 90
#This is defining the variable cars_not_driven as cars - drivers
cars_not_driven = cars - drivers
#This is defining the variable cars_driven as equal to drivers
cars_driven = drivers
#This is defining the variable carpool_capacity as cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#This is defining the average_passengers_per_car variable as passengers divided by cars_not_driven
average_passengers_per_car = passengers / cars_driven

#This will print out the string, then the value for the car variable, followed by the rest of the string
print("There are", cars, "cars available.")
#This will print out the string, followed by the value of the drivers variable, followed by the rest of the string
print("There are only", drivers, "drivers available.")
#This willl print out the string, followed by the variable for cars_not_driven, followed by the rest of the string
print("There will be", cars_not_driven, "empty cars today.")
#This will print out the string, followed by the variable carpool_capacity, followed by the rest of the string
print("We can transport", carpool_capacity, "people today.")
#This will print out the string, followed by the variable for passengers, followeed by the rest of the string
print("We have", passengers, "to carpool today.")
#This will print out the string, followed by th evalu efor average_passengers_per_car, followed by the rest of the string
print("We need to put about", average_passengers_per_car, "in each car.")
