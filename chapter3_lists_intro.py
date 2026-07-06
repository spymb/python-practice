# ---------------------------------------------------------------
# 文件名：chapter3_lists_intro.py
# 作者：Python学习者
# 日期：2026-07-05
# 功能描述：完成《Python编程：从入门到实践》第3章所有练习
#           涵盖列表的创建、访问、修改、排序及常见列表操作。
# ---------------------------------------------------------------

# =============================================================
# 练习 3.1：姓名
# 将一些朋友的姓名存储在一个列表中，依次访问并打印。
# =============================================================
print("=" * 50)
print("练习 3.1：姓名")

names = ["Zhang Wei", "Li Na", "Wang Hao", "Liu Yang", "Chen Jing"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
# =============================================================
# 练习 3.2：问候语
# 继续使用 3.1 的列表，为每人打印一条包含相同问候语的消息。
# =============================================================
print("=" * 50)
print("练习 3.2：问候语")

names = ["Zhang Wei", "Li Na", "Wang Hao", "Liu Yang", "Chen Jing"]
print(f"Hello, {names[0]}! Have a great day!")
print(f"Hello, {names[1]}! Have a great day!")
print(f"Hello, {names[2]}! Have a great day!")
print(f"Hello, {names[3]}! Have a great day!")
print(f"Hello, {names[4]}! Have a great day!")
# =============================================================
# 练习 3.3：自己的列表
# 创建一个包含多种通勤方式的列表，打印一系列陈述。
# =============================================================
print("=" * 50)
print("练习 3.3：自己的列表")

vehicles = ["Honda motorcycle", "Tesla car", "Giant bicycle", "subway", "scooter"]
print(f"I would like to own a {vehicles[0]}.")
print(f"I dream of driving a {vehicles[1]} one day.")
print(f"Riding a {vehicles[2]} on weekends sounds wonderful.")
print(f"Taking the {vehicles[3]} is the most efficient way to commute in the city.")
print(f"Using a {vehicles[4]} is a fun way to get around the neighborhood.")
# =============================================================
# 练习 3.4：嘉宾名单
# 创建包含至少三位想邀请共进晚餐的人的列表，打印邀请消息。
# =============================================================
print("=" * 50)
print("练习 3.4：嘉宾名单")

guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]
print(f"Dear {guests[0]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be honored to invite you to dinner.")
# =============================================================
# 练习 3.5：修改嘉宾名单
# 一位嘉宾无法赴约，替换为新嘉宾，重新发送邀请。
# =============================================================
print("=" * 50)
print("练习 3.5：修改嘉宾名单")

guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# 指出哪位嘉宾无法赴约
print(f"Unfortunately, {guests[2]} cannot make it to the dinner.")
print()

# 替换无法赴约的嘉宾
guests[2] = "Isaac Newton"

# 重新发送邀请
print(f"Dear {guests[0]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be honored to invite you to dinner.")
# =============================================================
# 练习 3.6：添加嘉宾
# 找到更大的餐桌，使用 insert()和 append() 再邀请三位嘉宾。
# =============================================================
print("=" * 50)
print("练习 3.6：添加嘉宾")

guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]

# 指出找到了更大的餐桌
print("Great news! I found a bigger dinner table, so we can invite more guests!")
print()

# 使用 insert() 将新嘉宾添加到开头
guests.insert(0, "Nikola Tesla")

# 使用 insert() 将新嘉宾添加到中间
guests.insert(len(guests) // 2, "Charles Darwin")

# 使用 append() 将新嘉宾添加到末尾
guests.append("Galileo Galilei")

# 打印邀请消息
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner.")
# =============================================================
# 练习 3.7：缩短名单
# 新餐桌无法送达，只能邀请两位嘉宾。使用 pop() 和 del 处理名单。
# =============================================================
print("=" * 50)
print("练习 3.7：缩短名单")

guests = ["Nikola Tesla", "Albert Einstein", "Charles Darwin",
          "Marie Curie", "Isaac Newton", "Galileo Galilei"]

# 打印只能邀请两位嘉宾的消息
print("Unfortunately, the new table won't arrive in time, "
      "so I can only invite two guests to dinner.")
print()

# 使用 pop() 不断删除嘉宾，直到只剩两位
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, I'm very sorry, "
          "but I can no longer invite you to dinner.")

print()

# 向余下的两位嘉宾确认他们仍在受邀之列
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

