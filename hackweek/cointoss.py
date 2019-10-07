import random as r
def toss():
	side = r.randint(0,2)
	if side == 0:
		print("Heads !!")
	elif side == 1:
		print("Tails !!")
	elif side == 2:
		print("Retoss !!")
#if(__name__ == '__main__'):