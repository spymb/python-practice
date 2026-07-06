# ---------------------------------------------------------------
# 文件名：chapter7_user_input_while_loops.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第7章所有练习
#           涵盖用户输入、while循环、break、列表操作等。
# ---------------------------------------------------------------

# =============================================================
# 练习 7.1：汽车租赁
# 询问用户要租什么样的汽车，并打印一条消息。
# =============================================================
print("=" * 50)
print("练习 7.1：汽车租赁")

car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car}.")
# =============================================================
# 练习 7.2：餐馆订位
# 询问用户有多少人用餐，判断是否有空桌。
# =============================================================
print("=" * 50)
print("练习 7.2：餐馆订位")

num_people = int(input("How many people are in your dinner group? "))
if num_people > 8:
    print("Sorry, there is no available table for your group.")
else:
    print("Great, we have a table available for you!")
# =============================================================
# 练习 7.3：10 的整数倍
# 让用户输入一个数，并指出这个数是否是 10 的整数倍。
# =============================================================
print("=" * 50)
print("练习 7.3：10 的整数倍")

number = int(input("Please enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
# =============================================================
# 练习 7.4：比萨配料
# 循环提示用户输入配料，输入 'quit' 时结束。
# =============================================================
print("=" * 50)
print("练习 7.4：比萨配料")

prompt = "\nPlease enter a pizza topping (enter 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"We'll add {topping} to your pizza.")
# =============================================================
# 练习 7.5：电影票
# 根据观众年龄收取不同票价，使用循环询问。
# =============================================================
print("=" * 50)
print("练习 7.5：电影票")

prompt = "\nPlease enter your age (enter 'quit' to finish): "

while True:
    age_input = input(prompt)
    if age_input == 'quit':
        break
    age = int(age_input)
    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
# =============================================================
# 练习 7.6：三种出路
# 以三种不同的方式控制循环结束。
# =============================================================
print("=" * 50)
print("练习 7.6：三种出路")

# 方式 1：在 while 循环中使用条件测试来结束循环
print("\n--- 方式 1：使用条件测试 ---")
topping = ""
while topping != 'quit':
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    if topping != 'quit':
        print(f"We'll add {topping} to your pizza.")

# 方式 2：使用变量 active 来控制循环结束的时机
print("\n--- 方式 2：使用 active 变量 ---")
active = True
while active:
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    if topping == 'quit':
        active = False
    else:
        print(f"We'll add {topping} to your pizza.")

# 方式 3：使用 break 语句在用户输入 'quit' 时退出循环
print("\n--- 方式 3：使用 break 语句 ---")
while True:
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"We'll add {topping} to your pizza.")
# =============================================================
# 练习 7.7：无限循环
# 编写一个没完没了的循环，并运行它。
# =============================================================
print("=" * 50)
print("练习 7.7：无限循环")

# 下面的代码是一个无限循环。要结束它，请按 Ctrl + C。
# 此处已注释掉，如需运行请取消注释。
# while True:
#     print("This is an infinite loop! Press Ctrl + C to stop.")

print("无限循环示例已注释掉，运行将不会进入死循环。")
print("如需体验，请取消代码中的注释后重新运行。")
# =============================================================
# 练习 7.8：熟食店
# 遍历三明治订单列表，制作后将订单移到已完成列表。
# =============================================================
print("=" * 50)
print("练习 7.8：熟食店")

sandwich_orders = ['tuna', 'chicken', 'ham', 'veggie', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")
# =============================================================
# 练习 7.9：五香烟熏牛肉卖完了
# 删除 sandwich_orders 中所有的 'pastrami'。
# =============================================================
print("=" * 50)
print("练习 7.9：五香烟熏牛肉卖完了")

sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'chicken',
    'ham', 'pastrami', 'veggie', 'turkey',
]
finished_sandwiches = []

print("Sorry, we have run out of pastrami today.\n")

# 删除所有的 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 制作剩余的三明治
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"  - {sandwich}")
# =============================================================
# 练习 7.10：梦想中的度假胜地
# 调查用户梦想中的度假胜地，并打印结果。
# =============================================================
print("=" * 50)
print("练习 7.10：梦想中的度假胜地")

responses = {}

polling_active = True

while polling_active:
    # 询问用户名
    name = input("\nWhat is your name? ")
    # 询问梦想中的度假胜地
    place = input("If you could visit one place in the world, where would you go? ")

    # 存储回答
    responses[name] = place

    # 询问是否继续
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# 打印调查结果
print("\n--- Dream Vacation Survey Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
