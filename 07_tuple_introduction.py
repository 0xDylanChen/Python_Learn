# 檔名: 07_tuple_introduction.py
# 目的: 學習 tuple (元組) 的使用

print("--- 認識元組 (Tuple) ---")

# 建立一個元組，用小括號 () 包起來
# 元組一旦建立，裡面的東西就不能被改變了
my_coordinates = (10, 20)
my_personal_info = ("小花", 25, "女")
my_colors = ("紅", "綠", "藍")

print("我的座標是:", my_coordinates)
print("小花的個人資訊是:", my_personal_info)
print("我喜歡的顏色是:", my_personal_info)
print("--------------------------------")

# 存取元組裡面的資料，和列表一樣用索引號碼 (從 0 開始)
print("座標的 X 值是:", my_coordinates[0]) # 0 是第一個位置
print("座標的 Y 值是:", my_coordinates[1]) # 1 是第二個位置

print("小花的名字是:", my_personal_info[0])
print("小花的年齡是:", my_personal_info[1])

print("--------------------------------")

# 試圖修改元組 (會出錯！)
# 如果我們試著這樣做，Python 會告訴我們這是錯的
# my_coordinates[0] = 30 # 這行如果執行會報錯 TypeError

print("--------------------------------")
print("元組的長度 (裡面有幾個東西):", len(my_colors)) # 用 len() 檢查長度

input("按 Enter 鍵結束...")
