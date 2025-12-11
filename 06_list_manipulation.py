# 檔名: 06_list_manipulation.py
# 目的: 學習 list 的常用操作 (新增、刪除、顯示)

print("--- 簡單的待辦事項列表 ---")

# 建立一個空的列表，用來存放待辦事項
todo_list = []

# 設定一個旗標，讓程式可以一直跑
running_todo_app = True

while running_todo_app:
    print("--------------------------------")
    print("1. 新增待辦事項")
    print("2. 顯示所有事項")
    print("3. 刪除待辦事項")
    print("4. 離開")
    print("--------------------------------")

    choice = input("請選擇功能 (1-4): ")

    if choice == "1":
        # 新增事項
        new_item = input("請輸入新的待辦事項: ")
        todo_list.append(new_item) # 使用 append() 把新項目加到列表的最後
        print("「" + new_item + "」已新增！")

    elif choice == "2":
        # 顯示所有事項
        print("目前的待辦事項:")
        if len(todo_list) == 0: # 使用 len() 檢查列表有沒有東西
            print("目前沒有任何待辦事項。")
        else:
            item_count = 1
            for item in todo_list:
                print(str(item_count) + ". " + item) # 用索引號碼顯示
                item_count = item_count + 1

    elif choice == "3":
        # 刪除事項
        if len(todo_list) == 0:
            print("沒有待辦事項可以刪除。")
        else:
            print("目前的待辦事項:")
            item_count = 1
            for item in todo_list:
                print(str(item_count) + ". " + item)
                item_count = item_count + 1
            
            try:
                delete_index = int(input("請輸入要刪除的事項編號: "))
                # 列表的索引是從 0 開始，所以要減 1
                if 0 < delete_index <= len(todo_list):
                    deleted_item = todo_list.pop(delete_index - 1) # 使用 pop() 刪除指定位置的項目
                    print("「" + deleted_item + "」已刪除！")
                else:
                    print("編號無效，請重新輸入。")
            except ValueError:
                print("輸入錯誤，請輸入數字編號。")

    elif choice == "4":
        # 離開程式
        running_todo_app = False
        print("感謝使用待辦事項程式！")

    else:
        print("無效的選擇，請重新輸入。")

    if running_todo_app: # 如果還沒離開，就等使用者按 Enter
        input("按 Enter 鍵繼續...")
