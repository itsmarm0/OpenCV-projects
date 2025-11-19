import cv2

image = cv2.imread("4.jpg")
rec_image = cv2.rectangle(image, (100,100), (400,400), (0,255,255), 20)

cv2.imshow('rec_image',rec_image)
cv2.waitKey(0)


