import time
import pyautogui
import tkinter as tk
from selenium import webdriver

# ウェイト時間の定義
wait_time_s = 0.5
wait_time_m = 3
wait_time_l = 7

# URLの設定
url = 'https://www.customs.go.jp/toukei/srch/index.htm?M=77&P=0'

# 選択されたデータに応じて表示名を設定
data_display_names = {
    '293212000': 'FL',
    '293213000': 'FA'
}

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
    
    # GUIで選択したデータを取得
    def handle_option_selection(option, options_window):
        options_window.destroy()
        selected_data = list(data_display_names.keys())[option - 1]  # インデックスが0から始まるため、1を引く
        display_name = data_display_names[selected_data]
        daijin_exe(selected_data)  # 選択されたデータを引数として関数を呼び出す
        show_completion_message(display_name)

    def show_options():
        options_window = tk.Tk()
        options_window.title("選択肢")
        options_window.attributes("-topmost", True)  # ウィンドウを最前面に設定

        label = tk.Label(options_window, text="選択肢を選んでください:")
        label.pack(padx=20, pady=20)

        for index, display_name in enumerate(data_display_names.values(), start=1):
            option_button = tk.Button(options_window, text=display_name, command=lambda i=index: handle_option_selection(i, options_window))
            option_button.pack(padx=10, pady=5)

        options_window.mainloop()

    show_options()
    
    # Chromeの操作アクション
    input_actions = [
        # ここにChromeの操作アクションを追加する
    ]
    
    perform_input_actions(input_actions)
    
finally:
    # ブラウザを終了
    driver.quit()
