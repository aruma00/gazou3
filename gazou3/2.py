import cv2
import argparse
import numpy as np

if __name__ == "__main__":
    img_1 = cv2.imread("a.jpeg") #画像の読み込み
    img_2 = cv2.imread("b.jpeg")

    assert img_1.shape == img_2.shape #画像サイズが違う場合はエラーを返す。

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type = str, default = "alpha_blending", help = "average, emboss")

    args = parser.parse_args()

w = img_1.shape[1]
alpha = np.linspace(0, 1, w).reshape(1, -1, 1) 
width_alpha_img = img_1 * alpha + img_2 * (1 - alpha)
cv2.imwrite("width_alpha.png", width_alpha_img)


   