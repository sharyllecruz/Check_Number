while True:
	check_number = input("Put a number")
	check_number = int(check_number)
	abs_number = abs (check_number)
	if abs_number %2 == 0:
		print(str(check_number) + " is a Even number.")
	else:
		print(str(check_number) + " is a odd number.")