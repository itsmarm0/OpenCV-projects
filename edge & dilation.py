import cv2
import numpy as np

image = cv2.imread("9.jpg")
edge_canny = cv2.Canny(image,200,100)

cv2.imshow('edge_canny', edge_canny)
cv2.imshow('image',image)



#extra

dilation = cv2.dilate(edge_canny,np.ones((3,3),dtype=np.int8))
cv2.imshow('dilation',dilation)

eroding = cv2.dilate(dilation,np.ones((3,3),dtype=np.int8))
cv2.imshow('eroding',eroding)

cv2.waitKey(0)
cv2.destroyAllWindows()
