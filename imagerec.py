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
			avgNum = reduce(lambda x, y : x+y, pixel[:3])/len(pixel[:3])
			balanceArr.append(avgNum)

	balance = reduce(lambda x, y : x+y, balanceArr)/len(balanceArr)

		
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
	
