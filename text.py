import cv2

image = cv2.imread("4.jpg")


text_image = cv2.putText(image, 
                         'Panda', 
                         (200, 200), 
                         cv2.FONT_ITALIC, 
                         2, 
                         (0, 255, 255), 
                         3)

cv2.imshow('text_image', text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



