# @author: Asmaa ~ 2019
# Useful Scripts for Image Processing
# Image Type Converting
#####################################

# NOTE: This file is useful for converting .ppm to .jpg

# import Python Image Library
from PIL import Image

# import operating systems library
import os

# specify paths of input and output folders
# for example:
input_path = 'C:/Users/asmaa/dataset'
output_path = 'C:/Users/asmaa/train'

# initialize i counter
i = 0

# loop over all files in the specifies derectory
for filename in os.listdir(path):
	
	# open each image
	im = Image.open(os.path.join(path, filename))
    
	# save each image in the required format
	im.save(os.path.join(output_path, 'output' + str(i) + '.jpg')
	
	# increase the counter
    i = i + 1
	
	
# Output images:
# output0.jpg, output1.jpg, output2.jpg, .........