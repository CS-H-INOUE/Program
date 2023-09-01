import cv2
import os

# 画像ファイルのパス
image_filename = "IMG.jpg"
# 現在のファイルパス
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, image_filename)

# 画像を読み込む
image = cv2.imread(image_path)

# マウスで選択した領域の座標
selected_regions = []

# マウスクリックイベントのコールバック関数
def mouse_callback(event, x, y, flags, param):
    global selected_regions

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_regions.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", image)

# 画像ウィンドウを表示し、マウスクリックイベントを待機
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 選択した領域を表示
print("Selected regions:")
for region in selected_regions:
    print(region)
