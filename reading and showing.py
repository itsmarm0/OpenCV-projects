import cv2


image = cv2.imread("1.jpg")
print(type(image))
print(image.shape)

cv2.imshow('frame',image)
cv2.waitKey(0)


# video = cv2.VideoCapture("111.gif")

# ret = True
# while ret:
#     ret,frame = video.read()

#     if ret:

#       cv2.imshow('frame',frame)
#       cv2.waitKey(40)
    
# video.release()
# cv2.destroyAllWindows()



# webcam = cv2.VideoCapture(0)

# while True:
#    ret,frame = webcam.read()
#    cv2.imshow('frame',frame)
#    if cv2.waitKey(40) & 0xFF == ord('z'):
#       break
    
# webcam.release()
# cv2.destroyAllWindows()
 
