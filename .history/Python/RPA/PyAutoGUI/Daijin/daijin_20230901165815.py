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

# Junpo
# 定義された変数
COPY_PATHS = {
    0: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\01_tougetsu_241101_junpo.xls',
    1: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\02_zenkitougetsu_241101_junpo.xls',
    2: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\03_kichu_241101_junpo.xls',
    3: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\04_zennenkichu_241101_junpo.xls',

    4: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\05_tougetsu_241102_junpo.xls',
    5: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\06_zenkitougetsu_241102_junpo.xls',
    6: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\07_kichu_241102_junpo.xls',
    7: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\08_zennenkichu_241102_junpo.xls',

    8: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\08_tougetsu_221201_junpo.xls',
    9: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\09_zenkitougetsu_221201_junpo.xls',
    10: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\10_kichu_221201_junpo.xls',
    11: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\11_zennenkichu_221201_junpo.xls'
}

COPY_DIR = '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\'

# NumLock をオンにする
def turn_on_numlock():
    keyboard.press_and_release("num lock")

# NumLock をオフにする
def turn_off_numlock():
    keyboard.press_and_release("num lock")

def show_completion_message(n):
    def on_ok_button_click():
        print("他も検索するボタンが押されました。")
        root.destroy()  # ウィンドウを閉じる
        show_options()

    def on_exit_button_click():
        # ここに"終了"ボタンが押されたときの処理を追加
        print("Finished!!!!!")
        subprocess.Popen(["explorer", COPY_DIR])
        root.destroy()  # ウィンドウを閉じる

    root = tk.Tk()
    root.title("DL FINISHED")
    root.attributes("-topmost", True)  # ウィンドウを最前面に設定

    label = tk.Label(root, text="大臣DL完了", font=("Helvetica", 16))
    label.pack(padx=20, pady=20)

    ok_button = tk.Button(root, text="他も検索", command=on_ok_button_click)
    ok_button.pack(padx=10, pady=10)

    exit_button = tk.Button(root, text="終了", command=on_exit_button_click)
    exit_button.pack(padx=10, pady=10)

    root.mainloop()

def get_previous_month_range(date):
    """前月の開始日と終了日を計算する関数"""
    first_day_of_previous_month = date.replace(day=1) - timedelta(days=date.day)
    last_day_of_previous_month = date.replace(day=1) - timedelta(days=1)

    print (first_day_of_previous_month.year, first_day_of_previous_month.month, 1,
            last_day_of_previous_month.year, last_day_of_previous_month.month, last_day_of_previous_month.day)

    return (first_day_of_previous_month.year, first_day_of_previous_month.month, 1,
            last_day_of_previous_month.year, last_day_of_previous_month.month, last_day_of_previous_month.day)

def get_previous_year_previous_month_range(date):
    """前年の前月の開始日と終了日を計算する関数"""
    first_day_of_previous_year_previous_month = date.replace(year=date.year-1, day=1) - timedelta(days=date.day)
    last_day_of_previous_year_previous_month = date.replace(year=date.year-1, day=1) - timedelta(days=1)
    return (first_day_of_previous_year_previous_month.year, first_day_of_previous_year_previous_month.month, 1,
            last_day_of_previous_year_previous_month.year, last_day_of_previous_year_previous_month.month, last_day_of_previous_year_previous_month.day)

def get_recent_month_range(date, start_month):
    """直近の指定した月の開始日と終了日を計算する関数"""
    if date.month >= start_month:
        start_date = date.replace(month=start_month, day=1)
    else:
        start_date = date.replace(year=date.year-1, month=start_month, day=1)
    last_day_of_current_month = start_date.replace(day=1) + timedelta(days=32) - timedelta(days=1)
    last_day_of_current_month = last_day_of_current_month.replace(day=1) - timedelta(days=1)
    return (start_date.year, start_date.month, 1, last_day_of_current_month.year, last_day_of_current_month.month, last_day_of_current_month.day)

def get_recent_year_previous_month_range(date, start_month):
    """前年以前の直近の指定した月の開始日と終了日を計算する関数"""
    start_date = date.replace(year=date.year-1, month=start_month, day=1)
    last_day_of_current_month = start_date.replace(day=1) + timedelta(days=32) - timedelta(days=1)
    last_day_of_current_month = last_day_of_current_month.replace(day=1) - timedelta(days=1)
    return (start_date.year, start_date.month, 1, last_day_of_current_month.year, last_day_of_current_month.month, last_day_of_current_month.day)

def calculate_ranges(date):
    """各条件の期間を計算する関数"""
    start1, start_month1, start_day1, end1, end_month1, end_day1 = get_previous_month_range(date)
    start2, start_month2, start_day2, end2, end_month2, end_day2 = get_previous_year_previous_month_range(date)
    start3, start_month3, start_day3, _, _, _ = get_recent_month_range(date, 8)
    end3 = end1  # 条件1の終了日を使用
    start4, start_month4, start_day4, _, _, _ = get_recent_year_previous_month_range(date, 8)
    end4 = date.replace(year=date.year-1, day=1) - timedelta(days=1)
    return (start1, start_month1, start_day1, end1, end_month1, end_day1,
            start2, start_month2, start_day2, end2, end_month2, end_day2,
            start3, start_month3, start_day3, end1, 8, end_day1,
            start4, start_month4, start_day4, end4.year, 8, end4.day)

