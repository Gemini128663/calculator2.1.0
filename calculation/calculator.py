"""
 # @Author: chang_an
 # @LastEditors: chang_an5:37
 # @LastEditTime: 2019-12-25 17:14:59
 # @LastEditTime: 2019-12-21 09:26:17
 # @FilePath: \calculator2.1.0\calculation\calculator.py
"""
from tkinter import *

from packages.calculator_page import CalcPage

def calc():
    root = Tk()
    root.title("简单计算器")
    CalcPage(root)
    root.mainloop()


calc()

