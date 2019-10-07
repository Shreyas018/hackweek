def convertt():
	while True:
		choice = int(input("Menu\n1. Convert Celsius to Farenheit \n2. Convert Farenheit to Celsius\nEnter your choice: "))
		if choice == 1:
			tempe = input("Enter the temperature: ")
			temp = float(tempe)
			res = (temp * 9/5) + 32
			print(f'{temp}C in Farenheit is {res}F')
		elif choice ==2:
			tempe = input("Enter the temperature: ")
			temp = float(tempe)
			res = (temp - 32) * 5/9
			print(f'{temp}F in Celsius is {res}C')
		else:
			break