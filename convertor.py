from PIL import Image

choice = input("Type 1 if you want to convert from .jpg to .png. Type 2 otherwise: ")

# if choice is to convert from .jpg to .png
if(choice == '1'):
	print("You selected .jpg to .png conversion.")
	image_name = input("Enter the name of the .jpg image: ")
	image_name += ".jpg"
	new_image_name = input("Enter the new name of the image: ")
	new_image_name += ".png"
	image = Image.open(image_name)
	image.save(new_image_name)


# if the choice is to convert from .png to .jpg 
elif(choice == '2'):
	print("You selected .png to .jpg conversion.")
	image_name = input("Enter the name of the .png image: ")
	image_name += ".png"
	new_image_name = input("Enter the new name of the image: ")
	new_image_name += ".jpg"
	image = Image.open(image_name)
	image.save(new_image_name)

# if the choice is unknown
else:
	print("The selected choice is unavailable.")
