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

    # 



    img = 'hoge.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 3
    check_image_presence(check_image_path, max_tries)



except Exception as e:
    print("エラーが発生しました:", e)

finally:
    # ブラウザを閉じます
    driver.quit()
