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

def judge_matching(num):
    if 0.99 < num:
        return True
    else:
        return False

def main():
    try:

        # ターゲットとなる画像ファイルの絶対パス
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_filename = 'search.png'
        target_image_path = os.path.join(current_directory, image_filename)

        check_image_presence(target_image_path, MAX_IMAGE_SEARCH_TRIES)
        

        # 最も類似度が高い位置と低い位置を取得します
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

        #類似度が閾値を超えているか判定（上で作った関数を使用）
        judg = judge_matching(maxVal)

        print(judg)


        while True:
            if keyboard.is_pressed('ctrl+c') or (pyautogui.position()[0] < 10 and pyautogui.position()[1] < 10):
                raise KeyboardInterrupt  # プログラムを強制終了
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("プログラムを終了します。")

    except Exception as e:
        print("エラーが発生しました:", e)

if __name__ == "__main__":
    main()
