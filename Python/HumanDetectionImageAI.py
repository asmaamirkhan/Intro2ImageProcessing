# @author: Asmaa ~ 2019
# HUMAN DETECTION - ImageAI library
######################

# import libraries
from imageai.Detection import ObjectDetection
import os
import cv2 as cv

# get execution path
execution_path = os.getcwd()

# create a detector
detector = ObjectDetection()

# choose model type
detector.setModelTypeAsYOLOv3()
# detector.setModelTypeAsRetinaNet()
# detector.setModelTypeAsTinyYOLOv3()

# get model path
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
#detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
#detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))

# load the model 
detector.loadModel()

# specify objects to be detected (we need PERSON only)
custom_objects = detector.CustomObjects(person=True)

# detect people and save output image
# the result is a list of objects
people = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                               input_image=os.path.join(
                                                   execution_path, "test1.jpg"),
                                               output_image_path=os.path.join(
                                                   execution_path, "YYY.jpg"),
                                               minimum_percentage_probability=30)

# print result
for obj in people:
    print(obj["name"], " : ", obj["percentage_probability"], " : ",
          obj["box_points"])
    print("--------------------------------")

print('Number of detected people: ', len(people))

# show image
"""
image=cv.imread(os.path.join(execution_path, "YY.jpg"))
cv.imshow('Result',image)
cv.waitKey(0)
"""
