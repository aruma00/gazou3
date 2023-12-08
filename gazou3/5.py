import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread("cat.jpeg")

# 3x3の平均化フィルタ
average_kernel_3x3 = np.ones((3, 3), np.float32) / 9
filtered_image_3x3 = cv2.filter2D(image, -1, average_kernel_3x3)

# 5x5の平均化フィルタ
average_kernel_5x5 = np.ones((5, 5), np.float32) / 25
filtered_image_5x5 = cv2.filter2D(image, -1, average_kernel_5x5)

# 3x3の加重平均化フィルタ
weighted_average_kernel_3x3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32) / 16
filtered_weighted_image_3x3 = cv2.filter2D(image, -1, weighted_average_kernel_3x3)

# 5x5の加重平均化フィルタ
weighted_average_kernel_5x5 = np.array([[1, 4, 6, 4, 1],
                                         [4, 16, 24, 16, 4],
                                         [6, 24, 36, 24, 6],
                                         [4, 16, 24, 16, 4],
                                         [1, 4, 6, 4, 1]], np.float32) / 256
filtered_weighted_image_5x5 = cv2.filter2D(image, -1, weighted_average_kernel_5x5)

# オリジナル画像とフィルタ適用後の画像を表示
cv2.imshow('Original Image', image)
cv2.imshow('3x3 Average Filter', filtered_image_3x3)
cv2.imshow('5x5 Average Filter', filtered_image_5x5)
cv2.imshow('3x3 Weighted Average Filter', filtered_weighted_image_3x3)
cv2.imshow('5x5 Weighted Average Filter', filtered_weighted_image_5x5)

cv2.waitKey(0)
cv2.destroyAllWindows()
