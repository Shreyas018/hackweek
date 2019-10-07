def calc():
	sum = 0
	while True:
		print("\n1.Add\n2.Subtract\n3.Multiply\n4.GST\n5. View Bill\nEnter your choice: ")
		ch = int(input())
		if ch==1:
			sum += float(input("Enter the price of the item you want to add: "))
		elif ch==2:
			sum -= float(input("Enter the price of the item you want to subtract: "))
		elif ch==3:
			single = float(input("Enter the price of one item: "))
			fact = int(input("Enter the number of item: "))
			sum += (single*fact)
		elif ch==4:
			finalgst = float(0.18*sum) + sum
			print(f"Total amount with GST is {finalgst}\n")
		elif ch==5:
			print(f"Bill amount {sum}")
		else:
			break
#if(__name__ == '__main__'):