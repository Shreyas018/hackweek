from PIL import Image
def resize_using_resolu():
	org = Image.open(input("Enter image name with extention: "))
	#org.show()
	ox,oy = org.size
	print(f"Original x {ox}\nOriginal y {oy}")
	x= int(input("Enter x dimension for new image: "))
	y= int(input("Enter y dimension for new image: "))
	size = (x,y)
	org.thumbnail(size)
	org.save("out1.jpg")
	fin = Image.open("out1.jpg")
	fin.show()
if(__name__ == '__main__'):
	resize_using_resolu()