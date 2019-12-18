"""
 # @Author: chang_an
 # @Date: 2019-12-18 18:13:11
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-18 18:16:18
 # @FilePath: \calculator2.1.0\calculation\calculator_page.py
"""


from calculation.standard_page import *
from calculation.science_page import *
from calculation.programmer_page import *
from calculation.calculator_date_page import *


class CalcPage(object):
    def __init__(self, master=None):
        """[初始化页面]
        
        Keyword Arguments:
            master {['tkinter.Frame']} -- [页面] (default: {None})
        """

        self.root = master  # 定义内部变量root
        self.main_page()  # 设置主页面

    def main_page(self):
        """[菜单实现以及设定初始页面]
        
        """
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
        """[实现标准型页面]
        
        """

        self.standard_page.pack()
        self.science_page.pack_forget()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack_forget()

    def science(self):
        """[实现科学型页面]
        
        """

        self.standard_page.pack_forget()
        self.science_page.pack()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack_forget()

    def programmer(self):
        """[实现程序员型页面]
        
        """
        self.standard_page.pack_forget()
        self.science_page.pack_forget()
        self.programmer_page.pack()
        self.date_calculator_page.pack_forget()

    def date_calculator(self):
        """[实现日期计算型页面]
        
        """
        self.standard_page.pack_forget()
        self.science_page.pack_forget()
        self.programmer_page.pack_forget()
        self.date_calculator_page.pack()
