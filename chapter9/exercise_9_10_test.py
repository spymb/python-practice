"""练习 9.10：导入 Restaurant 类"""

from restaurant_module import Restaurant

# 创建实例并调用方法
restaurant = Restaurant('Moon River Bistro', 'French')
print("--- Testing Restaurant Import ---")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(100)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(25)
print(f"Number served after increment: {restaurant.number_served}")
print("Import test passed!")
