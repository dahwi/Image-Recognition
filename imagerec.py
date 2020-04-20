from PIL import Image
import numpy as np

image = Image.open('images/dot.png')
#spit out a correspoding array(3D) of this image above
imageArr = np.asarray(image)

print imageArr 
