import cv2
import os

# PNG画像をJPEGに変換する関数
def convert_png_to_jpg(input_path, output_path):
    # PNG画像を読み込む
    image = cv2.imread(input_path)

    # もし画像が読み込めなかった場合
    if image is None:
        print(f"Error: Unable to load image from {input_path}")
        return

    # JPEG形式で保存
    success = cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

    # もし画像を保存できなかった場合
    if not success:
        print(f"Error: Unable to save image to {output_path}")
    else:
        print(f"Image saved as {output_path}")

# カレントディレクトリのパス
current_directory = os.getcwd()

# 変換元のPNG画像ファイル名
image_filename = "IMG.png"

# 変換後のJPEG画像ファイル名
output_filename = "output.jpg"

# 画像ファイルのパスを作成
input_image_path = os.path.join(current_directory, image_filename)
output_image_path = os.path.join(current_directory, output_filename)

# PNGからJPEGに変換
convert_png_to_jpg(input_image_path, output_image_path)

# 変換後のJPEG画像を読み込む
image = cv2.imread(output_image_path)

# もし画像が読み込めなかった場合
if image is None:
    print(f"Error: Unable to load image from {output_image_path}")
else:
    # 画像を表示
    cv2.imshow("Converted Image", image)

    # キー入力待ち（任意のキーを押すと終了）
    cv2.waitKey(0)

    # ウィンドウを閉じる
    cv2.destroyAllWindows()
