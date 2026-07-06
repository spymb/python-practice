# ---------------------------------------------------------------
# 文件名：employee.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：第11章练习 11.3 —— Employee 类
# ---------------------------------------------------------------


class Employee:
    """一个表示雇员的简单类。"""

    def __init__(self, first_name, last_name, annual_salary):
        """初始化雇员属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """给雇员加薪，默认为 5000 美元。"""
        self.annual_salary += amount
