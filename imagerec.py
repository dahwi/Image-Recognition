from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

image = Image.open('images/numbers/0.1.png')
#spit out a correspoding array(3D) of this image above
imageArr = np.asarray(image)


#create a file called numArEx.txt which contains the number and examples that match that specific number
def createExamples():
	numberArrayExamples = open('numArEx.txt','a')
	number = range(0,10)
	version = range(1,10)
	
	for num in number:
		for v in version:
			imgFileName = 'images/numbers/'+str(num)+'.'+str(v)+'.png'
			ei = Image.open(imgFileName)
			eiarr = np.array(ei)
			eiar1 = str(eiarr.tolist())

			lineToWrite = str(num) + '::'+eiar1+'\n'
			numberArrayExamples.write(lineToWrite)
			
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

def whatNumIsThis(filepath):
	matchedArr = []
	loadExamps = open('numArEx.txt', 'r').read()
	loadExamps = loadExamps.split('\n')
	
	i = Image.open(filepath)
	iArr = np.array(i)
	iArrL = iArr.tolist()

	inQuestion = str(iArrL)

	for eachExample in loadExamps:
		if len(eachExample) > 3:
			splitEx = eachExample.split('::')
			currentNum = splitEx[0]
			currentArr = splitEx[1]
			
			eachPixEx = currentArr.split('],')
			
			eachPixInQ = inQuestion.split('],')
			
			x = 0 
				
			while x < len(eachPixEx):
				if eachPixEx[x] == eachPixInQ[x]:
					matchedArr.append(int(currentNum))

				x += 1

	c = Counter(matchedArr)	
	print c
		

whatNumIsThis('images/test.png')

