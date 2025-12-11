# 檔名: 01_variables_and_io.py
# 目的: 學習變數、輸入和輸出

# 印出一個歡迎訊息
print("--- 歡迎來到 Python 的世界 ---")

# 使用 input() 來問使用者的名字，並把結果存到 'user_name' 這個變數裡
user_name = input("請問你叫什麼名字？ ")

# 把使用者的名字和問候語結合在一起
# 注意我們用 + 來連接字串
greeting = "你好, " + user_name + "！"

# 把最後的問候語印出來
print(greeting)

print("--------------------------------")
input("按 Enter 鍵結束...")
