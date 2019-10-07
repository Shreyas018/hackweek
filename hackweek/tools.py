import imgresizer as ir
#import chess as chessb
import cointoss as ct
import tempconv as tc
import teamchooser as tgen
import gstcalc as gc
import diceroll as dr
while True:
	choice = int(input("\nMenu\n1. Image Resizer\n2. Coin Toss\n3. Temperature Converter\n4. Team Generator\n5. GST Calculator\n6. Dice Roll\nEnter your choice: "))
	if(choice == 1):
		ir.resize_using_resolu()
	elif(choice == 2):
		input("Toss a coin")
		ct.toss()
	elif(choice == 3):
		tc.convertt()
	elif(choice == 4):
		tgen.teamgen()
	elif (choice == 5):
		gc.calc()
	elif (choice == 6):
		dr.roll()
	else:
		break
