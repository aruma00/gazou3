import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread("orange.jpeg")

# グレースケール変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ガウシアンフィルタによる平滑化
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Cannyエッジ検出
edges = cv2.Canny(blurred_image, 50, 150)

# 輪郭を描画するためのコピー
contour_image = image.copy()

# 輪郭の抽出
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を描画
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# 結果の表示
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Contour Image', contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
