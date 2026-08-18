import os
import sys
import subprocess
import time
import pyautogui
import pyperclip
from flask import Flask, render_template, request
import threading

app = Flask(__name__)
pyautogui.FAILSAFE = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move")
def move():
    dx = float(request.args.get("dx", 0))
    dy = float(request.args.get("dy", 0))
    pyautogui.move(dx, dy)
    return "OK"

@app.route("/click")
def click():
    pyautogui.click()
    return "OK"

@app.route("/right_click")
def right_click():
    pyautogui.rightClick()
    return "OK"

@app.route("/space")
def space():
    pyautogui.press("space")
    return "OK"

@app.route("/enter")
def enter():
    pyautogui.press("enter")
    return "OK"

@app.route("/backspace")
def backspace():
    pyautogui.press("backspace")
    return "OK"

@app.route("/alt_f4")
def alt_f4():
    pyautogui.hotkey('alt', 'f4')
    return "OK"

@app.route("/scroll")
def scroll():
    amount = int(request.args.get("amount", 0))
    try:
        pyautogui.scroll(amount)
        return "OK"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/mute")
def mute():
    pyautogui.press("volumemute")
    return "OK"

@app.route("/vol_up")
def vol_up():
    pyautogui.press("volumeup")
    return "OK"

@app.route("/vol_down")
def vol_down():
    pyautogui.press("volumedown")
    return "OK"

@app.route("/open_app")
def open_app():
    app_name = request.args.get("name")
    try:
        if app_name == "firefox":
            os.system("start firefox")
        elif app_name == "telegram":
            tg_path = os.path.expanduser("~") + r"\AppData\Roaming\Telegram Desktop\Telegram.exe"
            if os.path.exists(tg_path):
                os.startfile(tg_path)
            else:
                os.system("start telegram")
        elif app_name == "youtube":
            os.system("start https://www.youtube.com")
        elif app_name == "yummy":
            os.system("start https://yummyani.me")
        return f"OK: {app_name}"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/type_text")
def type_text():
    text = request.args.get("text", "")
    try:
        print(f"Пытаюсь вставить текст: {text}")
        
        # 2. Копируем текст в буфер обмена Windows
        pyperclip.copy(text)
        
        # 3. Даем системе чуть больше времени на обработку буфера
        time.sleep(0.15)
        
        # 4. Нажимаем Ctrl + V
        pyautogui.hotkey('ctrl', 'v')
        
        return "OK"
    except Exception as e:
        print(f"Ошибка печати: {str(e)}")
        return f"Error: {str(e)}"

@app.route("/restart_script")
def restart_script():
    def restart():
        time.sleep(0.5)
        python = sys.executable
        subprocess.Popen([python] + sys.argv)
        os._exit(0)
    threading.Thread(target=restart).start()
    return "Restarting..."

@app.route("/shutdown")
def shutdown():
    os.system("shutdown /s /t 1")
    return "Shutting down..."

@app.route("/reboot")
def reboot():
    os.system("shutdown /r /t 1")
    return "Rebooting..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)