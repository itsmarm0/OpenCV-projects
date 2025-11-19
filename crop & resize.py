import cv2

#resize
image = cv2.imread("2.jpg")
resized_image = cv2.resize(image,(200,400))

cv2.imshow('image',image)
cv2.imshow('resized_image',resized_image)
cv2.waitKey(0)

print(image.shape)
print(resized_image.shape)

#crop
image = cv2.imread("3.jpg")
cropped_image = image[200:200 , 400:400]

cv2.imshow('image',cropped_image)
cv2.waitKey(0)