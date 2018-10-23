#prints a message to the terminal window
print("Rules that govern the state of water")

#set up a variable to hold the temperature we input
current_temp = False

while current_temp is False:
	current_temp = input("Enter a temperature:\n")
	# see what current temp is
	print("you input:", current_temp)

	# if the current temp is at freezing or below, water is a solid
	if(int(current_temp) < 0 or (int(current_temp) == 0)):
		print("water is in a solid state at or below freezing!")
		current_temp = False

	elif (int(current_temp) == 25):
		print("water is at its ambient temperature")
		current_temp = False

	# else check another condition, if it's not freezing, is below boiling?
	elif (int(current_temp) < 100):
		print("water is in a liquid state above the freezing point and below the boiling point!")
		current_temp = False

	elif (int(current_temp) > 100 or (int(current_temp) == 100 )):
		print("water is in a gas state at or above boiling point!")
		current_temp = False

# figure out how to make current_temp a number and clean the code up (DRY it out)