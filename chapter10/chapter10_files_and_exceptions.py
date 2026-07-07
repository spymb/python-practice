# ---------------------------------------------------------------
# 文件名：chapter10_files_and_exceptions.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第10章所有练习
#           涵盖文件读取、写入、异常处理及JSON数据存储。
# ---------------------------------------------------------------

import os
import json

# =============================================================
# 练习 10.1：Python 学习笔记
# 读取 learning_python.txt，打印两次：
#   第一次：读取整个文件
#   第二次：先存入列表，再遍历各行
# =============================================================
print("=" * 50)
print("练习 10.1：Python 学习笔记")

filename = 'chapter10/learning_python.txt'

# 第一次：读取整个文件
print("--- Reading the entire file ---")
with open(filename, encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 第二次：遍历各行
print("\n--- Reading line by line ---")
with open(filename, encoding='utf-8') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# =============================================================
# 练习 10.2：C 语言学习笔记
# 读取 learning_python.txt，将每行中的 'Python' 替换为其他语言，
# 并打印替换后的结果。
# =============================================================
print("=" * 50)
print("练习 10.2：C 语言学习笔记")

with open(filename, encoding='utf-8') as file_object:
    for line in file_object:
        modified_line = line.replace('Python', 'C')
        print(modified_line.rstrip())

# =============================================================
# 练习 10.3：简化代码
# 删除临时变量，直接遍历 splitlines() 返回的列表。
# =============================================================
print("=" * 50)
print("练习 10.3：简化代码")

# 原来的写法（使用临时变量）
print("--- Original (with temp variable 'lines') ---")
with open(filename, encoding='utf-8') as file_object:
    contents = file_object.read()
lines = contents.splitlines()
for line in lines:
    print(f"  {line}")

# 简化后的写法（删除临时变量）
print("\n--- Simplified (no temp variable) ---")
with open(filename, encoding='utf-8') as file_object:
    contents = file_object.read()
for line in contents.splitlines():
    print(f"  {line}")

print("\n(Simplified: removed the 'lines' variable, iterating splitlines() directly.)")

# =============================================================
# 练习 10.4：访客
# 提示用户输入名字，将其写入 guest.txt。
# =============================================================
print("=" * 50)
print("练习 10.4：访客")

guest_name = input("Please enter your name: ")
with open('chapter10/guest.txt', 'w', encoding='utf-8') as file_object:
    file_object.write(guest_name)
print(f"Hello, {guest_name}! Your name has been saved to guest.txt.")

# =============================================================
# 练习 10.5：访客簿
# 用 while 循环收集多个名字，写入 guest_book.txt。
# =============================================================
print("=" * 50)
print("练习 10.5：访客簿")

print("Enter 'quit' at any time to stop.")
with open('chapter10/guest_book.txt', 'a', encoding='utf-8') as file_object:
    while True:
        name = input("Please enter your name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        file_object.write(f"{name}\n")
        print(f"Welcome, {name}! Your name has been recorded.")

print("Guest book entries saved to guest_book.txt.")

# =============================================================
# 练习 10.6：加法运算
# 提示用户输入两个数，相加并打印结果。
# 在输入不是数时捕获 ValueError 异常。
# =============================================================
print("=" * 50)
print("练习 10.6：加法运算")

try:
    num1 = input("Enter the first number: ")
    num1 = int(num1)
    num2 = input("Enter the second number: ")
    num2 = int(num2)
except ValueError:
    print("Error: Please enter valid numbers, not text!")
else:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

# =============================================================
# 练习 10.7：加法计算器
# 将练习 10.6 放在 while 循环中，让用户能在出错后继续输入。
# =============================================================
print("=" * 50)
print("练习 10.7：加法计算器")

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter the first number (or 'q' to quit): ")
    if first.lower() == 'q':
        break
    second = input("Enter the second number (or 'q' to quit): ")
    if second.lower() == 'q':
        break
    try:
        result = int(first) + int(second)
    except ValueError:
        print("Error: Please enter valid numbers, not text! Please try again.")
    else:
        print(f"{first} + {second} = {result}")

print("Calculator closed.")

# =============================================================
# 练习 10.8：猫和狗
# 读取 cats.txt 和 dogs.txt，用 try-except 处理 FileNotFoundError。
# =============================================================
print("=" * 50)
print("练习 10.8：猫和狗")


def print_file_content(filename, animal_type):
    """尝试读取文件并打印内容。"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(f"--- {animal_type} ---")
            print(contents.rstrip())
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")


print_file_content('chapter10/cats.txt', 'Cats')
print()
print_file_content('chapter10/dogs.txt', 'Dogs')

# =============================================================
# 练习 10.9：静默的猫和狗
# 修改 except 代码块，在文件不存在时静默失败。
# =============================================================
print("=" * 50)
print("练习 10.9：静默的猫和狗")


def print_file_content_silently(filename, animal_type):
    """尝试读取文件，文件不存在时静默失败。"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(f"--- {animal_type} ---")
            print(contents.rstrip())
    except FileNotFoundError:
        pass  # 静默失败


print_file_content_silently('chapter10/cats.txt', 'Cats')
print()
print_file_content_silently('chapter10/dogs.txt', 'Dogs')
print()
# 测试一个不存在的文件
print("Attempting to read a missing file (should fail silently)...")
print_file_content_silently('missing_file.txt', 'Unknown')
print("(No error message — silent failure works!)")

# =============================================================
# 练习 10.10：常见单词
# 读取古登堡计划的文本，计算 'the' 和 'the ' 的出现次数。
# =============================================================
print("=" * 50)
print("练习 10.10：常见单词")

book_filename = 'chapter10/sherlock_holmes.txt'

try:
    with open(book_filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Error: '{book_filename}' not found.")
else:
    # 统计单词 'the' 的出现次数（不区分大小写）
    count_the = contents.lower().count('the')
    # 统计 'the '（带空格）的出现次数
    count_the_space = contents.lower().count('the ')

    # 估算总单词数
    words = contents.split()
    total_words = len(words)

    print(f"Analyzing: {book_filename}")
    print(f"  Total words: {total_words}")
    print(f"  Occurrences of 'the' (any form): {count_the}")
    print(f"  Occurrences of 'the ' (with trailing space): {count_the_space}")
    print(f"  Difference: {count_the - count_the_space}")
    print(f"  (The difference includes words like 'then', 'there', 'them', etc.)")

# =============================================================
# 练习 10.11：喜欢的数
# 程序1：提示用户输入喜欢的数，用 json.dumps() 存储到文件。
# 程序2：从文件读取并打印消息。
# =============================================================
print("=" * 50)
print("练习 10.11：喜欢的数")

favorite_number_file = 'chapter10/favorite_number.json'


# --- 程序 1：存储喜欢的数 ---
def store_favorite_number():
    """提示用户输入喜欢的数并存储到 JSON 文件。"""
    number = input("What is your favorite number? ")
    with open(favorite_number_file, 'w') as f:
        json.dump(number, f)
    print(f"Your favorite number ({number}) has been saved!")
    return number


# --- 程序 2：读取喜欢的数 ---
def read_favorite_number():
    """从 JSON 文件读取喜欢的数并打印消息。"""
    try:
        with open(favorite_number_file) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


# 先存储
stored_number = store_favorite_number()

# 再读取
retrieved_number = read_favorite_number()
if retrieved_number:
    print(f"I know your favorite number! It's {retrieved_number}.")

# =============================================================
# 练习 10.12：记住喜欢的数
# 将两个程序合而为一：如果已存储就显示，否则提示输入并存储。
# =============================================================
print("=" * 50)
print("练习 10.12：记住喜欢的数")

favorite_number_file_v2 = 'chapter10/favorite_number_v2.json'


def remember_favorite_number():
    """记住用户喜欢的数：已存储则显示，否则提示输入。"""
    try:
        with open(favorite_number_file_v2) as f:
            number = json.load(f)
    except FileNotFoundError:
        number = input("What is your favorite number? ")
        with open(favorite_number_file_v2, 'w') as f:
            json.dump(number, f)
        print(f"Got it! I'll remember that your favorite number is {number}.")
    else:
        print(f"Welcome back! I remember your favorite number is {number}.")


# 第一次运行：文件不存在，提示输入
print("--- First run ---")
# 删除文件以确保第一次运行的效果
if os.path.exists(favorite_number_file_v2):
    os.remove(favorite_number_file_v2)
remember_favorite_number()

# 第二次运行：文件已存在，直接显示
print("\n--- Second run ---")
remember_favorite_number()

# =============================================================
# 练习 10.13：用户字典
# 扩展 remember_me.py，收集多项用户信息并存入字典。
# 用 json.dumps() 和 json.loads() 读写。
# =============================================================
print("=" * 50)
print("练习 10.13：用户字典")

user_info_file = 'chapter10/user_info.json'


def store_user_info():
    """提示用户输入多项信息，存入字典并写入 JSON 文件。"""
    username = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where do you live? ")

    user_dict = {
        'username': username,
        'age': age,
        'location': location,
    }

    with open(user_info_file, 'w') as f:
        json.dump(user_dict, f)

    return user_dict


def read_user_info():
    """从 JSON 文件读取用户信息。"""
    try:
        with open(user_info_file) as f:
            user_dict = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_dict


# 先存储
print("--- Storing user info ---")
user_info = store_user_info()

# 再读取
print("\n--- Reading user info ---")
retrieved_user = read_user_info()
if retrieved_user:
    print(f"I remember the following about you:")
    print(f"  Name: {retrieved_user['username']}")
    print(f"  Age: {retrieved_user['age']}")
    print(f"  Location: {retrieved_user['location']}")

# =============================================================
# 练习 10.14：验证用户
# 修改 remember_me.py，在欢迎用户回来之前验证用户名是否正确。
# 如果不对就让用户输入正确的用户名。
# =============================================================
print("=" * 50)
print("练习 10.14：验证用户")

verify_user_file = 'chapter10/verify_username.json'


def get_stored_username():
    """获取已存储的用户名。"""
    try:
        with open(verify_user_file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入新的用户名并存储。"""
    username = input("What is your name? ")
    with open(verify_user_file, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并在欢迎之前验证身份。"""
    username = get_stored_username()
    if username:
        # 验证当前用户是否就是上次的用户
        print(f"Are you {username}?")
        answer = input("Enter 'yes' if this is correct, or 'no' to change: ")
        if answer.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


# 模拟两次运行
print("--- First run (no stored user) ---")
if os.path.exists(verify_user_file):
    os.remove(verify_user_file)
greet_user()

print("\n--- Second run (user already stored) ---")
greet_user()
