import pyautogui
import time
import keyboard
import os
from datetime import datetime, timedelta
import pyperclip

WAIT_TIME = 0.5
WAIT_TIME_LONG = 5
MAX_IMAGE_SEARCH_TRIES = 3  # 画像検索を試行する最大回数

# Junpo
# 定義された変数
COPY_PATHS = {
    0: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\01_tougetsu_junpo.xls',
    1: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\02_zenkitougetsu_junpo.xls',
    2: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\03_kichu_junpo.xls',
    3: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\04_zennenkichu_junpo.xls'
}

# NumLock をオンにする
def turn_on_numlock():
    keyboard.press_and_release("num lock")

# NumLock をオフにする
def turn_off_numlock():
    keyboard.press_and_release("num lock")

def get_previous_month_range(date):
    """前月の開始日と終了日を計算する関数"""
    first_day_of_previous_month = date.replace(day=1) - timedelta(days=date.day)
    last_day_of_previous_month = date.replace(day=1) - timedelta(days=1)
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

def daijin_dl(n):
    """
        24->11 : 自由設計帳票：商品
        n=0: 初期起動から処理する

        nにより、保存ファイル（グローバルとして定義）が変わる

        COPY_PATHS = {
            0: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\01_tougetsu_junpo.xls',
            1: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\02_zenkitougetsu_junpo.xls',
            2: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\03_kichu_junpo.xls',
            3: '\\\\192.168.1.240\\中部産商(共有)\\【会議】\\D_Data\\Data_py\\04_zennenkichu_junpo.xls'
        }
    """

    if(n == 0):
        # 初回は、起動画面からの処理

        check_image_path = 'daijin.png'
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

    #
    #
    # ここから、自由設計帳票：商品の処理
    #
    #

    # 共通処理
    print('共通処理をします')
    pyautogui.press('f2')
    print('press f2')
    time.sleep(WAIT_TIME_LONG)

    for i in range(2):
        pyautogui.press('tab')
        time.sleep(WAIT_TIME)


    #
    # 日付選択: 当月
    #
    today = datetime.today()
    ranges = calculate_ranges(today)

    # ここでデータ格納
    d1 = [(ranges[0] - 2018), (ranges[1]), (ranges[2]), (ranges[3] - 2018), (ranges[4]), (ranges[5])]
    d2 = [(ranges[6] - 2018), (ranges[7]), (ranges[8]), (ranges[9] - 2018), (ranges[10]), (ranges[11])]
    d3 = [(ranges[12] - 2018), 8, 1, (ranges[15] - 2018), (ranges[4]), (ranges[5])]
    d4 = [(ranges[12] - 2018 - 1), 8, 1, (ranges[21] - 2018), (ranges[10]), (ranges[11])]

    print("今日の日付:", today.strftime("%Y/%m/%d"))
    print("条件1:", d1)
    print("条件2:", ranges[6], "/", ranges[7], "/", ranges[8], "-", ranges[9], "/", ranges[10], "/", ranges[11])
    print("条件3:", ranges[12], "/", 8, "/", 1, "-", ranges[15], "/", ranges[4], "/", ranges[5])
    print("条件4:", ranges[12]-1, "/", 8, "/", 1, "-", ranges[21], "/", ranges[10], "/", ranges[11])

    if(n == 0):

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

    elif(n == 1):

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

    elif(n == 2):

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

    elif(n == 3):

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

    print('Wait 7 seconds...............................')

def operate_exe():
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(WAIT_TIME)
    pyautogui.press('enter')
    time.sleep(2)
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
                time.sleep(WAIT_TIME)   # 画面遷移待ち
                pyautogui.hotkey('win','up')    # 最大化
                time.sleep(WAIT_TIME)

                break  # 画像が見つかったらループを終了
            else:
                print("画像が見つかりませんでした。試行:", try_count + 1)
                print('Program finished Unsuccessfully')
                if try_count == max_tries:
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
                print("画像が見つかりました。")
                found_image = True
                break  # 画像が見つかったらループを終了
            else:
                print("画像が見つかりませんでした。試行:", try_count + 1)
                try_count += 1
                time.sleep(WAIT_TIME)  # 画像が見つからなかった場合、待機

        if found_image:
            # 画像が見つかった場合の処理をここに記述
            print("画像が見つかったため、後続の処理を行います。")
        else:
            print("画像が見つからなかったため、プログラムを終了します。")

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
    check_image_path = 'remote.png'
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

def main():
    try:
        # Numlock OFF
        turn_off_numlock()

        remote_connect()  # リモート接続の関数を呼び出す

        # ターゲットとなる画像ファイルの絶対パス
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_filename = 'image.png'
        target_image_path = os.path.join(current_directory, image_filename)

        # 画像の検索とクリックを行う関数を呼び出す
        find_and_double_click(target_image_path,MAX_IMAGE_SEARCH_TRIES)

        print('exe command complete')

        operate_exe() # EXEファイルを起動する関数を呼び出す

        for i in range(4):
            print('Call daijin_dl(i) :',i)
            daijin_dl(i)

        # Numlock ON
        turn_on_numlock()

        # Ctrl + C が押されたか、画面の左上隅にマウスが移動したかを監視
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
