import os
import time
from selenium import webdriver

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  # スクリプトのディレクトリを取得

def check_image_presence(image_path, max_tries):
    """
    画像の存在を確認する関数

    Args:
        image_path (str): 画像ファイルのパス
        max_tries (int): 最大試行回数

    Returns:
        bool: 画像が存在すればTrue、存在しなければFalse
    """
    for _ in range(max_tries):
        if os.path.exists(image_path):
            return True
        time.sleep(1)  # 1秒待って再度試行
    return False

def main():
    # URLを指定
    url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

    # 待機時間を設定
    wait_time_l = 10  # ページの読み込みなど、長めの待機時間
    wait_time_m = 5   # クリックなど、中程度の待機時間

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
        time.sleep(wait_time_m)

        # スクレイピング処理をここで実行

        # 画像のチェック
        img = 'hoge.png'
        check_image_path = os.path.join(CURRENT_DIR, img)
        max_tries = 3
        if check_image_presence(check_image_path, max_tries):
            print("画像が存在します。")
        else:
            print("画像が存在しません。")

    except Exception as e:
        print("エラーが発生しました:", e)

    finally:
        # ブラウザを閉じる
        driver.quit()

if __name__ == "__main__":
    main()
