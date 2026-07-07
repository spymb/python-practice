# ---------------------------------------------------------------
# 文件名：chapter9_classes.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：完成《Python编程：从入门到实践》第9章所有练习
#           涵盖类的创建、属性、方法、继承、导入以及骰子与彩票。
# ---------------------------------------------------------------

# =============================================================
# 练习 9.1：餐馆
# 创建 Restaurant 类，包含属性 restaurant_name 和 cuisine_type，
# 以及方法 describe_restaurant() 和 open_restaurant()。
# =============================================================
print("=" * 50)
print("练习 9.1：餐馆")


class Restaurant:
    """一个简单的餐馆类。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆的信息。"""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """打印餐馆正在营业的消息。"""
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant('Happy Dumpling', 'Chinese')
print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# =============================================================
# 练习 9.2：三家餐馆
# 根据练习 9.1 的类创建三个实例，并调用 describe_restaurant()。
# =============================================================
print("=" * 50)
print("练习 9.2：三家餐馆")

restaurant_1 = Restaurant('Golden Pizza', 'Italian')
restaurant_2 = Restaurant('Sakura Sushi', 'Japanese')
restaurant_3 = Restaurant('Spicy Kingdom', 'Sichuan')

print("--- Restaurant 1 ---")
restaurant_1.describe_restaurant()
print("\n--- Restaurant 2 ---")
restaurant_2.describe_restaurant()
print("\n--- Restaurant 3 ---")
restaurant_3.describe_restaurant()

# =============================================================
# 练习 9.3：用户
# 创建 User 类，包含 first_name、last_name 等属性，
# 以及 describe_user() 和 greet_user() 方法。
# =============================================================
print("=" * 50)
print("练习 9.3：用户")


class User:
    """一个简单的用户类。"""

    def __init__(self, first_name, last_name, age, location, email):
        """初始化用户的属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        """打印用户信息摘要。"""
        print(f"User Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Location: {self.location}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"Hello, {self.first_name} {self.last_name}! "
              f"Welcome back!")


user_1 = User('Alice', 'Wang', 25, 'Shanghai', 'alice@example.com')
user_2 = User('Bob', 'Li', 30, 'Beijing', 'bob@example.com')
user_3 = User('Charlie', 'Zhang', 28, 'Shenzhen', 'charlie@example.com')

print("--- User 1 ---")
user_1.describe_user()
user_1.greet_user()
print("\n--- User 2 ---")
user_2.describe_user()
user_2.greet_user()
print("\n--- User 3 ---")
user_3.describe_user()
user_3.greet_user()

# =============================================================
# 练习 9.4：就餐人数
# 添加 number_served 属性（默认值 0），
# 添加 set_number_served() 和 increment_number_served() 方法。
# =============================================================
print("=" * 50)
print("练习 9.4：就餐人数")


class RestaurantV2:
    """带有就餐人数管理的餐馆类。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆的信息。"""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """打印餐馆正在营业的消息。"""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """设置就餐人数。"""
        self.number_served = number

    def increment_number_served(self, number):
        """让就餐人数递增。"""
        self.number_served += number


restaurant_v2 = RestaurantV2('Happy Dumpling', 'Chinese')
print(f"Number served initially: {restaurant_v2.number_served}")

restaurant_v2.number_served = 10
print(f"Number served after manual change: {restaurant_v2.number_served}")

restaurant_v2.set_number_served(50)
print(f"Number served after set_number_served(50): {restaurant_v2.number_served}")

restaurant_v2.increment_number_served(30)
print(f"Number served after increment_number_served(30): {restaurant_v2.number_served}")

# =============================================================
# 练习 9.5：尝试登录次数
# 在 User 类中添加 login_attempts 属性，
# 添加 increment_login_attempts() 和 reset_login_attempts() 方法。
# =============================================================
print("=" * 50)
print("练习 9.5：尝试登录次数")


class UserV2:
    """带有登录次数管理的用户类。"""

    def __init__(self, first_name, last_name, age, location, email):
        """初始化用户的属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要。"""
        print(f"User Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Location: {self.location}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"Hello, {self.first_name} {self.last_name}! "
              f"Welcome back!")

    def increment_login_attempts(self):
        """将登录尝试次数加 1。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录尝试次数重置为 0。"""
        self.login_attempts = 0


user_v2 = UserV2('Alice', 'Wang', 25, 'Shanghai', 'alice@example.com')

# 多次递增登录尝试次数
user_v2.increment_login_attempts()
user_v2.increment_login_attempts()
user_v2.increment_login_attempts()
print(f"Login attempts after 3 increments: {user_v2.login_attempts}")

user_v2.increment_login_attempts()
user_v2.increment_login_attempts()
print(f"Login attempts after 2 more increments: {user_v2.login_attempts}")

# 重置登录尝试次数
user_v2.reset_login_attempts()
print(f"Login attempts after reset: {user_v2.login_attempts}")

# =============================================================
# 练习 9.6：冰激凌小店
# 创建 IceCreamStand 类继承 RestaurantV2，
# 添加 flavors 属性和显示口味的方法。
# =============================================================
print("=" * 50)
print("练习 9.6：冰激凌小店")


class IceCreamStand(RestaurantV2):
    """冰激凌小店类，继承自 RestaurantV2。"""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """初始化冰激凌小店的属性。"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mango', 'green tea']

    def display_flavors(self):
        """显示所有冰激凌口味。"""
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"  - {flavor.title()}")


ice_cream_stand = IceCreamStand('Cool Treats')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

# =============================================================
# 练习 9.7：管理员
# 创建 Admin 类继承 UserV2，添加 privileges 属性和 show_privileges() 方法。
# =============================================================
print("=" * 50)
print("练习 9.7：管理员")


