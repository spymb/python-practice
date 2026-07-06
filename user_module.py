"""只存储 User 类的模块。"""


class User:
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
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        """将登录尝试次数加 1。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录尝试次数重置为 0。"""
        self.login_attempts = 0
