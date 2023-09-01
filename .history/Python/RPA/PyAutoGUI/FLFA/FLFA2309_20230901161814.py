import os
import time
from selenium import webdriver
import pyautogui

# URLを指定
url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

# 待機時間を設定
wait_time_l = 10  # ページの読み込みなど、長めの待機時間
wait_time_m = 5   # クリックなど、中程度の待機時間
wait_time_s = 0.5

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # スクリプトのディレクトリを取得

def input_sdate():
    # 画像のチェック
    img = 'sdate.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 3
    check_image_presence(check_image_path, max_tries)

    time.sleep(wait_time_s)
    pyautogui.press('space')
    time.sleep(wait_time_s)
    for i in range(4):
        pyautogui.press('down')
        time.sleep(wait_time_s)
    pyautogui.press('enter')
    time.sleep(wait_time_s)

def input_sdate():

    time.sleep(wait_time_m)
    pyautogui.press('space')
    time.sleep(wait_time_s)
    for i in range(4):
        pyautogui.press('up')
        time.sleep(wait_time_s)
    pyautogui.press('enter')
    time.sleep(wait_time_s)


def main():

    # Chromeウェブドライバーを起動
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # ヘッドレスモード（画面表示なし）を有効にする場合
    driver = webdriver.Chrome(options=options)

    try:
        # URLにアクセス
        driver.get(url)

        # ページタイトルを表示
        print("ページタイトル:", driver.title)

        # 必要な待機時間を設定
        print('Please wait 5 sec.')
        time.sleep(wait_time_m)

        pyautogui.keyDown('win')
        pyautogui.press('up')
        pyautogui.keyUp('win')
        



    finally:
        # ブラウザを閉じる
        driver.quit()

if __name__ == "__main__":
    main()
