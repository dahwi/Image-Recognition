from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

image = Image.open('images/numbers/0.1.png')
#spit out a correspoding array(3D) of this image above
imageArr = np.asarray(image)


#change the values so that each pixel in the picture will be either black or white
def threshold(imageArray):
	balanceArr = []
	newArr = imageArray
	
	for row in imageArray:
		for pixel in row:
			'''
			#calculate the average value of r,g,b pixel values of each pixel using reduce function
			avgNum = reduce(lambda x, y : x+y, pixel[:3])/len(pixel[:3])
			'''		
			#if you do not want to use reduce function, you have to manually 
			#calculate the average value of r,g,b. Notice that the range is from 0 to 255, so you need to adjust if the sum is greater than equal to 255	
			val = 0
			for color in pixel[:3]:
				val += color
				if(val >= 255):
					 val %= 255
					 val -= 1
			avgNum = val / 3
			balanceArr.append(avgNum)

	#calculate the average pixel value of all pixels in the imageArray
	balance = reduce(lambda x, y : x+y, balanceArr)/len(balanceArr)

	#update the imageArray in a way that if average value of r,g,b is bigger than average pixel value of the imageArray, set it to white. Black otherwise.		
	for row in newArr:
		for pixel in row:
			if reduce(lambda x, y : x+y, pixel[:3])/len(pixel[:3]) > balance:
				pixel[0] = 255
				pixel[1] = 255
 				pixel[2] = 255
				pixel[3] = 255
			else:
				pixel[0] = 0
				pixel[1] = 0
				pixel[2] = 0
				pixel[3] = 255

	return newArr


image1 = Image.open('images/numbers/0.1.png')
imageArr1 = np.asarray(image)

image2 = Image.open('images/numbers/y0.4.png')
imageArr2 = np.asarray(image2)
imageArr2.setflags(write = 1)

image3 = Image.open('images/numbers/y0.5.png')
imageArr3 = np.asarray(image3)
imageArr3.setflags(write = 1)


image4 = Image.open('images/sentdex.png')
imageArr4 = np.asarray(image4)
imageArr4.setflags(write = 1)

threshold(imageArr2)
threshold(imageArr3)
threshold(imageArr4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0),rowspan = 4, colspan = 3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan = 4, colspan = 3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan = 4, colspan = 3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan = 4, colspan = 3)

ax1.imshow(imageArr1)
ax2.imshow(imageArr2)
ax3.imshow(imageArr3)
ax4.imshow(imageArr4)

plt.show()
	
