import pyautogui
import time
import keyboard
import os
from datetime import datetime, timedelta
import pyperclip
import tkinter as tk
from tkinter import messagebox
import subprocess

WAIT_TIME = 0.8
WAIT_TIME_LONG = 5
MAX_IMAGE_SEARCH_TRIES = 3  # 画像検索を試行する最大回数

CURRENT_DIR = os.path.dirname(__file__)

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
                print("check_画像が見つかりました。")
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
            # GUI表示: 大臣DL完了
            show_completion_message(2)

            turn_on_numlock()
            exit()

    except Exception as e:
        print("エラーが発生しました:", e)

def remote_connect():
    print("リモートデスクトップ接続開始")

    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    print("Run ダイアログを開く")

    pyautogui.write('mstsc.exe')
    pyautogui.press('enter')
    time.sleep(2)
    print("リモートデスクトップ接続ツールを起動")

    #
    #Check remote exe
    #
    img = 'remote.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 3
    check_image_presence(check_image_path, max_tries)

    pyautogui.write('192.168.1.242')
    time.sleep(2)
    print("コンピューター名を入力")

    pyautogui.press('enter')
    time.sleep(3)
    print("接続ボタンをクリック")

    pyautogui.press('left')
    time.sleep(WAIT_TIME)
    pyautogui.press('enter')
    time.sleep(4)
    print("接続完了")
    pyautogui.press('down')
    time.sleep(WAIT_TIME)

def daijin_exe(cat):
    if(cat == 1):
        cat =1
        for i in range(4):
            print('Call daijin_dl(i) :', i, 'cat:', cat)
            daijin_dl(i,cat)
            time.sleep(WAIT_TIME)

    elif(cat == 2):
        for i in range[4:8]:
            print('Call daijin_dl(i) :',i, 'cat:', cat)
            daijin_dl(i,cat)
            time.sleep(WAIT_TIME)

    elif(cat == 3):
        for i in range[8:12]:
            print('Call daijin_dl(i) :',i, 'cat:', cat)
            daijin_dl(i,cat)
            time.sleep(WAIT_TIME)


def handle_option_selection(option,options_window):
    options_window.destroy()
    pyautogui.click(100, 150)  # pyautoguiで座標(100, 150)をクリック
    daijin_exe(option)
    show_completion_message(option)

def show_options():
    options_window = tk.Tk()
    options_window.title("選択肢")
    options_window.attributes("-topmost", True)  # ウィンドウを最前面に設定

    label = tk.Label(options_window, text="選択肢を選んでください:")
    label.pack(padx=20, pady=20)

    option1_button = tk.Button(options_window, text="24->11 旬報中段", command=lambda: handle_option_selection(1,options_window))
    option1_button.pack(padx=10, pady=5)

    option2_button = tk.Button(options_window, text="24->11 旬報上段", command=lambda: handle_option_selection(2,options_window))
    option2_button.pack(padx=10, pady=5)

    option2_button = tk.Button(options_window, text="22->12 仕入先", command=lambda: handle_option_selection(3,options_window))
    option2_button.pack(padx=10, pady=5)

    options_window.mainloop()


def env_handle_option_selection(option,options_window):
    """
    環境により、操作が異なる
    1: 1FPC /1F-SUB /2F -> ローカルプログラム起動
    2: Other -> リモート接続
    """
    options_window.destroy()
    if(option == 1):
        pyautogui.click(100, 150)  # pyautoguiで座標(100, 150)をクリック
        # ローカル環境のexeを起動
        print('sorry not implemented yet')
        exit()





    else:
        remote_connect()  # リモート接続の関数を呼び出す

def show_options_1():
    """
        DL環境の確認
        1FPC -> ローカルプログラム起動
        その他 -> リモート接続
    """

    options_window = tk.Tk()
    options_window.title("選択肢")
    options_window.attributes("-topmost", True)  # ウィンドウを最前面に設定

    label = tk.Label(options_window, text="選択肢を選んでください:")
    label.pack(padx=20, pady=20)

    option1_button = tk.Button(options_window, text="1F-MAINPC / 1F-SUBPC / 2F-PC ", command=lambda: env_handle_option_selection(1,options_window))
    option1_button.pack(padx=10, pady=5)

    option2_button = tk.Button(options_window, text="その他PC", command=lambda: env_handle_option_selection(2,options_window))
    option2_button.pack(padx=10, pady=5)

    options_window.mainloop()


def main():
    try:
        # Numlock OFF
        turn_off_numlock()

        show_options_1() # choose environment

        # ターゲットとなる画像ファイルの絶対パス
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_filename = 'image.png'
        target_image_path = os.path.join(current_directory, image_filename)

        # 画像の検索とクリックを行う関数を呼び出す
        find_and_double_click(target_image_path,MAX_IMAGE_SEARCH_TRIES)

        operate_exe() # EXEファイルを起動する関数を呼び出す
        print('operate_exe OK')

        show_options() # 大臣DLを行う関数を呼び出す*

        # Numlock ON
        turn_on_numlock()

        # Ctrl + C が押されたか、画面の左上隅にマウスが移動したかを監視
        while True:
            if keyboard.is_pressed('ctrl+c') or (pyautogui.position()[0] < 10 and pyautogui.position()[1] < 10):
                raise KeyboardInterrupt  # プログラムを強制終了
            time.sleep(0.1)

    except KeyboardInterrupt:
        turn_on_numlock()
        print("プログラムを終了します。")

    except Exception as e:
        turn_on_numlock()
        print("エラーが発生しました:", e)

if __name__ == "__main__":
    main()
