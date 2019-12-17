"""
@Author: your name
@Date: 2019-12-11 19:14:19
@LastEditTime: 2019-12-16 15:27:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \calculator2.1.0\science_page.py
"""

from tkinter import *
from standard_science_calc import standard_science_calc
from button_name import button_name


class ScienceFrame(Frame):
    """科学型页面，继承Frame类"""

    def __init__(self, master=None):
        """定义构造函数"""
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.sciencepage()

    def sciencepage(self):
        """设置显示组件的字体，宽度，背景，方位以及位置

        设置文本标签的方位和位置
        设置按钮组件
        定义点击函数
        """
        self.show = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=23,
            bg="white",
            anchor=W,
        )
        self.show.pack(side=TOP, pady=24)
        label = Label(self, anchor=W, text="科学型计算器")
        label.place(x=150, y=62)
        p = Frame(self)
        p.pack(side=BOTTOM)
        button_name(
            p,
            name=(
                "1",
                "2",
                "3",
                "↺",
                "4",
                "5",
                "6",
                "0",
                "7",
                "8",
                "9",
                ".",
                "tan",
                "sin",
                "cos",
                "n!",
                "log",
                "log2",
                "ln",
                "←",
            ),
            number=4,
            click_method=self.standard_science_click,
            clean_method=self.clean,
        )

    def standard_science_click(self, event):
        """[标准型和科学型的点击计算处理]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """        
       
        self.show["text"] = standard_science_calc(event, self.show["text"])  # 计算

        if event.widget["text"] == "=" and self.show["text"] is not None:  # 等于
            # 赋值给self.hi
            self.hi = self.show["text"]
            if "÷" in self.hi:  # 将÷换成/
                self.hi = self.hi.replace("÷", "/")
            print(self.hi)
            self.show["text"] = str("{:.2f}".format(eval(self.hi)))

    def clean(self, event):
        """[清空函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """

        self.show["text"] = ""
