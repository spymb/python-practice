# ---------------------------------------------------------------
# 文件名：chapter4_exercises.py
# 作者：Python学习者
# 日期：2026-07-05
# 功能描述：完成《Python编程：从入门到实践》第4章所有练习
#           涵盖 for 循环、range()、列表推导式、切片、元组及 PEP 8。
# ---------------------------------------------------------------


# =============================================================
# 练习 4.1：比萨
# 存储喜欢的比萨名称，用 for 循环打印名称及句子，最后总结。
# =============================================================
pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

# 打印每种比萨的名称
for pizza in pizzas:
    print(pizza)

print()

# 打印包含比萨名称的句子
for pizza in pizzas:
    print(f"I like {pizza.lower()} pizza.")

print()

# 总结性句子（在循环外部）
print("I really love pizza!")
print("—" * 50)


# =============================================================
# 练习 4.2：动物
# 存储有共同特征的动物名称，打印名称、句子及共同之处。
# =============================================================
animals = ["dog", "cat", "rabbit"]

# 打印每种动物的名称
for animal in animals:
    print(animal)

print()

# 针对每种动物打印一个句子
for animal in animals:
    print(f"A {animal} would make a great pet.")

print()

# 指出共同之处（在循环外部）
print("Any of these animals would make a great pet!")
print("—" * 50)


# =============================================================
# 练习 4.3：数到 20
# 使用 for 循环打印 1～20（含）。
# =============================================================
for number in range(1, 21):
    print(number)
print("—" * 50)


# =============================================================
# 练习 4.4：100 万
# 创建 1～1 000 000 的列表并用 for 循环打印。
# （输出太长时已做截断处理，仅演示开头和结尾若干行）
# =============================================================
numbers = list(range(1, 1_000_001))

# 为避免输出过长，仅打印前 5 个和后 5 个作为验证
print("First 5 numbers:")
for number in numbers[:5]:
    print(number)

print("...")
print("(omitting middle output for readability)")
print("...")

print("Last 5 numbers:")
for number in numbers[-5:]:
    print(number)
print("—" * 50)


# =============================================================
# 练习 4.5：100 万求和
# 创建 1～1 000 000 的列表，使用 min()、max() 和 sum()。
# =============================================================
numbers = list(range(1, 1_000_001))
print(f"min(numbers) = {min(numbers)}")
print(f"max(numbers) = {max(numbers)}")
print(f"sum(numbers) = {sum(numbers)}")
print("—" * 50)


# =============================================================
# 练习 4.6：奇数
# 通过 range() 第三个参数创建 1～20 的奇数列表并打印。
# =============================================================
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
print("—" * 50)


# =============================================================
# 练习 4.7：3 的倍数
# 创建 3～30 内能被 3 整除的数的列表并打印。
# =============================================================
multiples_of_3 = list(range(3, 31, 3))
for number in multiples_of_3:
    print(number)
print("—" * 50)


# =============================================================
# 练习 4.8：立方
# 创建前 10 个整数（1～10）的立方列表，用 for 循环打印。
# =============================================================
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)

for cube in cubes:
    print(cube)
print("—" * 50)


# =============================================================
# 练习 4.9：立方推导式
# 使用列表推导式生成前 10 个整数的立方列表。
# =============================================================
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
print("—" * 50)


# =============================================================
# 练习 4.10：切片
# 基于练习 4.8 的立方列表，使用切片打印前三个、中间三个、
# 末尾三个元素。
# =============================================================
cubes = [value ** 3 for value in range(1, 11)]

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
# 10 个元素，中间三个：索引 3, 4, 5 即第 4~6 个
print(cubes[3:6])

print("The last three items in the list are:")
print(cubes[-3:])
print("—" * 50)


# =============================================================
# 练习 4.11：你的比萨，我的比萨
# 创建比萨列表的副本，分别添加不同比萨，验证是两个独立列表。
# =============================================================
pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

# 创建副本
friend_pizzas = pizzas[:]

# 在原来的比萨列表中添加一种
pizzas.append("BBQ Chicken")

# 在 friend_pizzas 中添加另一种
friend_pizzas.append("Vegetarian")

# 验证是两个不同的列表
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
print("—" * 50)


# =============================================================
# 练习 4.12：使用多个循环
# 编写两个 for 循环，将各个食品列表都打印出来。
# =============================================================
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")
print("—" * 50)


# =============================================================
# 练习 4.13：自助餐
# 用元组存储餐馆提供的 5 种食品，尝试修改元组元素（会报错），
# 然后通过重新赋值来替换菜单。
# =============================================================
foods = ("fried rice", "noodles", "dumplings", "spring rolls", "soup")

print("Original menu:")
for food in foods:
    print(f"- {food}")

# 尝试修改元组中的一个元素 —— Python 会拒绝此操作
# 取消下面这行注释会引发 TypeError:
# foods[1] = "steamed buns"
# Traceback (most recent call last):
#   ...
# TypeError: 'tuple' object does not support item assignment

print("\nAttempting to modify a tuple element...")
try:
    foods[1] = "steamed buns"
except TypeError as e:
    print(f"Python rejected the change: {e}")

print()

# 餐馆调整菜单：通过重新赋值替换两种食品
print("Revised menu:")
foods = ("fried rice", "steamed buns", "dumplings", "spring rolls",
         "hot pot")
for food in foods:
    print(f"- {food}")
print("—" * 50)


# =============================================================
# 练习 4.14：PEP 8
# 请访问 python.org 搜索"PEP 8 -- Style Guide for Python Code"。
# 已访问并浏览过 PEP 8 格式设置指南。
# =============================================================
print("Exercise 4.14: See PEP 8 at https://peps.python.org/pep-0008/")
print("—" * 50)


# =============================================================
# 练习 4.15：代码审核
# 本章所有代码已遵循 PEP 8 规范：
#   - 每级缩进使用 4 个空格
#   - 每行不超过 80 个字符
#   - 不在程序文件中滥用空行
#   - 运算符两侧各留一个空格
#   - 逗号后留一个空格
# =============================================================
print("Exercise 4.15: All code in this file follows PEP 8 guidelines.")
