"""存储 Restaurant 类的模块。"""


class Restaurant:
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
