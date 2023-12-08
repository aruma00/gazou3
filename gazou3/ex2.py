import cv2
import numpy as np
import time

# 画像の読み込み
image_path = "panda.jpeg"  # 画像のパス
image = cv2.imread(image_path)

# 画像の高さと幅を取得
height, width = image.shape[:2]

# 3x3のモザイクタイルに画像を分割
tiles = [image[i:i + height // 3, j:j + width // 3] for i in range(0, height, height // 3) for j in range(0, width, width // 3)]

# タイル番号を左上に描画し、番号をリストに保存
tile_numbers = []
for i in range(3):
    for j in range(3):
        x, y = j * width // 3, i * height // 3
        cv2.putText(image, f'{i * 3 + j + 1}', (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        tile_numbers.append(f'Tile {i * 3 + j + 1}: (x={x}, y={y})')
        
# 反転前のモザイクタイルを表示
mosaic_image = np.vstack([np.hstack(row) for row in np.array_split(tiles, 3)])
cv2.imshow('Mosaic Image with Tile Numbers', mosaic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# タイルを1枚ずつ5秒ごとに順番に左右反転させて表示
for i, tile in enumerate(tiles, start=1):
    # 左右反転
    flipped_tile = cv2.flip(tile, 1)
    
    # タイル番号を表示
    print(f"Showing flipped Tile {i}")

    # 画像を表示
    cv2.imshow('Flipped Mosaic Image', flipped_tile)
    cv2.waitKey(5000)  # 5秒待機

cv2.destroyAllWindows()

# 番号順に左右反転させたタイルを組み立て
flipped_tiles = [cv2.flip(tile, 1) for tile in tiles]

# 反転後のモザイクタイルを表示
mosaic_image = np.vstack([np.hstack(row) for row in np.array_split(flipped_tiles, 3)])
cv2.imshow('Flipped Mosaic Image', mosaic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# タイル番号のリストを表示
print("Tile Numbers:")
for tile_number in tile_numbers:
    print(tile_number)

