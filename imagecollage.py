from PIL import Image
import random

#sets the canvas
background = Image.open("blackscreen.jpg")

#retrieves the images
def opening(picture_name):
    return Image.open(picture_name)

#example
#image1 = Image.open("porsche1.jpg")

#resizes the images to be equal
def resize(file):
    return file.resize((400,400))

#area you want to place the image
#area = (x,y,x,y)
#area1 = (0,0)
#area2 = (0,400)
#area3 = (400,0)
#area4 = (400,400)

#randomises the layout
list = [(0,0), (0,400), (400,0), (400,400)]
new_list = random.sample(list,4)

#places the images on top of canvas
def paste(fileName, size):
   return background.paste(resize(opening(fileName)), size)

paste("porsche1.jpg", new_list[0])
paste("mclarenP1.jpg", new_list[1])
paste("astonV1.jpg", new_list[2])
paste("porsche2.jpg", new_list[3])

#loads up the picture
background.show()