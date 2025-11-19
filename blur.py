import cv2

image = cv2.imread("3.jpg")
# image = cv2.imread("2n.jpg")

k_size = 21
# k_size = 5
image_blur = cv2.blur(image,(k_size,k_size))
image_gaussian = cv2.GaussianBlur(image,(k_size,k_size),5)
median_blur = cv2.medianBlur(image,k_size)

cv2.imshow('image',image)
cv2.imshow('image_blur',image_blur)
cv2.imshow('image_gaussian',image_gaussian)
cv2.imshow('median_blur',median_blur)
cv2.waitKey(0)


