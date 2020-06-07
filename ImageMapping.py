# Implementation Test of the ColorMap 
# and Recoloring of an Image
from ColorImageMap import colormap
from collections import Counter
from PIL import Image


# Extracts the color RGB value 
# and Maps using the ColorMap ADT
def colour(image):
    # Open the Image
    color = Image.open(image)
    # Return the Pixel value as a List
    colors = list(color.getdata())
    # Gets Unque Values in the list
    size = len(Counter(colors).keys())

    # Creates a ColorMap Object of unique values
    color = colormap(size)
    # Iterates over the ColorMap and add the value
    for value in colors:
        red, green, blue = value
        color.add(red, green, blue)

    return color

# Returns the Mapped RGB of image, 
# the mode and the size
def recolorImage(image, colormap):  
    im = Image.open(image)
    # Return the Pixel value as a List
    image_list = list(im.getdata())
    # Create and empty List to store new Data
    image_recolor = list()

    # Iterates over the pixel value, 
    # Map and append value to new data list
    for value in image_list:
        red, green, blue, _ = value
        colour = red, green, blue
        image_recolor.append(colormap.map(colour))  
   
    return image_recolor, im.mode, im.size
    

# TEST
# Create New Image
def main():
    color = colour("colors.jpeg")
    image_to_recolor = "Test Image.png"
    image, mode, size = recolorImage(image_to_recolor, color)
    im2 = Image.new(mode, size)
    im2.putdata(image)
    # Save Image
    im2.save("Test Result.png")

if __name__ == "__main__":
    main()

