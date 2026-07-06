# ---------------------------------------------------------------
# 文件名：chapter8_functions.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第8章所有练习
#           涵盖函数的定义、形参、实参、返回值、模块导入等。
# ---------------------------------------------------------------

# =============================================================
# 练习 8.1：消息
# 编写 display_message() 函数，打印本章主题。
# =============================================================
print("=" * 50)
print("练习 8.1：消息")


def display_message():
    """打印本章的主题。"""
    print("In this chapter, I am learning about functions in Python.")


display_message()
# =============================================================
# 练习 8.2：喜欢的书
# 编写 favorite_book() 函数，接受书名形参并打印消息。
# =============================================================
print("=" * 50)
print("练习 8.2：喜欢的书")


def favorite_book(title):
    """打印一条关于喜欢的书的消息。"""
    print(f"One of my favorite books is {title}.")


favorite_book("Alice in Wonderland")
# =============================================================
# 练习 8.3：T 恤
# 编写 make_shirt() 函数，接受尺码和字样。
# =============================================================
print("=" * 50)
print("练习 8.3：T 恤")


def make_shirt(size, message):
    """打印 T 恤的尺码和字样。"""
    print(f"T-shirt size: {size}, message: \"{message}\"")


# 位置实参
make_shirt("M", "Hello World!")

# 关键字实参
make_shirt(size="L", message="Python Rocks!")
# =============================================================
# 练习 8.4：大号 T 恤
# 修改 make_shirt()，默认大号且字样为 "I love Python"。
# =============================================================
print("=" * 50)
print("练习 8.4：大号 T 恤")


def make_shirt(size="L", message="I love Python"):
    """打印 T 恤的尺码和字样（默认为大号 + I love Python）。"""
    print(f"T-shirt size: {size}, message: \"{message}\"")


# 默认字样的大号 T 恤
make_shirt()

# 默认字样的中号 T 恤
make_shirt("M")

# 其他字样的 T 恤
make_shirt("S", "Code is Poetry")

# 使用关键字实参
make_shirt(message="Keep Calm and Code On", size="XL")
# =============================================================
# 练习 8.5：城市
# 编写 describe_city() 函数，国家形参有默认值。
# =============================================================
print("=" * 50)
print("练习 8.5：城市")


def describe_city(city, country="China"):
    """打印城市及其所属国家的句子。"""
    print(f"{city} is in {country}.")


describe_city("Beijing")
describe_city("Shanghai")
describe_city("Reykjavik", "Iceland")
# =============================================================
# 练习 8.6：城市名
# 编写 city_country() 函数，返回格式化的字符串。
# =============================================================
print("=" * 50)
print("练习 8.6：城市名")


def city_country(city, country):
    """返回 'City, Country' 格式的字符串。"""
    return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))
# =============================================================
# 练习 8.7：专辑
# 编写 make_album() 函数，返回包含歌手和专辑名的字典。
# =============================================================
print("=" * 50)
print("练习 8.7：专辑")


def make_album(artist, album, num_songs=None):
    """返回一个描述音乐专辑的字典。
    包含歌手名、专辑名，可选的歌曲数量。
    """
    album_dict = {
        'artist': artist,
        'album': album,
    }
    if num_songs is not None:
        album_dict['num_songs'] = num_songs
    return album_dict


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album("The Beatles", "Abbey Road")
album4 = make_album("Pink Floyd", "The Dark Side of the Moon", 10)

print(album1)
print(album2)
print(album3)
print(album4)
# =============================================================
# 练习 8.8：用户的专辑
# 使用 while 循环让用户输入专辑信息，调用 make_album()。
# =============================================================
print("=" * 50)
print("练习 8.8：用户的专辑")


def make_album(artist, album, num_songs=None):
    """返回一个描述音乐专辑的字典。"""
    album_dict = {
        'artist': artist,
        'album': album,
    }
    if num_songs is not None:
        album_dict['num_songs'] = num_songs
    return album_dict


while True:
    print("\nPlease enter album information (enter 'q' at any time to quit):")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    album = input("Album name: ")
    if album == 'q':
        break

    songs_input = input("Number of songs (press Enter to skip): ")
    if songs_input == 'q':
        break

    if songs_input:
        result = make_album(artist, album, int(songs_input))
    else:
        result = make_album(artist, album)

    print(f"\nAlbum created: {result}")

print("Goodbye!")
# =============================================================
# 练习 8.9：消息
# 将列表传递给 show_messages() 函数打印每条消息。
# =============================================================
print("=" * 50)
print("练习 8.9：消息")


def show_messages(messages):
    """打印列表中的每条文本消息。"""
    for message in messages:
        print(message)


text_messages = [
    "Hello, how are you?",
    "Don't forget to bring your book.",
    "See you at the meeting at 3pm.",
    "Happy birthday to you!",
]

