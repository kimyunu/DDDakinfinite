import tkinter as tk
import pyautogui
import time
import threading

running = False

def run_ddak():
    global running
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        delay = float(entry_delay.get())
        repeat = int(entry_repeat.get())
        running = True

        for i in range(repeat):
            if not running:
                print("딱 끝")
                break
            pyautogui.click(x, y)
            print(f"딱 {i+1}/{repeat}")
            time.sleep(delay)

    except Exception as e:
        print("에러 발생:", e)

def stop_ddak():
    global running
    running = False

def set_position():
    pos = pyautogui.position()
    entry_x.delete(0, tk.END)
    entry_x.insert(0, str(pos.x))
    entry_y.delete(0, tk.END)
    entry_y.insert(0, str(pos.y))

def start_ddak_thread():
    thread = threading.Thread(target=run_ddak)
    thread.start()

root = tk.Tk()
root.title("딱무한 2050")

tk.Label(root, text="딱 X 위치").grid(row=0, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

tk.Label(root, text="딱 Y 위치").grid(row=1, column=0)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

btn_pos = tk.Button(root, text="현재 위치 딱", command=set_position)
btn_pos.grid(row=0, column=2, rowspan=2, padx=10)

tk.Label(root, text="딱과 딱 사이 시간(초)").grid(row=2, column=0)
entry_delay = tk.Entry(root)
entry_delay.insert(0, "0.1")
entry_delay.grid(row=2, column=1)

tk.Label(root, text="딱 반복 횟수").grid(row=3, column=0)
entry_repeat = tk.Entry(root)
entry_repeat.insert(0, "10")
entry_repeat.grid(row=3, column=1)

btn_start = tk.Button(root, text="딱 시작", command=start_ddak_thread)
btn_start.grid(row=4, column=0, columnspan=2, pady=10)

btn_stop = tk.Button(root, text="딱 끝", command=stop_ddak)
btn_stop.grid(row=4, column=2, padx=5)

root.mainloop()
