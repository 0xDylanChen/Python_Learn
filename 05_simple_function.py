# 檔名: 05_simple_function.py
# 目的: 學習如何定義和呼叫函式 (function)

print("--- 簡單的加法函式 ---")

# --- 函式定義區 ---
# 我們用 def 來定義一個函式
# 這個函式叫做 'add_two_numbers'
# 它需要兩個參數 (parameter), 我們暫時叫它們 a 和 b
def add_two_numbers(a, b):
    # 這是在函式裡面的程式碼
    print("函式內部: 我收到了", a, "和", b)
    # 把 a 和 b 加起來，存到 'total' 這個變數
    total = a + b
    # 用 return 把結果送回去
    return total
# --- 函式定義結束 ---


# --- 主程式區 ---
# 程式會從這裡開始跑
num1 = 10
num2 = 25

print("我要呼叫函式來把", num1, "和", num2, "加起來。")
print("--------------------------------")

# 這就是呼叫 (call) 我們的函式
# 我們把 num1 和 num2 當作引數 (argument) 送進去
# 函式會回傳一個結果，我們把它存到 'sum_result' 變數裡
sum_result = add_two_numbers(num1, num2)

print("--------------------------------")
print("函式算完後，回傳的結果是:", sum_result)

# 我們也可以直接用 input 來讓使用者決定數字
try:
    user_num1 = int(input("請再給我一個數字: "))
    user_num2 = int(input("再一個: "))
    
    # 再呼叫一次函式
    user_result = add_two_numbers(user_num1, user_num2)
    print("你輸入的數字加總是:", user_result)
except ValueError:
    print("抱歉，你輸入的不是數字。")


print("--------------------------------")
input("按 Enter 鍵結束...")

