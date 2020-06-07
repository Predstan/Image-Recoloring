# Implementation of colorMap ADT for storing a limited set of colors 
# and for use in mapping one of the 16.7+ million colors possible in 
# the discrete RGB color space to a color in the colormap.
# Colors are sorted in the Array with the GrayScale Value
from Array import Array
import math


class colormap:
    # Creates and Instance of the Colors
    def __init__(self, k):
        self.k = k
        self.color = Array(k)

    # Returns the number of Colors in the Map
    def __len__(self):
        num = 0
        for color in self:
            if color is not None:
                num += 1
        return num

    # Determines if Color is Contained in the Map
    def __contains__(self, color):
        assert len(color) == 3, "Enter 3 digits in red, Green, Blue"
        red, green, blue = color
        gray = self.toGray(red, green, blue)

        # Determines the position of the Color
        ndx = self.findPosition(gray)[0]
        return ndx < len(self.color) and self.color[ndx].red == red \
           and self.color[ndx].green == green and self.color[ndx].blue == blue

    # Adds a Color (RGB) to the Map
    def add(self, red, green, blue):
        gray = self.toGray(red, green, blue)
        ndx, true = self.findPosition(gray)
        assert len(self) < self.k, 'Color Map is Full'
        color = RGBColor(red, green, blue)
        if true == None:
            self.color.insert(ndx, color)

    # Remove a Color from the Map if in Map
    def remove(self, red, green, blue):
        assert (red, green, blue) in self, "Color not in Color Map"
        gray = self.toGray(red, green, blue)
        ndx = self.findPosition(gray)[0]

        # Uses a pop Method in the Array
        self.color.pop(ndx)
    
    # Maps a color to the nearest color in the Map and returns the Color
    def map(self, color):
        red, green, blue = color
        gray = self.toGray(red, green, blue)
        ndx, true = self.findPosition(gray)

        # Is color in the Map
        if true == True:
            return red, green, blue
        
        # If color not in Map
        else:
            if ndx-1 >= 0 and ndx < len(self.color):
                low = self.color[ndx-1] # color less than color but nearest
                high = self.color[ndx] #color larger than color but nearest
            
            elif ndx >= len(self.color):
                low = self.color[ndx-1]
                low_red, low_green, low_blue = (low.red, low.green, low.blue)
                # Return the largest Color in the List
                return low.red, low.green, low.blue

            else:
                high = self.color[ndx]
                high_red, high_green, high_blue = (high.red, high.green, high.blue)
                # Return the largest Color in the List
                return high.red, high.green, high.blue

            # Is this color larger than all the color in the map
            if high == None:
                low = self.color[ndx-1]
                return low.red, low.green, low.blue
                        
            # If Color is between two colors
            else:
                low = self.color[ndx-1] # color less than color but nearest
                high = self.color[ndx] #color larger than color but nearest
                # color less than color but nearest
                low_red, low_green, low_blue = (low.red, low.green, low.blue) 
                #color larger than color but nearest
                high_red, high_green, high_blue = (high.red, high.green, high.blue)
            # Determines distance between low color
            distanceLow = math.sqrt(((low_red - red)**2)\
                +((low_green - green)**2) + ((low_blue - blue)**2))
            # Determines distance between higher color
            distancehigh = math.sqrt(((high_red - red)**2)\
                +((high_green - green)**2) + ((high_blue - blue)**2))

            # Returns the Color with the minimum distance
            if distanceLow < distancehigh:
                return low.red, low.green, low.blue
            else:
                return high.red, high.green, high.blue
    
    # Returns the Gray value of the Color
    def toGray(self, red, green, blue):
        gray = 0.299 *  red + 0.587 * green + 0.114 * blue
        return gray

    # Iterates over the color
    def __iter__(self):
        return self.color.__iter__()

    # Returns the Postion of a color
    # Returns True if color is found, Returns None if not Found
    def findPosition(self, color):
        low = 0
        high = len(self.color) - 1

        # Continues to Divide the Array Until Color is Found
        while low <= high:
            mid = (high + low) // 2
            # Value in the Middle of the Array
            value = self.color[mid]
            # If there value is a color
            if value != None:
                value = self.toGray(self.color[mid].red, \
                    self.color[mid].green, self.color[mid].blue)
            # Determines If the Color is found, Returns the position
            if value == color or (mid == 0 and value == color):
                return mid, True
            # If Color is less, Go to backward of Array
            elif value == None or (value > color):
                high = mid - 1
            # If Color is less, Go forward of Array
            elif value != None and value < color:
                low = mid + 1
        # Determines if not found, Returns the position where Color is supose to be 
        return low, None

# Storage Class for Color Intensity
class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


