# ---------------------------------------------------------------
# 文件名：chapter5_if_statements.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第5章所有练习
#           涵盖条件测试、if语句、if-else、if-elif-else结构。
# ---------------------------------------------------------------

# =============================================================
# 练习 5.1：条件测试
# 编写至少10个条件测试，结果为True和False的至少各5个。
# =============================================================
print("=" * 50)
print("练习 5.1：条件测试")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 更多条件测试
food = 'pizza'
print("\nIs food == 'pizza'? I predict True.")
print(food == 'pizza')

print("\nIs food == 'sushi'? I predict False.")
print(food == 'sushi')

age = 25
print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

score = 90
print("\nIs score >= 90? I predict True.")
print(score >= 90)

print("\nIs score <= 60? I predict False.")
print(score <= 60)

city = 'Beijing'
print("\nIs city == 'Beijing'? I predict True.")
print(city == 'Beijing')

print("\nIs city != 'Beijing'? I predict False.")
print(city != 'Beijing')

language = 'Python'
print("\nIs language == 'python'? I predict False.")
print(language == 'python')

print("\nIs language.lower() == 'python'? I predict True.")
print(language.lower() == 'python')
# =============================================================
# 练习 5.2：更多条件测试
# 对每种比较类型，至少编写两个结果分别为True和False的测试。
# =============================================================
print("=" * 50)
print("练习 5.2：更多条件测试")

# 1. 检查两个字符串是否相等和不等
s1, s2 = 'hello', 'hello'
print("\n--- 字符串相等/不等 ---")
print(f"s1 == s2 (相等): {s1 == s2}")        # True
print(f"s1 != s2 (不等): {s1 != s2}")        # False

s3, s4 = 'hello', 'world'
print(f"s3 == s4 (相等): {s3 == s4}")        # False
print(f"s3 != s4 (不等): {s3 != s4}")        # True

# 2. 使用 lower() 方法的条件测试
print("\n--- lower() 测试 ---")
word = 'PYTHON'
print(f"word.lower() == 'python': {word.lower() == 'python'}")  # True
print(f"word.lower() == 'PYTHON': {word.lower() == 'PYTHON'}")  # False

brand = 'Tesla'
print(f"brand.lower() == 'tesla': {brand.lower() == 'tesla'}")  # True
print(f"brand.lower() != 'tesla': {brand.lower() != 'tesla'}")  # False

# 3. 数值比较：相等、不等、大于、小于、大于等于、小于等于
print("\n--- 数值比较 ---")
a, b = 10, 20
print(f"a == b: {a == b}")      # False
print(f"a != b: {a != b}")      # True
print(f"a > b: {a > b}")        # False
print(f"a < b: {a < b}")        # True
print(f"a >= 10: {a >= 10}")    # True
print(f"a <= 5: {a <= 5}")      # False

c, d = 100, 100
print(f"c == d: {c == d}")      # True
print(f"c > d: {c > d}")        # False
print(f"c <= d: {c <= d}")      # True
print(f"d >= 200: {d >= 200}")  # False

# 4. 使用关键字 and 和 or 的条件测试
print("\n--- and / or 测试 ---")
x, y = 15, 30
print(f"x > 10 and y > 20: {x > 10 and y > 20}")    # True
print(f"x > 20 and y > 20: {x > 20 and y > 20}")    # False
print(f"x > 10 or y < 20: {x > 10 or y < 20}")      # True
print(f"x < 10 or y < 20: {x < 10 or y < 20}")      # False

# 5. 测试特定的值是否在列表中
print("\n--- 值是否在列表中 ---")
colors = ['red', 'green', 'blue', 'yellow', 'purple']
print(f"'red' in colors: {'red' in colors}")          # True
print(f"'green' in colors: {'green' in colors}")      # True
print(f"'orange' in colors: {'orange' in colors}")    # False
print(f"'black' in colors: {'black' in colors}")      # False

# 6. 测试特定的值是否不在列表中
print("\n--- 值是否不在列表中 ---")
print(f"'orange' not in colors: {'orange' not in colors}")  # True
print(f"'white' not in colors: {'white' not in colors}")    # True
print(f"'red' not in colors: {'red' not in colors}")        # False
print(f"'blue' not in colors: {'blue' not in colors}")      # False
# =============================================================
# 练习 5.3：外星人颜色 1
# 使用 if 语句测试外星人颜色，通过/未通过各一个版本。
# =============================================================
print("=" * 50)
print("练习 5.3：外星人颜色 1")

# 版本 1：条件测试通过
print("\n版本 1（条件测试通过）:")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

# 版本 2：条件测试未通过（无输出）
print("\n版本 2（条件测试未通过）:")
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
print("（没有输出，因为 alien_color 不是 'green'）")
# =============================================================
# 练习 5.4：外星人颜色 2
# 使用 if-else 结构，两个版本分别执行if块和else块。
# =============================================================
print("=" * 50)
print("练习 5.4：外星人颜色 2")

