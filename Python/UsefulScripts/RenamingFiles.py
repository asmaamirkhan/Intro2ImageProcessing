# @author: Asmaa ~ 2019
# Useful Scripts for Image Processing
# Renaming All Files in a Folder
######################################

# import operating systems library
import os

# specify the path of the folder
# for example:
path = 'C:/Users/asmaa/train'

# initialize i counter
i = 0

# loop over all files in the folder
for filename in os.listdir(path):
	
	# rename files
    os.rename(os.path.join(path,filename), os.path.join(path,'image' + str(i) + '.jpg'))

	# increase the counter
    i = i + 1

	
# Output files:
# image0, image1, image2, .....