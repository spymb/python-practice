# ---------------------------------------------------------------
# 文件名：printing_functions.py
# 作者：Python学习者
# 日期：2026-07-06
# 功能描述：打印模型相关的函数模块
#           供练习 8.15 导入使用。
# ---------------------------------------------------------------


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表 completed_models 中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"  - {completed_model}")