# 版本 1：执行 if 代码块
print("\n版本 1（执行 if 代码块）:")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# 版本 2：执行 else 代码块
print("\n版本 2（执行 else 代码块）:")
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")
# =============================================================
# 练习 5.5：外星人颜色 3
# 使用 if-elif-else 结构，三个版本分别对应三种颜色。
# =============================================================
print("=" * 50)
print("练习 5.5：外星人颜色 3")

# 版本 1：绿色外星人
print("\n版本 1（绿色外星人）:")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# 版本 2：黄色外星人
print("\n版本 2（黄色外星人）:")
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# 版本 3：红色外星人
print("\n版本 3（红色外星人）:")
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
# =============================================================
# 练习 5.6：人生的不同阶段
# 使用 if-elif-else 根据年龄判断人生阶段。
# =============================================================
print("=" * 50)
print("练习 5.6：人生的不同阶段")

ages = [1, 3, 8, 15, 25, 70]  # 测试多个年龄值

for age in ages:
    print(f"\nAge = {age}: ", end="")
    if age < 2:
        print("You are a baby.")
    elif age < 4:
        print("You are a toddler.")
    elif age < 13:
        print("You are a kid.")
    elif age < 18:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are an elder.")
# =============================================================
# 练习 5.7：喜欢的水果
# 列表包含三种喜欢的水果，写5条if语句检查特定水果。
# =============================================================
print("=" * 50)
print("练习 5.7：喜欢的水果")

favorite_fruits = ['mango', 'watermelon', 'strawberry']

# 检查 5 种水果
fruits_to_check = ['banana', 'mango', 'apple', 'watermelon', 'grape']

for fruit in fruits_to_check:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")
# =============================================================
# 练习 5.8：以特殊方式跟管理员打招呼
# 创建用户名列表，admin打印特殊问候，其他用户打印普通问候。
# =============================================================
print("=" * 50)
print("练习 5.8：以特殊方式跟管理员打招呼")

usernames = ['admin', 'Jaden', 'Sarah', 'Mike', 'Emily']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
# =============================================================
# 练习 5.9：处理没有用户的情形
# 先检查列表是否为空，为空则打印特殊消息。
# =============================================================
print("=" * 50)
print("练习 5.9：处理没有用户的情形")

# 先测试有用户的情况
print("\n（有用户的情况）:")
usernames = ['admin', 'Jaden', 'Sarah', 'Mike', 'Emily']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 清空列表，测试没有用户的情况
print("\n（清空列表后）:")
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
# =============================================================
# 练习 5.10：检查用户名
# 模拟网站检查新用户名是否已被使用（不区分大小写）。
# =============================================================
print("=" * 50)
print("练习 5.10：检查用户名")

current_users = ['John', 'Alice', 'Bob', 'Charlie', 'Diana']
new_users = ['john', 'Eve', 'ALICE', 'Frank', 'George']

# 创建 current_users 的全小写副本，用于不区分大小写的比较
current_users_lower = [user.lower() for user in current_users]

print(f"当前用户: {current_users}")
print(f"新注册用户: {new_users}\n")

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")
# =============================================================
# 练习 5.11：序数
# 打印数字 1~9 对应的序数（1st, 2nd, 3rd, 4th...）。
# =============================================================
print("=" * 50)
print("练习 5.11：序数")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
# =============================================================
# 练习 5.12：设置 if 语句的格式
# 审核本章所有 if 语句的格式——已完成。
# （所有条件测试都在比较运算符两侧加了空格，
#  缩进统一使用 4 个空格，代码块之间有空行分隔。）
# =============================================================
print("=" * 50)
print("练习 5.12：设置 if 语句的格式")

print("已审核：所有 if/elif/else 语句格式正确，")
print("比较运算符两侧均有空格，缩进统一为 4 个空格。")
# =============================================================
# 练习 5.13：自己的想法
# 记录编程想法：想开发的游戏、想研究的数据集、想创建的 Web 应用。
# =============================================================
print("=" * 50)
print("练习 5.13：自己的想法")

ideas = """
=== 我的编程想法 ===

[游戏] 想开发的游戏：
  - 一个文字冒险游戏，玩家探索地牢、收集物品、击败怪物
  - 基于 Pygame 的贪吃蛇游戏
  - 21 点（Blackjack）纸牌游戏的控制台版

[数据] 想研究的数据集：
  - 天气数据分析：研究当地气温变化趋势
  - 电影评分数据集：分析哪种类型的电影评分最高
  - 股票历史数据：学习数据可视化和趋势分析

[Web] 想创建的 Web 应用程序：
  - 个人博客系统（使用 Flask/Django）
  - 待办事项（Todo）管理应用
  - 简单的在线投票系统
"""

print(ideas)
