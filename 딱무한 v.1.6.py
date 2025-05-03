
import tkinter as tk
import pyautogui
import time
import threading
#import keyboard

running = False
click_pos = None

def listen_for_click():
    global click_pos
    click_pos = None
    print("마우스로 클릭해서 위치를 지정하세요...")
    while click_pos is None:
        if pyautogui.mouseDown():
            click_pos = pyautogui.position()
            print(f"선택된 위치: {click_pos}")
            break

def run_ddak():
    global running, click_pos
    try:
        delay = float(entry_delay.get())
        repeat = int(entry_repeat.get())

        # 클릭 위치 받기
        listen_for_click()
        if click_pos is None:
            print("위치 선택이 취소되었습니다.")
            return

        running = True

        for i in range(repeat):
            if not running:
                print("딱 끝")
                break
            pyautogui.click(click_pos)
            print(f"딱 {i+1}/{repeat}")
            time.sleep(delay)

    except Exception as e:
        print("에러 발생:", e)

def stop_ddak():
    global running
    running = False

def start_ddak_thread():
    thread = threading.Thread(target=run_ddak)
    thread.start()

root = tk.Tk()
root.title("딱무한 2050")

tk.Label(root, text="딱과 딱 사이 시간(초)").grid(row=0, column=0)
entry_delay = tk.Entry(root)
entry_delay.insert(0, "0.1")
entry_delay.grid(row=0, column=1)

tk.Label(root, text="딱 반복 횟수").grid(row=1, column=0)
entry_repeat = tk.Entry(root)
entry_repeat.insert(0, "10")
entry_repeat.grid(row=1, column=1)

btn_start = tk.Button(root, text="딱 시작", command=start_ddak_thread)
btn_start.grid(row=2, column=0, columnspan=2, pady=10)

btn_stop = tk.Button(root, text="딱 끝", command=stop_ddak)
btn_stop.grid(row=2, column=2, padx=5)

root.mainloop()
