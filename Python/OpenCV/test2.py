import cv2
import pytesseract
import os

# 画像ファイルのパス
image_filename = "IMG.jpg"
# 現在のファイルパス
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, image_filename)

# Tesseractのパス（環境に合わせて変更してください）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 画像を読み込む
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load image")
else:
    print("Image loaded successfully")

# テキスト領域を切り出してOCRを適用する関数
def process_text_regions(image, text_regions):
    extracted_text = []

    for idx, region in enumerate(text_regions):
        x, y, w, h = region  # テキスト領域の座標情報
        text_image = image[y:y+h, x:x+w]  # テキスト領域の切り出し

        print(f"Processing region {idx}")
        print(f"Region coordinates: ({x}, {y}, {w}, {h})")

        # 切り出したテキスト領域を画像として保存（デバッグ用）
        region_image_path = f"debug_region_{idx}.jpg"
        cv2.imwrite(region_image_path, text_image)

        # OCRを適用してテキストを抽出
        result = pytesseract.image_to_string(text_image, lang='jpn')

        print(f"Extracted text from region {idx}: {result.strip()}")
        extracted_text.append(result.strip())

    return extracted_text

# テキスト領域の座標情報をテキストファイルから読み込む
text_regions = []
regions_file_path = "extracted_text_regions.txt"
if os.path.exists(regions_file_path):
    with open(regions_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            region = tuple(map(int, line.strip().split(',')))
            text_regions.append(region)

    print("Text regions loaded successfully")
else:
    print("Text regions file not found")

# テキスト領域を切り出してOCRを適用
extracted_text = process_text_regions(image, text_regions)

# OCR結果を表示
for text in extracted_text:
    print("Extracted text:", text)
