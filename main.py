import tkinter as tk
import random
import traceback
from tkinter import messagebox

def on_confirm():
    name = entry_name.get().strip()
    if not name:
        messagebox.showwarning("提示", "请输入名字")
        return
    gender = "男的" if random.choice([True, False]) else "女的"
    label_result.config(text=f"{name}，你是{gender}")

try:
    root = tk.Tk()
    root.title("性别判断器")
    root.geometry("300x180")

    label_prompt = tk.Label(root, text="请输入你的名字：")
    label_prompt.pack(pady=10)

    entry_name = tk.Entry(root, width=30)
    entry_name.pack()

    btn_confirm = tk.Button(root, text="确认", command=on_confirm)
    btn_confirm.pack(pady=10)

    label_result = tk.Label(root, text="", font=("Arial", 12))
    label_result.pack(pady=10)

    root.mainloop()
except Exception as e:
    # 弹出异常内容（不会被黑窗口吞掉）
    messagebox.showerror("程序崩溃", traceback.format_exc())