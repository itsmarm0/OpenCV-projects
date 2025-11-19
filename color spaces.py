import cv2

#resize
image = cv2.imread("3.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image',image)
cv2.imshow('gary_image',gray_image)
cv2.imshow('rgb_image',rgb_image)
cv2.imshow('HSV_image',HSV_image)
cv2.waitKey(0)


