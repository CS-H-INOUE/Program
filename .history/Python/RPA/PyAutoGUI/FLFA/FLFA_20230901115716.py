import pyautogui
import datetime
from selenium import webdriver
import os
import glob
import shutil
from pathlib import Path
import zipfile
import csv
import openpyxl as px
from openpyxl.utils import column_index_from_string
import tkinter as tk
from tkinter import messagebox, simpledialog, StringVar, OptionMenu
import time

WAIT_TIME = 0.5
WAIT_TIME_LONG = 7

# %s は、文字列のフォーマット指定子（format specifier）の一つであり、Pythonにおいて文字列内で変数や値を埋め込むために使用されます。指定子 %s は、文字列（string）を埋め込むためのものであり、他のデータ型も埋め込むための別の指定子もあります。
# ex. url = 'https://www.example.com'
# chrome_command = CHROME_PATH % url
# システムコマンドを実行してChromeを開く
# os.system(chrome_command)
CHROME_PATH= r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# ダウンロードデータを処理する関数（必要に応じて実装）
def process_download_data(user_data):
    # ここにダウンロードデータの処理を追加する
    print('process_download_data(): finished!!')

# ファイルの一括削除
def remove_glob(pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)

# ユーザーにデータ選択を求める関数
def get_user_data():
    root = tk.Tk()
    root.withdraw()
    data_options = ['293212000: FL', '293213000: FA']
    selected_data = simpledialog.askstring("Data Selection", "Select data:", initialvalue=data_options[0])
    if selected_data == '293212000: FL':
        return ['293212000']
    elif selected_data == '293213000: FA':
        return ['293213000']
    else:
        return []

# WebDriverを起動する関数
def start_webdriver():
    
    # マルチディスプレイ環境でのディスプレイの情報を取得
    # 以下は2つのディスプレイを想定した例です
    # 実際の環境に合わせてディスプレイ情報を取得してください
    # 0番がメインディスプレイ、1番がセカンダリディスプレイと仮定しています
    display_id = 2

    # ウィンドウの位置を指定（左上隅の座標）
    window_position = {'x': 0, 'y': 0}

    # Chromeブラウザのオプションを設定
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # ヘッドレスモードで起動
    chrome_options.add_argument('--disable-gpu')  # GPUを無効にする
    chrome_options.add_argument(f'--display={display_id}')  # 表示するディスプレイを指定

    # Chromeドライバーを起動
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'
    driver.get(url)

    print('chrome exe. please waite 7 sec.')
    time.sleep(WAIT_TIME_LONG)

    # ウィンドウを最大化
    driver.set_window_position(window_position['x'], window_position['y'])
    driver.maximize_window()

# pyautoguiで操作を行う関数
def perform_pyautogui_actions(user_data):
    print("pyautogui: 操作を開始します.")
    
    def debug_print(message):
        if True:  # デバッグモードの条件を設定
            print(message)

    # 入力アクションの定義
    input_actions = [
        ('right',),
        ('tab', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('space', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('down', WAIT_TIME),
        ('down', WAIT_TIME),
        ('down', WAIT_TIME),
        ('down', WAIT_TIME),
        ('down', WAIT_TIME),
        ('down', WAIT_TIME),
        ('enter', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('space', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('enter', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('space', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('down', WAIT_TIME),
        ('enter', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('typewrite', ('105',), WAIT_TIME),
        ('tab', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('space', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('up', WAIT_TIME),
        ('down', WAIT_TIME),
        ('enter', WAIT_TIME),
        ('tab', WAIT_TIME),
        ('typewrite', (user_data[0],), WAIT_TIME),
        ('enter', WAIT_TIME),
    ]
    
    # 検索ボタンのアクション
    search_button_actions = [pyautogui.hotkey('shift', 'tab') for _ in range(12)]
    search_button_actions.append(pyautogui.press('enter'))
    
    for action in input_actions:
        debug_print(f"Performing action: {action[0]}")
        pyautogui.press(action[0])
        if len(action) == 2:
            time.sleep(action[1])

    for action in search_button_actions:
        debug_print("Performing search button action")
        action()
        time.sleep(WAIT_TIME)
        
    time.sleep(WAIT_TIME_LONG)
    print("pyautogui: 操作が完了しました.")

# メインの処理
def main():
    try:
        # 選択されたデータに応じて表示名を設定
        data_display_names = {
            '293212000': 'FL',
            '293213000': 'FA'
        }

        display_data_to_code = {v: k for k, v in data_display_names.items()}
        user_data = get_user_data()

        p_path = os.path.expanduser("~")

        print('WebDriverを起動します。')
        # WebDriverを起動
        start_webdriver()
        print('7秒待機しています...')
        time.sleep(WAIT_TIME_LONG)

        # pyautoguiでの操作を実行
        perform_pyautogui_actions(user_data)

        # 一時フォルダ内の古いZIPファイルを削除
        remove_glob(p_path + '/Downloads/*.zip')
        print("ダウンロードフォルダをクリーンアップしています...")

        # ダウンロードデータの処理
        process_download_data(user_data)

        today = datetime.date.today()
        Y = str(today.year)
        M = str(today.month)
        D = str(today.day)

        p = Path(p_path, "Downloads/")
        l_1 = list(p.glob('*.zip'))
        re_l = [f'{data_display_names[data]}.csv' for data in user_data]

        # 他の処理も同様に改善

    except KeyboardInterrupt:
        print('\n終了')
    except pyautogui.FailSafeException:
        print("マウスカーソルが画面の左上隅に来たため終了します。")
    except Exception as e:
        print('エラーが発生しました:', str(e))
        messagebox.showerror("エラー", "エラーが発生しました。詳細はコンソールをご確認ください。")

if __name__ == "__main__":
    main()
