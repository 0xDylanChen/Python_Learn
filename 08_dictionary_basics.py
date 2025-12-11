# 檔名: 08_dictionary_basics.py
# 目的: 學習 dictionary (字典) 的基本使用

print("--- 簡單的電話簿 ---")

# 建立一個叫做 my_phonebook 的字典
# 大括號 {} 裡面放的是「名字: 電話號碼」這樣的鍵值對
my_phonebook = {
    "小明": "0912345678",
    "小花": "0987654321",
    "老師": "02-12345678"
}

print("目前的電話簿資料:")
print("--------------------------------")

# 用 for 迴圈來印出字典裡的所有資料
# .items() 會把字典裡的每一個鍵值對都拿出來
for name, number in my_phonebook.items():
    print("名字: " + name + ", 電話: " + number)

print("--------------------------------")

# 如何從字典裡找到某個人的電話號碼
search_name = input("你想找誰的電話號碼？ ")

# 檢查這個名字有沒有在電話簿裡
if search_name in my_phonebook:
    found_number = my_phonebook[search_name] # 用 key (名字) 來找 value (電話號碼)
    print(search_name + " 的電話號碼是: " + found_number)
else:
    print("對不起，電話簿裡沒有 " + search_name + " 的資料。")

print("--------------------------------")

# 新增一個新的聯絡人
new_name = input("請輸入新聯絡人的名字: ")
new_number = input("請輸入新聯絡人的電話號碼: ")

my_phonebook[new_name] = new_number # 用中括號 [] 來新增或更新資料
print("「" + new_name + "」已新增到電話簿！")

print("--------------------------------")
print("更新後的電話簿資料:")
for name, number in my_phonebook.items():
    print("名字: " + name + ", 電話: " + number)

print("--------------------------------")
input("按 Enter 鍵結束...")