# cat: 241101, 241102 など
def daijin_dl(n,cat):
    """
        FLOW:::
        24->11 : 自由設計帳票：商品
        n=0: 初期起動から処理する

        24->11:
            241101_商品分類担当（商品、旬報中）
            241102 商品分類担当（商品、旬報上）

        nにより、保存ファイル（グローバルとして定義）が変わる

        COPY_PATHS = {
            0: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\01_tougetsu_junpo.xls',
            1: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\02_zenkitougetsu_junpo.xls',
            2: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\03_kichu_junpo.xls',
            3: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\04_zennenkichu_junpo.xls'

            4: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\05_tougetsu_241102_junpo.xls',
            5: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\06_zenkitougetsu_241102_junpo.xls',
            6: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\07_kichu_241102_junpo.xls',
            7: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\08_zennenkichu_241102_junpo.xls'

        }
    """
    if(cat == 1):
        if(n == 0):
            # 初回は、起動画面からの処理

            print('check_image:daijin.png')

            img = 'daijin_2.png'
            check_image_path = os.path.join(CURRENT_DIR, img)
            max_tries = 3
            check_image_presence(check_image_path, max_tries)

            time.sleep(2)
            pyautogui.typewrite('24')
            time.sleep(WAIT_TIME)
            pyautogui.press('enter')
            time.sleep(WAIT_TIME)
            pyautogui.typewrite('11')
            time.sleep(WAIT_TIME)
            pyautogui.press('enter')
            time.sleep(WAIT_TIME)

    elif(cat == 2):
        if(n == 0):

            time.sleep(2)
            pyautogui.press('up')
            time.sleep(WAIT_TIME)
            pyautogui.press('space')
            time.sleep(WAIT_TIME)
            for i in range(3):
                pyautogui.press('up')
            time.sleep(WAIT_TIME)
            for i in range(3):
                pyautogui.press('down')
                time.sleep(WAIT_TIME)
            pyautogui.press('enter')
            time.sleep(WAIT_TIME)

    #
    #
    # ここから、自由設計帳票：商品の処理
    #
    #

    # 共通処理
    print('共通処理をします')
    pyautogui.press('f2')
    print('press f2')
    time.sleep(WAIT_TIME)

    #
    #Check finished!
    # 1ogin: syouhinbunrui1
    img = 'file_output.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 10
    # print('check_dl1_input.png')
    print('check:file_output.png')
    check_image_presence(check_image_path, max_tries)

    time.sleep(WAIT_TIME)
    for i in range(2):
        pyautogui.press('tab')
        time.sleep(WAIT_TIME)

    #
    #
    # Delete
    #
    #
    for i in range(2):
        pyautogui.press('backspace')
        time.sleep(WAIT_TIME)
    pyautogui.press('delete')

    #
    # 日付選択: 当月
    #
    print('today')
    today = datetime.today()
    ranges = calculate_ranges(today)

    # ここでデータ格納
    # d1 = [(ranges[0] - 2018), (ranges[1]), (ranges[2]), (ranges[3] - 2018), (ranges[4]), (ranges[5])]
    # d2 = [(ranges[6] - 2018), (ranges[7]), (ranges[8]), (ranges[9] - 2018), (ranges[10]), (ranges[11])]
    # d3 = [(ranges[12] - 2018), 8, 1, (ranges[15] - 2018), (ranges[4]), (ranges[5])]
    # d4 = [(ranges[12] - 2018 - 1), 8, 1, (ranges[21] - 2018), (ranges[10]), (ranges[11])]

    # print('d1,d2')
    d1 = [(ranges[0] - 2018), (ranges[1]), (ranges[2]), (ranges[3] - 2018), (ranges[4]), (ranges[5])]
    d2 = [(ranges[6] - 2018), (ranges[7]), (ranges[8]), (ranges[9] - 2018), (ranges[10]), (ranges[11])]

    # 日付部分を日付オブジェクトに変換
    # print('d3')
    start_date3 = datetime(ranges[12], 8, 1)

    # print('d31')
    end_date3 = datetime(ranges[15], ranges[4], ranges[5])
    # print('d32')
    if(int(start_date3.month) > int(end_date3.month)):
        d3 = [start_date3.year - 2019, start_date3.month, start_date3.day, end_date3.year - 2018, end_date3.month, end_date3.day]
    else:
        d3 = [start_date3.year - 2018, start_date3.month, start_date3.day, end_date3.year - 2018, end_date3.month, end_date3.day]

    # print('d4')
    start_date4 = datetime(ranges[12] - 1, 8, 1)
    end_date4 = datetime(ranges[21], ranges[10], ranges[11])
    if (int(start_date4.month) > int(end_date4.month)):
        d4 = [start_date4.year - 2019, start_date4.month, start_date4.day, end_date4.year - 2018, end_date4.month, end_date4.day]
    else:
        d4 = [start_date4.year - 2018, start_date4.month, start_date4.day, end_date4.year - 2018, end_date4.month, end_date4.day]

    if(n == 0 or n == 4):
        print("今日の日付:", today.strftime("%Y/%m/%d"))
        print("条件1:", d1)

        time.sleep(2)
        pyautogui.typewrite(str(d1[0]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d1[1]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d1[2]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')

        pyautogui.typewrite(str(d1[3]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d1[4]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d1[5]))
        time.sleep(WAIT_TIME)

    elif(n == 1 or n == 5):
        print("条件2:", d2)

        time.sleep(2)
        pyautogui.typewrite(str(d2[0]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d2[1]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d2[2]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')

        pyautogui.typewrite(str(d2[3]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d2[4]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d2[5]))
        time.sleep(WAIT_TIME)

    elif(n == 2 or n == 6):
        print("条件3:", d3)

        time.sleep(2)
        pyautogui.typewrite(str(d3[0]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d3[1]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d3[2]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')

        pyautogui.typewrite(str(d3[3]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d3[4]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d3[5]))
        time.sleep(WAIT_TIME)

    elif(n == 3 or n == 7):
        print("条件4:", d4)

        time.sleep(2)
        pyautogui.typewrite(str(d4[0]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d4[1]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d4[2]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')

        pyautogui.typewrite(str(d4[3]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d4[4]))
        time.sleep(WAIT_TIME)
        pyautogui.press('right')
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(d4[5]))
        time.sleep(WAIT_TIME)

    pyautogui.press('tab')
    time.sleep(WAIT_TIME)
    pyautogui.press('tab')
    time.sleep(WAIT_TIME)
    pyautogui.press('enter')
    time.sleep(2)   # 画面遷移待ち

    pyautogui.press('tab')
    time.sleep(1)

    # テキストをクリップボードにコピー
    pyperclip.copy(COPY_PATHS[n])    # Ctrl+C（コピー）を実行
    print('DL COPY_PATH_' + str(n) + ':', COPY_PATHS[n])

    # Ctrl+V（貼り付け）を実行
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    time.sleep(WAIT_TIME)
    pyautogui.keyUp('ctrl')
    time.sleep(WAIT_TIME)

    pyautogui.press('tab')
    time.sleep(WAIT_TIME)
    pyautogui.press('tab')
    time.sleep(WAIT_TIME)
    pyautogui.press('enter')
    time.sleep(WAIT_TIME_LONG)

    #
    #Check finished!
    # p1: syouhinbunrui1
    #
    img = 'p2.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 10
    print('check: p2.png')
    check_image_presence(check_image_path, max_tries)

def operate_exe():

    for i in range(2):
        pyautogui.press('backspace')
    time.sleep(WAIT_TIME)

    #
    #Check finished!
    # 1ogin: syouhinbunrui1
    img = 'login.png'
    max_tries = 5
    check_image_path = os.path.join(CURRENT_DIR, img)
    print('check_login.png')
    check_image_presence(check_image_path, max_tries)

    time.sleep(WAIT_TIME)
    pyautogui.press('enter')
    time.sleep(WAIT_TIME)

    #
    #Check finished!
    # 1ogin: syouhinbunrui1
    img = 'login_2.png'
    check_image_path = os.path.join(CURRENT_DIR, img)
    max_tries = 5
    print('check_login2.png')
    check_image_presence(check_image_path, max_tries)

    pyautogui.press('enter')
    time.sleep(WAIT_TIME)
    print("EXEファイル起動")

def find_and_double_click(target_image_path, max_tries):
    """
    指定された画像をスクリーン上で検索し、中心座標をクリックする関数。
    最大試行回数に達するまで画像検索を繰り返します。
    """
    try:
        for try_count in range(max_tries):
            target_position = pyautogui.locateOnScreen(target_image_path)

            if target_position is not None:
                target_center = pyautogui.center(target_position)
                pyautogui.click(target_center)
                print("画像が見つかりました。クリックしました。")
                pyautogui.press('enter')
                time.sleep(2)   # 画面遷移待ち
                # pyautogui.hotkey('win','up')    # 最大化
                pyautogui.keyDown('win')
                time.sleep(WAIT_TIME)
                pyautogui.press('up')
                time.sleep(WAIT_TIME)
                pyautogui.keyUp('win')

                print('fnish find_and_double_click')

                break  # 画像が見つかったらループを終了
            else:
                print("画像が見つかりませんでした。試行:", try_count + 1)
                print('Program finished Unsuccessfully')
                if try_count == max_tries:
                    # GUI表示: 大臣DL完了
                    show_completion_message(2)
                    turn_on_numlock()
                    exit()  # 最大試行回数に達したらプログラムを終了
    except Exception as e:
        print("エラーが発生しました:", e)

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
