import cv2
import numpy as np

def variable_sharpening_filter(image, alpha):
    # Sobelフィルタによる勾配の計算
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # 勾配の絶対値と方向
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)
    
    # 可変鮮鋭化フィルタ
    sharpened_image = image + alpha * gradient_magnitude * np.cos(gradient_direction)
    
    # 画像の範囲を[0, 255]にクリップ
    sharpened_image = np.clip(sharpened_image, 0, 255)
    
    # 整数型に変換
    sharpened_image = np.uint8(sharpened_image)
    
    return sharpened_image

# 画像の読み込み
image = cv2.imread("cat.jpeg", cv2.IMREAD_GRAYSCALE)

# alphaの値を変化させながら処理を行い、結果を複数のウィンドウに表示
for alpha_value in [0.5, 1.0, 1.5, 2.0]:
    result_image = variable_sharpening_filter(image, alpha_value)
    
    # ウィンドウに表示
    window_name = f'Result with alpha={alpha_value}'
    cv2.imshow(window_name, result_image)

# オリジナル画像を表示
cv2.imshow('Original Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
