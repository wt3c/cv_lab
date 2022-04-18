import cv2

image = cv2.imread('./Photos-001/20210122_160524.jpg')
cv2.imwrite('my_pic.jpg', image)

cv2.namedWindow('Display Window')
cv2.imshow('Display Window', image)
print("size of image: ", image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

