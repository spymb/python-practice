# ---------------------------------------------------------------
# 文件名：chapter6_dictionaries.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第6章所有练习
#           涵盖字典的创建、访问、遍历、嵌套及其应用。
# ---------------------------------------------------------------

# =============================================================
# 练习 6.1：人
# 用字典存储一个人的信息，并打印每项信息。
# =============================================================
print("=" * 50)
print("练习 6.1：人")

person = {
    'first_name': 'San',
    'last_name': 'Zhang',
    'age': 28,
    'city': 'Beijing',
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
# =============================================================
# 练习 6.2：喜欢的数 1
# 用字典存储 5 个人的名字及其喜欢的数字，并打印。
# =============================================================
print("=" * 50)
print("练习 6.2：喜欢的数 1")

favorite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 13,
    'Diana': 8,
    'Eve': 3,
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
# =============================================================
# 练习 6.3：词汇表 1
# 创建 5 个编程术语的词汇表，并整洁地打印每个术语及其含义。
# =============================================================
print("=" * 50)
print("练习 6.3：词汇表 1")

glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'list': 'An ordered, mutable collection of items.',
    'dictionary': 'A collection of key-value pairs, allowing fast lookup by key.',
    'loop': 'A control structure that repeats a block of code multiple times.',
    'function': 'A named block of reusable code that performs a specific task.',
}

for term, meaning in glossary.items():
    print(f"{term}:\n\t{meaning}\n")
# =============================================================
# 练习 6.4：词汇表 2
# 将 print 调用替换为遍历循环，并再添加 5 个术语。
# =============================================================
print("=" * 50)
print("练习 6.4：词汇表 2")

glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'list': 'An ordered, mutable collection of items.',
    'dictionary': 'A collection of key-value pairs, allowing fast lookup by key.',
    'loop': 'A control structure that repeats a block of code multiple times.',
    'function': 'A named block of reusable code that performs a specific task.',
    'string': 'A sequence of characters, enclosed in quotes.',
    'integer': 'A whole number without a decimal point.',
    'boolean': 'A data type with only two possible values: True or False.',
    'tuple': 'An ordered, immutable collection of items.',
    'conditional test': 'An expression that evaluates to True or False.',
}

for term, meaning in glossary.items():
    print(f"{term}:\n\t{meaning}\n")
# =============================================================
# 练习 6.5：河流
# 用字典存储三条河流及其流经的国家，分别打印河流和国家。
# =============================================================
print("=" * 50)
print("练习 6.5：河流")

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

# 打印每条河流的消息
print("--- 河流与国家 ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 打印每条河流的名字
print("\n--- 河流列表 ---")
for river in rivers.keys():
    print(river.title())

# 打印每个国家的名字
print("\n--- 国家列表 ---")
for country in rivers.values():
    print(country.title())
# =============================================================
# 练习 6.6：调查
# 模拟 favorite_languages 调查，对已参与和未参与的人分别处理。
# =============================================================
print("=" * 50)
print("练习 6.6：调查")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# 应该接受调查的名单（有些人在字典中，有些人不在）
people_to_poll = ['jen', 'mike', 'sarah', 'tom', 'phil', 'lisa']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thank you, {name.title()}, for responding to the poll!")
    else:
        print(f"Hi {name.title()}, would you like to take our language poll?")
# =============================================================
# 练习 6.7：人们
# 创建三个表示人的字典，将它们存入列表 people 中并遍历。
# =============================================================
print("=" * 50)
print("练习 6.7：人们")

person_1 = {
    'first_name': 'San',
    'last_name': 'Zhang',
    'age': 28,
    'city': 'Beijing',
}

person_2 = {
    'first_name': 'Si',
    'last_name': 'Li',
    'age': 24,
    'city': 'Shanghai',
}

person_3 = {
    'first_name': 'Wu',
    'last_name': 'Wang',
    'age': 30,
    'city': 'Guangzhou',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Name: {full_name}")
    print(f"  Age: {person['age']}")
    print(f"  City: {person['city']}\n")
# =============================================================
# 练习 6.8：宠物
# 创建多个宠物字典，存入列表 pets 中并遍历打印所有信息。
# =============================================================
print("=" * 50)
print("练习 6.8：宠物")

pet_1 = {
    'type': 'dog',
    'owner': 'Alice',
}

pet_2 = {
    'type': 'cat',
    'owner': 'Bob',
}

pet_3 = {
    'type': 'hamster',
    'owner': 'Charlie',
}

pet_4 = {
    'type': 'parrot',
    'owner': 'Diana',
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['type']}.")
# =============================================================
# 练习 6.9：喜欢的地方
# 用字典存储三个人及其喜欢的 1~3 个地方，遍历并打印。
# =============================================================
print("=" * 50)
print("练习 6.9：喜欢的地方")

favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['London', 'Sydney'],
    'Charlie': ['Barcelona', 'Prague', 'Kyoto'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name}'s favorite place is:")
    else:
        print(f"{name}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
    print()
# =============================================================
# 练习 6.10：喜欢的数 2
# 修改练习 6.2，让每人可以有多个喜欢的数。
# =============================================================
print("=" * 50)
print("练习 6.10：喜欢的数 2")

favorite_numbers = {
    'Alice': [7, 21, 42],
    'Bob': [3, 14],
    'Charlie': [13, 99],
    'Diana': [8, 16, 24, 32],
    'Eve': [1],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name}'s favorite number is: {numbers[0]}")
    else:
        print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}")
# =============================================================
# 练习 6.11：城市
# 用嵌套字典存储三座城市的信息（所属国家、人口约数、事实）。
# =============================================================
print("=" * 50)
print("练习 6.11：城市")

cities = {
    'Beijing': {
        'country': 'China',
        'population': '21.5 million',
        'fact': 'Beijing has been the capital of China for over 800 years.',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
    },
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Paris is known as the City of Light.',
    },
}

for city, info in cities.items():
    print(f"--- {city} ---")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
# =============================================================
# 练习 6.12：扩展
# 对本章的一个示例进行扩展：改进输出格式或添加新功能。
# =============================================================
print("=" * 50)
print("练习 6.12：扩展")

# 扩展练习 6.11：添加更丰富的城市信息
# 新增 continent 和 landmarks 字段，并改进输出格式

cities_extended = {
    'Beijing': {
        'country': 'China',
        'continent': 'Asia',
        'population': '21.5 million',
        'fact': 'Beijing has been the capital of China for over 800 years.',
        'landmarks': ['Great Wall', 'Forbidden City', 'Summer Palace'],
    },
    'Tokyo': {
        'country': 'Japan',
        'continent': 'Asia',
        'population': '14 million',
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
        'landmarks': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing'],
    },
    'Paris': {
        'country': 'France',
        'continent': 'Europe',
        'population': '2.1 million',
        'fact': 'Paris is known as the City of Light.',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'],
    },
}

print("=== 世界城市指南 ===\n")

for city, info in cities_extended.items():
    print(f"[ {city} ]")
    print(f"  Location: {info['country']} ({info['continent']})")
    print(f"  Population: {info['population']}")
    print(f"  Did you know? {info['fact']}")
    print(f"  Famous landmarks: {', '.join(info['landmarks'])}")
    print()
