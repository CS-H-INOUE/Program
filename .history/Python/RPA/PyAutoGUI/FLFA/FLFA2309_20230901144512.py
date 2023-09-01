import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# インプットデータ（GUIからの選択に応じて設定）
user_data = ['293212000']

# ウェイト時間の定義
wait_time_s = 0.5
wait_time_m = 3
wait_time_l = 7

# URLの設定
url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

# pyautoguiで操作を行う関数
def perform_input_actions(input_actions):
    for action in input_actions:
        if action[0] == 'wait':
            time.sleep(action[1])
        elif action[0] == 'typewrite':
            pyautogui.typewrite(action[1][0])
            time.sleep(action[2])
        else:
            pyautogui.press(action[0])
            time.sleep(action[1])

# Chromeの起動
driver = webdriver.Chrome()

try:
    # URLにアクセス
    driver.get(url)
    
    # ウェイト（ページが読み込まれるまで待つ）
    time.sleep(wait_time_l)
    
    # pyautoguiで操作を実行
    input_actions = [
        ('right',),
        ('tab', wait_time_m),
        ('tab', wait_time_m),
        ('space', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('down', wait_time_s),
        ('down', wait_time_s),
        ('down', wait_time_s),
        ('down', wait_time_s),
        ('down', wait_time_s),
        ('down', wait_time_s),
        ('enter', wait_time_s),
        ('tab', wait_time_m),
        ('space', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('enter', wait_time_s),
        ('tab', wait_time_m),
        ('tab', wait_time_m),
        ('space', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('up', wait_time_s),
        ('down', wait_time_s),
        ('enter', wait_time_s),
        ('tab', wait_time_m),
        ('typewrite', (user_data[0],), wait_time_s),
        ('enter', wait_time_s),
    ]
    
    perform_input_actions(input_actions)
    
    # 選択されたデータに応じて表示名を取得
    data_display_names = {
        '293212000': 'FL',
        '293213000': 'FA'
    }
    
    selected_data = user_data[0]
    display_name = data_display_names.get(selected_data, 'Unknown')
    
    print(f'Selected Data: {selected_data} - Display Name: {display_name}')
    
finally:
    # ブラウザを終了
    driver.quit()
