# ---------------------------------------------------------------
# 文件名：test_cities.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：第11章练习 11.1 & 11.2 —— 测试 city_functions 模块
# ---------------------------------------------------------------

from city_functions import city_country


def test_city_country():
    """测试不含人口参数的城市/国家格式化。"""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'


def test_city_country_population():
    """测试含人口参数的城市/国家格式化。"""
    result = city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile - population 5000000'
