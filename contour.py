import cv2
import numpy as np

image = cv2.imread("12.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0,255,0), 2)

# for cnt in contours: 
#     print(cv2.contourArea(cnt))

cv2.imshow('Original', image)        
cv2.imshow('Threshold', thresh)     
cv2.imshow('Contours', contour_image) 

cv2.waitKey(0)
cv2.destroyAllWindows()
