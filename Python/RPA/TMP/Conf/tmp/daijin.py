import pyautogui
import time
import keyboard

def remote_connect():
    print("リモートデスクトップ接続開始")
    
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    print("Run ダイアログを開く")
    
    pyautogui.write('mstsc.exe')
    pyautogui.press('enter')
    time.sleep(2)
    print("リモートデスクトップ接続ツールを起動")

    pyautogui.write('192.168.1.242')
    time.sleep(2)
    print("コンピューター名を入力")
    
    pyautogui.press('enter')
    time.sleep(3)
    print("接続ボタンをクリック")

    pyautogui.press('left')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

    print("接続完了")
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)
    
    print("EXEファイル起動")
    for i in range(2):
        pyautogui.press('enter')
        time.sleep(0.5)
        print(f"エンターキーを{i+1}回押下")

def main():
    try:
        remote_connect()  # リモート接続の関数を呼び出す

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
