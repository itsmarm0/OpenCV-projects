import cv2 
import numpy as np


image = cv2.imread("4.jpg")
rotate_image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
# rotate_image = cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('rotate_image', rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




# image = cv2.imread('5.jpg')
# srcTri = np.array([[0, 0],
#                    [image.shape[1]-1, 0],
#                    [0, image.shape[0]-1]], dtype=np.float32)

# dstTri = np.array([[0, image.shape[1]*0.33],
#                    [image.shape[1]*0.85, image.shape[0]*0.25],
#                    [image.shape[1]*0.15, image.shape[0]*0.7]], dtype=np.float32)

# warp_mat = cv2.getAffineTransform(srcTri, dstTri)
# warp_dst = cv2.warpAffine(image, warp_mat, (image.shape[1], image.shape[0]))

# center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
# angle = -50
# scale = 0.6

# rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
# warp_rotate_dst = cv2.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

# cv2.imshow("Original", image)
# cv2.imshow("Warp", warp_dst)
# cv2.imshow("Warp + Rotate", warp_rotate_dst)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
