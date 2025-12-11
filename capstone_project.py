# Capstone Project - Multi-Tool Program

# 全域變數 (Global Variables)
# 用一個 list 來存學生的名字
student_list = ["小明", "小華", "小英"]
# 用一個 dictionary 來存學生的成績
student_grades = {"小明": 85, "小華": 92, "小英": 78}

# 這是一個旗標，用來控制主迴圈
running = True

# --- 函式定義 (Function Definitions) ---

# 這是一個簡單的計算機函式
def calculator():
    print("--- 歡迎使用計算機 ---")
    
    # 試著讓使用者輸入數字
    try:
        num1 = float(input("請輸入第一個數字: "))
        op = input("請輸入運算符號 (+, -, *, /): ")
        num2 = float(input("請輸入第二個數字: "))
    except ValueError:
        print("輸入錯誤！只能輸入數字。")
        return # 如果有錯，就結束這個函式

    # 檢查使用者輸入的運算符號
    if op == "+":
        result = num1 + num2
        print("結果是: " + str(result))
    elif op == "-":
        result = num1 - num2
        print("結果是: " + str(result))
    elif op == "*":
        result = num1 * num2
        print("結果是: " + str(result))
    elif op == "/":
        # 檢查是否除以零
        if num2 == 0:
            print("錯誤！不可以除以零。")
        else:
            result = num1 / num2
            print("結果是: " + str(result))
    else:
        print("不支援的運算符號！")

# 這是一個猜數字遊戲的函式
def guessing_game():
    print("--- 歡迎來玩猜數字遊戲 ---")
    # 我們先偷偷設定一個祕密數字
    secret_number = 7
    guess_count = 0
    guess_limit = 3

    print("你有 " + str(guess_limit) + " 次機會可以猜。")
    
    # 讓使用者猜數字
    while guess_count < guess_limit:
        try:
            guess = int(input("猜一個 1 到 10 之間的數字: "))
        except ValueError:
            print("請輸入一個真正的數字！")
            continue # 跳過這次，再試一次

        # 增加猜測次數
        guess_count = guess_count + 1

        # 檢查數字
        if guess < secret_number:
            print("太小了！再試一次。")
        elif guess > secret_number:
            print("太大了！再試一次。")
        else:
            # 猜對了！
            print("恭喜你！你猜對了！")
            break # 跳出迴圈

    # 如果迴圈結束了還沒猜對
    if guess != secret_number:
        print("可惜，你沒猜對。祕密數字是 " + str(secret_number))


# --- 主程式 (Main Program) ---
# 這個 while 迴圈會讓程式一直跑
while running:
    # 印出主選單
    print("--------------------")
    print("歡迎使用多功能工具！")
    print("1. 計算機")
    print("2. 學生分數管理")
    print("3. 猜數字遊戲")
    print("4. 離開程式")
    print("--------------------")

    # 讓使用者選擇
    choice = input("請選擇一個功能 (1-4): ")

    # 根據使用者的選擇做不同的事
    if choice == "1":
        # 如果選 1，就呼叫計算機函式
        calculator()

    elif choice == "2":
        # 如果選 2，就管理學生分數
        print("--- 學生分數管理 ---")
        print("1. 顯示所有學生跟分數")
        print("2. 新增一個學生")
        
        sub_choice = input("請選擇 (1-2): ")

        if sub_choice == "1":
            # 顯示所有學生
            print("目前的學生名單:")
            for student in student_list:
                # 從 dictionary 拿出分數
                grade = student_grades[student]
                print(student + " 的分數是: " + str(grade))
        
        elif sub_choice == "2":
            # 新增學生
            new_student_name = input("請輸入新學生的名字: ")
            
            # 檢查學生是否已經存在
            if new_student_name in student_list:
                print("這個學生已經存在了！")
            else:
                try:
                    new_student_grade = int(input("請輸入 " + new_student_name + " 的分數: "))
                    # 把新學生加到 list 和 dictionary
                    student_list.append(new_student_name)
                    student_grades[new_student_name] = new_student_grade
                    print("成功新增 " + new_student_name + "！")
                except ValueError:
                    print("分數必須是數字！")
        else:
            print("沒有這個選項！")

    elif choice == "3":
        # 如果選 3，就玩猜數字遊戲
        guessing_game()

    elif choice == "4":
        # 如果選 4，就結束程式
        print("謝謝使用，掰掰！")
        running = False # 把旗標設成 False 來停止 while 迴圈

    else:
        # 如果使用者亂輸入
        print("無效的選擇，請重新輸入。")

    # 暫停一下，讓使用者可以看結果
    input("按 Enter 鍵繼續...")
