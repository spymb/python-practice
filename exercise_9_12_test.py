"""练习 9.12：多个模块"""

from privileges_admin_module import Admin

# 创建 Admin 实例并调用方法
admin = Admin('Grace', 'Sun', 38, 'Chengdu', 'grace@admin.com')
print("--- Testing Admin Import (split modules) ---")
admin.describe_user()
admin.privileges.show_privileges()
print("Import test passed!")
