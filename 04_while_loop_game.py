# 檔名: 04_while_loop_game.py
# 目的: 學習 while 迴圈和 break

print("--- 猜數字遊戲 ---")
print("我心裡想好了一個 1 到 10 之間的數字。")

# 設定一個祕密數字
secret_number = 7

# 這是 while 迴圈，條件是 True，所以它會一直跑下去
# 直到我們在裡面用 break 把它停下來
while True:
    try:
        # 讓使用者猜一個數字
        guess_str = input("你猜是多少？ (或輸入 'quit' 離開): ")
        
        # 檢查使用者是不是想離開
        if guess_str == 'quit':
            print("好吧，下次再玩！")
            break # break 會立刻跳出這個 while 迴圈

        # 把輸入的字串轉成數字
        guess = int(guess_str)

        # 檢查猜的數字
        if guess < secret_number:
            print("太小了，再試一次！")
        elif guess > secret_number:
            print("太大了，再試一次！")
        else:
            print("恭喜你！猜對了！")
            break # 猜對了，也跳出迴圈

    except ValueError:
        print("請輸入數字，或是 'quit'。")

    print("--------------------------------")

print("遊戲結束。")
input("按 Enter 鍵結束...")

