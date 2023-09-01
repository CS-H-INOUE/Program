import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests
from bs4 import BeautifulSoup

def on_button_click():
    user_input = entry.get()
    selected_option = dropdown_var.get()
    
    if selected_option == "a":
        entry.delete(0, tk.END)  # 入力フィールドのクリア
        entry.insert(0, "TEST TARO")  # テキストの挿入
    elif selected_option == "b":
        webbrowser.open("https://www.google.com")  # Chromeを開く
    elif selected_option == "c":
        weather_data = get_weather()
        if weather_data:
            message = f"Today's weather: {weather_data}"
            messagebox.showinfo("Weather", message)
        else:
            messagebox.showerror("Error", "Failed to fetch weather data.")
    else:
        messagebox.showerror("Error", "Please select a valid option.")

def on_exit_button_click():
    if messagebox.askyesno("Exit", "Do you really want to quit?"):
        root.destroy()

def toggle_fullscreen():
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def get_weather():
    try:
        url = "https://www.jma.go.jp/jp/yoho/319.html"  # 気象庁の天気予報ページ
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        weather_data = soup.select_one(".info-time-weather").get_text(strip=True)
        return weather_data
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

# ウィンドウの作成
root = tk.Tk()
root.title("Feature-Rich GUI App")

# ウィンドウのサイズ設定
width, height = 600, 600
root.geometry(f"{width}x{height}")

# ラベル
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# エントリー
entry = tk.Entry(root)
entry.pack(pady=5)

# ドロップ
