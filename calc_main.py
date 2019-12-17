"""
@Author: _chang_an
@Date: 2019-12-11 18:28:01
@LastEditTime: 2019-12-16 13:56:40
@LastEditors: _chang_an
@Description: version:
# 2019.12.5----0.1  功能实现
# 2019.12.7----0.2  重构代码，增加小细节
# 2019.12.11---1.1  分出小模块
# 2019.12.12---2.0  在原有代码基础上分模块重新撰写
@FilePath: \calculator2.1.0\calc_main.py
"""


from tkinter import *
from calc_page import *
from standard_page import *

root = Tk()
root.title("简单计算器")
CalcPage(root)
root.mainloop()

