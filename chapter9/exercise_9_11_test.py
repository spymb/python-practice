"""练习 9.11：导入 Admin 类"""

from user_admin_module import Admin

# 创建 Admin 实例并调用方法
admin = Admin('Frank', 'Zhao', 40, 'Hangzhou', 'frank@admin.com')
print("--- Testing Admin Import (single module) ---")
admin.describe_user()
admin.privileges.show_privileges()
print("Import test passed!")
