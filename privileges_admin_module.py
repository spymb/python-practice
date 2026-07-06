"""存储 Privileges 和 Admin 类的模块（从 user_module 导入 User）。"""

from user_module import User


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


class Admin(User):
    """管理员类，继承自 User，使用 Privileges 实例作为属性。"""

    def __init__(self, first_name, last_name, age, location, email):
        """初始化管理员的属性。"""
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
