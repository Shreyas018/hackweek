import random as r
def roll():
	input("Roll Dice")
	dice1 = r.randint(1,6)
	dice2 = r.randint(1,6)
	def bordered(text):
	    lines = text.splitlines()
	    width = max(len(s) for s in lines)
	    res = ['┌' + '─' * width + '┐']
	    for s in lines:
	        res.append('│' + (s + ' ' * width)[:width] + '│')
	    res.append('└' + '─' * width + '┘')
	    return '\n'.join(res)
	print(bordered(str(dice1)))
	print(bordered(str(dice2)))