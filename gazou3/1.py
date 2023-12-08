import numpy as np
import cv2

def gammaTone(input_img, gamma):
    output_float = 255 * np.power(input_img / 255, gamma)
    return output_float.astype(np.uint8)

# 画像の読み込み
input_img = cv2.imread("cat.jpeg")

# ガンマ補正
gamma_value = 2  # ガンマ値
output_img = gammaTone(input_img, gamma_value)

# ウィンドウを作成して画像を表示
cv2.imshow("Original Image", input_img)
cv2.imshow("Gamma Corrected Image", output_img)
cv2.waitKey(0)

