"""
 # @Author: chang_an
 # @Date: 2019-12-21 09:25:37
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-21 09:26:17
 # @FilePath: \calculator2.1.0\calculation\calculator.py
"""
from tkinter import *

from packages.calculator_page import CalcPage

# from packages.standard_page import *


def calc():
    root = Tk()
    root.title("简单计算器")
    CalcPage(root)
    root.mainloop()


calc()