print()

# 使用 del 删除最后两位嘉宾，清空名单
del guests[1]
del guests[0]

# 打印名单，确认它是空的
print(f"Final guest list: {guests}")
# =============================================================
# 练习 3.8：放眼世界
# 存储想去旅游的地方，练习 sorted()、reverse()、sort() 等操作。
# =============================================================
print("=" * 50)
print("练习 3.8：放眼世界")

places = ["Tokyo", "Paris", "Bali", "New York", "Iceland"]

# 按原始排列顺序打印
print("Original order:")
print(places)

# 使用 sorted() 按字母顺序打印（不修改原列表）
print("\nAlphabetical order (sorted()):")
print(sorted(places))

# 核实排列顺序未变
print("\nAfter sorted() - original unchanged:")
print(places)

# 使用 sorted() 按字母相反顺序打印（不修改原列表）
print("\nReverse alphabetical order (sorted()):")
print(sorted(places, reverse=True))

# 核实排列顺序未变
print("\nAfter reverse sorted() - original unchanged:")
print(places)

# 使用 reverse() 反转列表顺序
print("\nAfter reverse():")
places.reverse()
print(places)

# 再次使用 reverse() 恢复到原来的排列顺序
print("\nAfter reverse() again - back to original:")
places.reverse()
print(places)

# 使用 sort() 按字母顺序排列
print("\nAfter sort() - alphabetical:")
places.sort()
print(places)

# 使用 sort() 按字母相反顺序排列
print("\nAfter sort(reverse=True) - reverse alphabetical:")
places.sort(reverse=True)
print(places)
# =============================================================
# 练习 3.9：晚餐嘉宾
# 使用 len() 打印一条消息，指出邀请了多少位嘉宾。
# =============================================================
print("=" * 50)
print("练习 3.9：晚餐嘉宾")

guests = ["Albert Einstein", "Marie Curie", "Isaac Newton",
          "Nikola Tesla", "Charles Darwin", "Galileo Galilei"]
print(f"I am inviting {len(guests)} guests to dinner.")
# =============================================================
# 练习 3.10：尝试使用各个函数
# 创建一个列表，尝试使用本章介绍的各种函数来处理它。
# =============================================================
print("=" * 50)
print("练习 3.10：尝试使用各个函数")

languages = ["Python", "JavaScript", "Rust", "Go", "TypeScript"]

# 访问元素（索引）
print(f"First language: {languages[0]}")
print(f"Last language: {languages[-1]}")

# 修改元素
languages[1] = "C++"
print(f"After modification: {languages}")

# append() - 在末尾添加
languages.append("Kotlin")
print(f"After append(): {languages}")

# insert() - 在指定位置插入
languages.insert(2, "Swift")
print(f"After insert(): {languages}")

# del - 删除指定位置的元素
del languages[4]
print(f"After del: {languages}")

# pop() - 弹出末尾元素
popped = languages.pop()
print(f"Popped: {popped}, remaining: {languages}")

# pop(index) - 弹出指定位置的元素
popped = languages.pop(1)
print(f"Popped index 1: {popped}, remaining: {languages}")

# remove() - 根据值删除元素
languages.remove("Rust")
print(f"After remove('Rust'): {languages}")

# sort() - 永久排序
languages.sort()
print(f"After sort(): {languages}")

# sort(reverse=True) - 永久反向排序
languages.sort(reverse=True)
print(f"After sort(reverse=True): {languages}")

# sorted() - 临时排序
print(f"sorted(): {sorted(languages)}")
print(f"Original after sorted(): {languages}")

# reverse() - 反转列表
languages.reverse()
print(f"After reverse(): {languages}")

# len() - 列表长度
print(f"List length: {len(languages)}")
# =============================================================
# 练习 3.11：有意引发错误
# 故意使用越界索引引发 IndexError，然后修正。
# =============================================================
print("=" * 50)
print("练习 3.11：有意引发错误")

items = ["apple", "banana", "cherry"]

# 有意引发索引错误 —— 列表只有3个元素（索引0~2），尝试访问索引3
# print(items[3])  # 取消注释将引发 IndexError: list index out of range

# 修正：使用正确的索引范围
print(f"The last item is: {items[-1]}")   # 推荐：使用 -1 获取最后一个元素
print(f"Valid indices are 0, 1, 2: {items[0]}, {items[1]}, {items[2]}")
