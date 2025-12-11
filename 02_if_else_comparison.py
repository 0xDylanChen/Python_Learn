# 檔名: 02_if_else_comparison.py
# 目的: 學習 if/elif/else 條件判斷與型別轉換

print("--- 數字比大小 ---")

# 準備一個 flag 來檢查輸入是否成功
input_ok = False

# 用一個迴圈來確保我們拿到正確的數字
while not input_ok:
    try:
        # 讓使用者輸入第一個數字
        num_str_1 = input("請輸入第一個數字: ")
        # 把使用者輸入的字串用 int() 轉成真正的整數
        number1 = int(num_str_1)

        # 讓使用者輸入第二個數字
        num_str_2 = input("請輸入第二個數字: ")
        number2 = int(num_str_2)
        
        # 如果都成功，就把 flag 設為 True
        input_ok = True

    except ValueError:
        # 如果 int() 轉換失敗，就會跑到這裡
        print("輸入錯誤！請確定你輸入的是整數。")
        print("--------------------------------")

# 開始比較
# 檢查 number1 是不是大於 number2
if number1 > number2:
    print("第一個數字 (" + str(number1) + ") 比較大。")
# 如果不大於，再檢查是不是 number1 比較小
elif number1 < number2:
    print("第二個數字 (" + str(number2) + ") 比較大。")
# 如果不大於也不小於，那一定就是相等
else:
    print("兩個數字一樣大。")

print("--------------------------------")
input("按 Enter 鍵結束...")
