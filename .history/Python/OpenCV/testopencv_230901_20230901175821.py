import pyautogui
import screeninfo

# 画像ファイルのパス
image_path = ".png"

# モニター情報を取得
monitors = screeninfo.get_monitors()

# サブモニターの情報を取得（インデックスは環境によって変わる）
sub_monitor = monitors[1]

# サブモニターの解像度と位置を取得
width = sub_monitor.width
height = sub_monitor.height
x_offset = sub_monitor.x
y_offset = sub_monitor.y

# サブモニターの範囲を指定して画像と一致する部分の座標を取得
x, y = pyautogui.locateCenterOnScreen(image_path, region=(x_offset, y_offset, width, height))

# マウスを移動してクリック
pyautogui.moveTo(x, y)
pyautogui.click()
