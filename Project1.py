from PIL import Image 
import statistics


im1 = Image.open ("1.png")
im2 = Image.open ("2.png")
im3 = Image.open ("3.png")
im4 = Image.open ("4.png")
im5 = Image.open ("5.png")
im6 = Image.open ("6.png")
im7 = Image.open ("7.png")
im8 = Image.open ("8.png")
im9 = Image.open ("9.png")

imageList = [im1, im2, im3, im4, im5, im6, im7, im8, im9]
print("open files")

pictureWidth = im1.size[0] 
pictureHeight = im1.size[1]

print(pictureWidth)
print(pictureHeight)

redMedianPixel = 0
blueMedianPixel = 0
greenMedianPixel = 0

redPixeList = []
bluePixeList = []
greenPixeList = []

color = Image.new("RGBA", (pictureWidth, pictureHeight), "white")


for x in range(0, pictureWidth):
    for y in range (0, pictureHeight):
        for image in imageList:
            
            red, green, blue = image.getpixel((x,y))
            
            redPixeList.append(red)
            bluePixeList.append(blue)
            greenPixeList.append(green)
            
        redMedianPixel = statistics.median(redPixeList)
        blueMedianPixel = statistics.median(bluePixeList)
        greenMedianPixel = statistics.median(greenPixeList)
        
        redPixeList = []
        bluePixeList = []
        greenPixeList = []
        
        color.putpixel((x,y),(redMedianPixel,blueMedianPixel, greenMedianPixel)) 
        
        
        
            

###################################################################################################################################
        
       


color.save("test.png")
print("Program Complete")
