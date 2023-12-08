import cv2
import numpy as np

# 画像の読み込み
image_path = 'panda.jpeg'  # 画像のパスを適切なものに変更してください
image = cv2.imread(image_path)

# 画像が読み込まれたか確認
if image is None:
    print(f'Error: Unable to load image from {image_path}')
    exit()

# 画像の高さと幅を取得
height, width = image.shape[:2]

# 3x3のモザイクタイルに画像を分割
tiles = [image[i:i + height // 3, j:j + width // 3] for i in range(0, height, height // 3) for j in range(0, width, width // 3)]

# タイル番号を表示するためのリスト
tile_numbers = []

# 分割線を描画
for i in range(1, 3):
    # 横の分割線
    cv2.line(image, (0, i * height // 3), (width, i * height // 3), (0, 255, 0), 2)
    # 縦の分割線
    cv2.line(image, (i * width // 3, 0), (i * width // 3, height), (0, 255, 0), 2)

# タイル番号を左上に描画し、番号をリストに保存
for i in range(3):
    for j in range(3):
        x, y = j * width // 3, i * height // 3
        cv2.putText(image, f'{i * 3 + j + 1}', (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        tile_numbers.append(f'Tile {i * 3 + j + 1}: (x={x}, y={y})')

# モザイクタイルを表示
mosaic_image = np.vstack([np.hstack(row) for row in np.array_split(tiles, 3)])
cv2.imshow('Mosaic Image with Tile Numbers', mosaic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# タイル番号のリストを表示
print("Tile Numbers:")
for tile_number in tile_numbers:
    print(tile_number)