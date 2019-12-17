"""
@Author: _chang_an
@Date: 2019-12-11 18:30:38
@LastEditTime: 2019-12-16 14:54:46
@LastEditors: _chang_an
@Description: 计算器各个页面的初始化以及菜单栏的绑定函数
@FilePath: \calculator2.1.0\calc_page.py
"""
from standard_page import *
from science_page import *
from programmer_page import *
from date_calculation_page import *


class CalcPage(object):
     
   

    def __init__(self, master=None):
        """[初始化页面]
        
        Keyword Arguments:
            master {['tkinter.Frame']} -- [页面] (default: {None})
        """        
        
        self.root = master  # 定义内部变量root
        self.main_page()  # 设置主页面

    def main_page(self):       
        """创建四个不同的Frame（标准型，科学型，日期计算，程序员）

        设置默认页面
        在顶部添加标准型，科学型，程序员，日期计算菜单"""
        self.standard_page = StandardFrame(self.root)  # 创建不同Frame
        self.science_page = ScienceFrame(self.root)
        self.programmer_page = Programmer(self.root)
        self.date_calculator_page = dateFrame(self.root)
        self.standard_page.pack()  # 默认页面
        menubar = Menu(self.root)
        menubar.add_command(label="标准型", command=self.standard)
        menubar.add_command(label="科学型", command=self.science)
        menubar.add_command(label="程序员", command=self.programmer)
        menubar.add_command(label="日期计算", command=self.date_calculator)
        self.root["menu"] = menubar

    def standard(self):
        """标准型回调函数,forget science_page,programmer_page,date_calculator_page"""
        self.standard_page.pack()
        self.science_page.pack_forget()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack_forget()

    def science(self):
        """科学型回调函数,forget standard_page,programmer_page,date_calculator_page"""
        self.standard_page.pack_forget()
        self.science_page.pack()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack_forget()

    def programmer(self):
        """程序员型回调函数,forget standard_page,science_page,date_calculator_page"""
        self.standard_page.pack_forget()
        self.science_page.pack_forget()
        self.programmer_page.pack()
        self.date_calculator_page.pack_forget()

    def date_calculator(self):
        """日期计算型回调函数,forget standard_page,science_page,programmer_page"""
        self.standard_page.pack_forget()
        self.science_page.pack_forget()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack()
