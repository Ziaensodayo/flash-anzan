import tkinter as tk
import random
import time
import tkinter.messagebox as messagebox
import unicodedata

numbers = []

def generate_numbers():
    numbers.clear()
    count = int(count_entry.get())  # 生成数を取得

    for _ in range(count):
        number = random.randint(1, 500)
        numbers.append(number)

    display_numbers()

def display_numbers():
    for number in numbers:
        numbers_label.config(text=str(number))
        window.update()
        time.sleep(0.1)
        numbers_label.config(text="")
        window.update()
        time.sleep(0.1)

    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    answer_label.config(text="")

def check_answer():
    user_answer = answer_entry.get()

    if not user_answer.isdigit():
        messagebox.showerror("エラー", "数字を入力してください")
        return

    user_answer = convert_to_halfwidth(user_answer)

    user_sum = sum(numbers)
    if int(user_answer) == user_sum:
        result_label.config(text="正解！", fg="green")
    else:
        result_label.config(text="不正解！", fg="red")
    answer_label.config(text=f"正解は {user_sum}")

def convert_to_halfwidth(text):
    return unicodedata.normalize("NFKC", text)

# Tkinterウィンドウの作成
window = tk.Tk()
window.title("フラッシュ暗算")
window.geometry("300x360")

# 数字を表示するラベル
numbers_label = tk.Label(window, text="", font=("Arial", 24))
numbers_label.pack(pady=20)

# 生成数入力用のラベルとテキストボックス
count_label = tk.Label(window, text="生成数：")
count_label.pack()
count_entry = tk.Entry(window, font=("Arial", 18))
count_entry.pack(pady=5)

# 問題の回答入力用のテキストボックス
answer_entry_label = tk.Label(window, text="回答を入力:")
answer_entry_label.pack()
answer_entry = tk.Entry(window, font=("Arial", 18))
answer_entry.pack(pady=10)

# 回答チェックボタン
check_button = tk.Button(window, text="回答をチェック", command=check_answer)
check_button.pack()

# 正誤結果を表示するラベル
result_label = tk.Label(window, text="", font=("Arial", 18))
result_label.pack(pady=10)

# 正答を表示するラベル
answer_label = tk.Label(window, text="", font=("Arial", 18))
answer_label.pack()

# 数字生成ボタン
generate_button = tk.Button(window, text="数字生成", command=generate_numbers)
generate_button.pack()

# ウィンドウのメインループ
window.mainloop()
