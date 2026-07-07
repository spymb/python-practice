# ---------------------------------------------------------------
# 文件名：city_functions.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：第11章练习 11.1 & 11.2 —— 城市/国家格式化函数
# ---------------------------------------------------------------


def city_country(city, country, population=None):
    """返回格式化的城市和国家字符串。

    Args:
        city: 城市名。
        country: 国家名。
        population: 可选的人口数量。

    Returns:
        格式为 "City, Country" 或 "City, Country - population xxx" 的字符串。
    """
    formatted = f"{city.title()}, {country.title()}"
    if population:
        formatted += f" - population {population}"
    return formatted
