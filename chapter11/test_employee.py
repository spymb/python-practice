# ---------------------------------------------------------------
# 文件名：test_employee.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：第11章练习 11.3 —— 测试 Employee 类（使用夹具）
# ---------------------------------------------------------------

import pytest
from employee import Employee


@pytest.fixture
def employee():
    """创建一个 Employee 实例供测试使用。"""
    return Employee('john', 'doe', 50000)


def test_give_default_raise(employee):
    """测试默认加薪 5000 美元。"""
    employee.give_raise()
    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    """测试自定义加薪金额。"""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
