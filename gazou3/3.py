import cv2

img = cv2.imread("panda.jpeg")
img_flip_lr = cv2.flip(img, 1)
cv2.imshow("panda", img)
cv2.imshow("flip_panda", img_flip_lr)
cv2.waitKey(0)