show_messages(text_messages)
# =============================================================
# 练习 8.10：发送消息
# send_messages() 打印每条消息并移动到 sent_messages 列表。
# =============================================================
print("=" * 50)
print("练习 8.10：发送消息")


def send_messages(messages, sent):
    """打印每条消息，并将其从原列表移到 sent 列表。"""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent.append(current_message)


text_messages = [
    "Hello, how are you?",
    "Don't forget to bring your book.",
    "See you at the meeting at 3pm.",
    "Happy birthday to you!",
]
sent_messages = []

send_messages(text_messages, sent_messages)

print(f"\ntext_messages: {text_messages}")
print(f"sent_messages: {sent_messages}")
# =============================================================
# 练习 8.11：消息归档
# 向 send_messages() 传递列表的副本，保留原始列表。
# =============================================================
print("=" * 50)
print("练习 8.11：消息归档")


def send_messages(messages, sent):
    """打印每条消息，并将其从原列表移到 sent 列表。"""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent.append(current_message)


text_messages = [
    "Hello, how are you?",
    "Don't forget to bring your book.",
    "See you at the meeting at 3pm.",
    "Happy birthday to you!",
]
sent_messages = []

# 传递列表的副本 [:]
send_messages(text_messages[:], sent_messages)

print(f"\ntext_messages (original, unchanged): {text_messages}")
print(f"sent_messages: {sent_messages}")
# =============================================================
# 练习 8.12：三明治
# 编写函数接受任意数量的食材，打印三明治概述。
# =============================================================
print("=" * 50)
print("练习 8.12：三明治")


def make_sandwich(*toppings):
    """打印顾客点的三明治的概述。"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"  - {topping}")


make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato", "mayo")
make_sandwich("peanut butter", "jelly")
# =============================================================
# 练习 8.13：用户简介
# 复制 user_profile.py 并调用 build_profile() 创建自己的简介。
# =============================================================
print("=" * 50)
print("练习 8.13：用户简介")


def build_profile(first, last, **user_info):
    """创建一个字典，包含用户的所有信息。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'San', 'Zhang',
    location='Beijing',
    field='Computer Science',
    hobby='Reading',
)

print(my_profile)
# =============================================================
# 练习 8.14：汽车
# 编写函数存储汽车信息，接受制造商、型号和任意关键字实参。
# =============================================================
print("=" * 50)
print("练习 8.14：汽车")


def make_car(manufacturer, model, **car_info):
    """将汽车信息存储在字典中并返回。"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car2 = make_car('honda', 'accord', year=2023, color='silver', sunroof=True)
print(car2)
# =============================================================
# 练习 8.15：打印模型
# 将函数放入 printing_functions.py 模块，再导入使用。
# =============================================================
print("=" * 50)
print("练习 8.15：打印模型")

import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs[:], completed_models)
printing_functions.show_completed_models(completed_models)
# =============================================================
# 练习 8.16：导入
# 使用多种方式导入同一个函数并调用。
# =============================================================
print("=" * 50)
print("练习 8.16：导入")

# 方式 1: import module_name
print("\n--- 方式 1: import module_name ---")
import greeting

greeting.say_hello("Alice")

# 方式 2: from module_name import function_name
print("\n--- 方式 2: from module_name import function_name ---")
from greeting import say_hello

say_hello("Bob")

# 方式 3: from module_name import function_name as fn
print("\n--- 方式 3: from module_name import function_name as fn ---")
from greeting import say_hello as sh

sh("Charlie")

# 方式 4: import module_name as mn
print("\n--- 方式 4: import module_name as mn ---")
import greeting as gt

gt.say_hello("Diana")

# 方式 5: from module_name import *
print("\n--- 方式 5: from module_name import * ---")
from greeting import *

say_hello("Eve")
# =============================================================
# 练习 8.17：函数编写指南
# 选择三个程序，确保遵循函数编写指南。
# =============================================================
print("=" * 50)
print("练习 8.17：函数编写指南")

print("""
已审查以下三个函数，确认它们遵循了编写指南：

【审查项清单】
  [OK] 函数名只包含小写字母和下划线
  [OK] 函数名具有描述性
  [OK] 每个函数都包含简要阐述其功能的文档字符串
  [OK] 形参和实参的长度合适（不超过 79 字符）
  [OK] 程序中对函数的所有调用都包含实参
  [OK] 函数定义之间用两个空行分隔

--- 审查的函数 ---
1. make_album()        — 练习 8.7：接受歌手/专辑名，返回字典
2. build_profile()     — 练习 8.13：接受姓名和任意关键字实参
3. make_car()          — 练习 8.14：接受制造商/型号和任意关键字实参

审查结果：以上三个函数均符合 PEP 8 函数编写指南，
         包括命名规范、文档字符串、合理形参数量和清晰的逻辑结构。
""")
