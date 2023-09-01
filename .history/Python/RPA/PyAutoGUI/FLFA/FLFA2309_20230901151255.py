import time
from selenium import webdriver

# URLを指定します
url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

# 待機時間を設定します（秒単位）
wait_time_l = 10  # ページの読み込みなど、長めの待機時間
wait_time_m = 5   # クリックなど、中程度の待機時間

# Chromeウェブドライバーを起動します
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # ヘッドレスモード（画面表示なし）を有効にする場合
driver = webdriver.Chrome(options=options)

try:
    # URLにアクセスします
    driver.get(url)

    # 必要な処理をここで実行します
    # 例: タイトルを表示する場合
    print("ページタイトル:", driver.title)

    # 必要な待機時間を設定します
    time.sleep(wait_time_m)

    # その他のスクレイピング処理をここで実行します




except Exception as e:
    print("エラーが発生しました:", e)

finally:
    # ブラウザを閉じます
    driver.quit()
