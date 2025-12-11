# 檔名: 09_set_operations.py
# 目的: 學習 set (集合) 的基本操作

print("--- 認識集合 (Set) ---")

# 建立一個集合，用大括號 {} 包起來，但裡面只有值，沒有鍵
# 集合的特色是裡面的元素不會重複
my_set = {"蘋果", "香蕉", "橘子", "蘋果"} # 蘋果只會出現一次

print("我的集合裡有:", my_set)
print("--------------------------------")

# 增加一個元素到集合
my_set.add("西瓜")
print("新增西瓜後:", my_set)

# 試著再新增一個已經存在的元素，集合不會有變化
my_set.add("香蕉")
print("再新增香蕉後 (沒有改變):", my_set)

# 刪除一個元素
my_set.remove("橘子")
print("刪除橘子後:", my_set)

print("--------------------------------")

# 另一個集合
your_set = {"香蕉", "草莓", "芒果"}
print("你的集合裡有:", your_set)
print("--------------------------------")

# 兩個集合的聯集 (Union) - 把所有不重複的元素都加起來
union_set = my_set.union(your_set)
print("我的集合和你的集合的聯集是:", union_set)

# 兩個集合的交集 (Intersection) - 找出兩個集合都有的元素
intersection_set = my_set.intersection(your_set)
print("我的集合和你的集合的交集是:", intersection_set)

# 兩個集合的差集 (Difference) - 找出我的集合有，但你的集合沒有的元素
difference_set = my_set.difference(your_set)
print("我的集合有，但你的集合沒有的元素是:", difference_set)

print("--------------------------------")
input("按 Enter 鍵結束...")
