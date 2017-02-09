###################################################################################################

#Github link for Project1

# https://github.com/madr8615/CST-205

###################################################################################################


from PIL import Image # Allows to open many images and edit them
import statistics    #defines statistics


im1 = Image.open ("1(CSUMB).png") #opening the image
im2 = Image.open ("2(CSUMB).png") #opening the image
im3 = Image.open ("3(CSUMB).png") #opening the image
im4 = Image.open ("4(CSUMB).png") #opening the image
im5 = Image.open ("5(CSUMB).png") #opening the image
im6 = Image.open ("6(CSUMB).png") #opening the image
im7 = Image.open ("7(CSUMB).png") #opening the image
im8 = Image.open ("8(CSUMB).png") #opening the image
im9 = Image.open ("9(CSUMB).png") #opening the image

imageList = [im1, im2, im3, im4, im5, im6, im7, im8, im9] #adding all 9 images into the array
print("open files")

pictureWidth = im1.size[0]   #width array set x as 0
pictureHeight = im1.size[1]  #Height of the image y set as 1

print(pictureWidth) #prints the width of the image
print(pictureHeight) #prints the height of the image

redMedianPixel = 0    # set variable red median pixel equal to 0 
blueMedianPixel = 0   # set variable blue median pixel equal to 0 
greenMedianPixel = 0  # set variable green median pixel equal to 0 

redPixeList = []    # creates an empty list for the red pixel
greenPixeList = []  # creates an empty list for the green pixel
bluePixeList = []   # creates an empty list for the blue pixel

color = Image.new("RGBA", (pictureWidth, pictureHeight), "White") #


for x in range(0, pictureWidth): # the loop for x is the width of image
    for y in range (0, pictureHeight): # the loop for y is the height of image
        for image in imageList:  # loops all 9 images
            
            red, blue, green = image.getpixel((x,y))  # gets the pixels, height, and width for all 9 images
            
            redPixeList.append(red)       # adds the red pixels to the list 
            greenPixeList.append(green)   # adds the green pixels to the list
            bluePixeList.append(blue)     # adds the blue pixels to the list
            
        redMedianPixel = statistics.median(redPixeList)     # return the median of the numeric data of image
        greenMedianPixel = statistics.median(greenPixeList) # return the median of numeric data of image 
        blueMedianPixel = statistics.median(bluePixeList)   # return the median of numeric data of image 
        
        
        redPixeList = []   # temporary list red pixels, which begins to delete
        bluePixeList = []  # temporary list blue pixels, which begins to delete
        greenPixeList = [] # temporary list green pixels, which begins to delete
        
        color.putpixel((x,y),(redMedianPixel,blueMedianPixel, greenMedianPixel))  # filters out the bad colored pixels 

color.save("test2.png") # saves new image as test.png
print("Program Complete") # Informing that the program runs perfectly