class Admin(UserV2):
    """管理员类，继承自 UserV2。"""

    def __init__(self, first_name, last_name, age, location, email):
        """初始化管理员的属性。"""
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            'can edit post',
            'can moderate comments',
        ]

    def show_privileges(self):
        """显示管理员的权限列表。"""
        print(f"Admin {self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


admin = Admin('David', 'Chen', 35, 'Beijing', 'david@admin.com')
admin.describe_user()
admin.show_privileges()

# =============================================================
# 练习 9.8：权限
# 创建 Privileges 类，将 show_privileges() 方法移到该类中。
# 在 Admin 类中将 Privileges 实例用作属性。
# =============================================================
print("=" * 50)
print("练习 9.8：权限")


class Privileges:
    """权限类，存储用户的权限列表。"""

    def __init__(self):
        """初始化权限列表。"""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            'can edit post',
            'can moderate comments',
        ]

    def show_privileges(self):
        """显示权限列表。"""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


class AdminV2(UserV2):
    """改进的管理员类，使用 Privileges 实例作为属性。"""

    def __init__(self, first_name, last_name, age, location, email):
        """初始化管理员的属性。"""
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()


admin_v2 = AdminV2('Eva', 'Liu', 32, 'Guangzhou', 'eva@admin.com')
admin_v2.describe_user()
admin_v2.privileges.show_privileges()

# =============================================================
# 练习 9.9：电池升级
# 给 Battery 类添加 upgrade_battery() 方法，
# 如果容量不是 65 就设为 65。
# =============================================================
print("=" * 50)
print("练习 9.9：电池升级")


class Car:
    """一个简单的汽车类。"""

    def __init__(self, make, model, year):
        """初始化汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称。"""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """打印汽车的里程。"""
        print(f"This car has {self.odometer_reading} miles on it.")


class Battery:
    """电动汽车的电池类。"""

    def __init__(self, battery_size=40):
        """初始化电池的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印描述电池容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印电池的续航里程。"""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        else:
            range_miles = int(self.battery_size * 3.5)

        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """升级电池：如果容量不是 65，就设为 65。"""
        if self.battery_size != 65:
            print(f"Upgrading battery from {self.battery_size}-kWh to 65-kWh...")
            self.battery_size = 65
        else:
            print("Battery is already at 65-kWh, no upgrade needed.")


class ElectricCar(Car):
    """电动汽车类，继承自 Car。"""

    def __init__(self, make, model, year):
        """初始化电动汽车的属性。"""
        super().__init__(make, model, year)
        self.battery = Battery()


# 创建默认电池容量（40）的电动汽车
my_electric_car = ElectricCar('Tesla', 'Model 3', 2024)
print(my_electric_car.get_descriptive_name())

# 升级前查询续航
my_electric_car.battery.get_range()

# 升级电池
my_electric_car.battery.upgrade_battery()

# 升级后查询续航
my_electric_car.battery.get_range()

# =============================================================
# 练习 9.13：骰子
# 创建 Die 类，包含 sides 属性（默认 6），
# 编写 roll_die() 方法打印 1 到面数之间的随机数。
# =============================================================
print("=" * 50)
print("练习 9.13：骰子")

import random


class Die:
    """一个简单的骰子类。"""

    def __init__(self, sides=6):
        """初始化骰子的面数。"""
        self.sides = sides

    def roll_die(self):
        """掷骰子，返回 1 到 sides 之间的随机数。"""
        return random.randint(1, self.sides)


# 创建 6 面骰子并掷 10 次
die_6 = Die()
print("Rolling a 6-sided die 10 times:")
results = [str(die_6.roll_die()) for _ in range(10)]
print("  " + " ".join(results))

# 创建 10 面骰子并掷 10 次
die_10 = Die(10)
print("\nRolling a 10-sided die 10 times:")
results = [str(die_10.roll_die()) for _ in range(10)]
print("  " + " ".join(results))

# 创建 20 面骰子并掷 10 次
die_20 = Die(20)
print("\nRolling a 20-sided die 10 times:")
results = [str(die_20.roll_die()) for _ in range(10)]
print("  " + " ".join(results))

# =============================================================
# 练习 9.14：彩票
# 从包含 10 个数字和 5 个字母的列表中随机选择 4 个，
# 中奖条件是这 4 个值全部匹配。
# =============================================================
print("=" * 50)
print("练习 9.14：彩票")

# 创建彩票池：10 个数 + 5 个字母
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 随机选择 4 个
winning_ticket = random.sample(lottery_pool, 4)
print("The lottery pool is:", lottery_pool)
print(f"Any ticket matching these 4 items wins the grand prize: {winning_ticket}")

# =============================================================
# 练习 9.15：彩票分析
# 不断随机抽取，直到中奖为止，并报告尝试次数。
# =============================================================
print("=" * 50)
print("练习 9.15：彩票分析")

# 定义中奖号码（my_ticket）
my_ticket = winning_ticket

# 计数器
attempts = 0

# 不断抽取直到匹配
while True:
    attempts += 1
    drawn = random.sample(lottery_pool, 4)
    if set(drawn) == set(my_ticket):
        break

print(f"After {attempts} attempts, you finally won the grand prize!")
print(f"Winning ticket: {my_ticket}")

# =============================================================
# 练习 9.16：Python 3 Module of the Week
# 访问 pymotw.com 网站，探索感兴趣的模块。
# =============================================================
print("=" * 50)
print("练习 9.16：Python 3 Module of the Week")
print("Visit https://pymotw.com/3/ to explore the Python standard library.")
print("Recommended starting point: the 'random' module.")
print("The 'random' module provides functions for generating random numbers,")
print("making random selections, shuffling sequences, and more — as")
print("demonstrated in exercises 9.13 through 9.15 above!")
