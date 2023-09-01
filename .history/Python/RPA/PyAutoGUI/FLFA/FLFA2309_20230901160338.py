import os
import time
from selenium import webdriver
import pyautogui

# URLを指定
url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

# 待機時間を設定
wait_time_l = 10  # ページの読み込みなど、長めの待機時間
wait_time_m = 5   # クリックなど、中程度の待機時間

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # スクリプトのディレクトリを取得

def check_image_presence(target_image_path, max_tries):
    """
    指定された画像が画面上に含まれるか確認する関数。
    最大試行回数に達するまで画像検索を繰り返します。
    """
    try:
        try_count = 0
        found_image = False

        while try_count < max_tries:
            target_position = pyautogui.locateOnScreen(target_image_path)

            if target_position is not None:
                target_center = pyautogui.center(target_position)
                pyautogui.click(target_center)

                print("check_画像が見つかりました。clickしました。")
                found_image = True
                break  # 画像が見つかったらループを終了
            else:
                print("check_画像が見つかりませんでした。試行:", try_count + 1)
                try_count += 1
                time.sleep(1)  # 画像が見つからなかった場合、待機

        if found_image:
            # 画像が見つかった場合の処理をここに記述
            print("画像が見つかったため、後続の処理を行います。")
        else:
            print("画像が見つからなかったため、プログラムを終了します。")

            turn_on_numlock()
            exit()

    except Exception as e:
        print("エラーが発生しました:", e)

def input_sdate():
    # 画像のチェック
    img = 'sdate.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 3
    check_image_presence(check_image_path, max_tries)

    time.sleep(wait_time_m)
    pyautogui.press('space')
    time.sleep(wait_time_s)
    for i in range(4):
        pyautogui.press('down')
        time.sleep(wait_time_s)
    pyautogui.press('enter')
    time.sleep(wait_time_s)

def input_sdate():
    # 画像のチェック
    img = 'edate.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 3
    check_image_presence(check_image_path, max_tries)

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

        # スクレイピング処理をここで実行


        input_sdate()
        input_edate()



    finally:
        # ブラウザを閉じる
        driver.quit()

if __name__ == "__main__":
    main()
