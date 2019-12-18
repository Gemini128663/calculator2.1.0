"""
@Author: your name
@Date: 2019-12-17 10:52:10
@LastEditTime: 2019-12-18 10:36:24
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \calculator2.1.0\standard_page.py
"""
from tkinter import *
from standard_science_calc import standard_science_calc
from button_name import button_name


class StandardFrame(Frame):
    """标准型页面，继承Frame类"""

    def __init__(self, master=None):
        """定义构造函数"""
        Frame.__init__(self, master)

        self.standpage()  # 初始化页面

    def standpage(self):
        """设置显示组件的字体，宽度，背景，方位以及位置

        设置文本标签的方位和位置
        设置按钮组件
        定义点击函数
        """
        self.show = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=29,
            bg="white",
            anchor=W,
        )
        self.show.pack(side=TOP, pady=24)
        label = Label(self, anchor=W, text="标准型计算器")
        label.place(x=195, y=62)
        p = Frame(self)
        p.pack(side=BOTTOM)

        button_name(
            p,
            name=(
                "+",
                "1",
                "2",
                "3",
                "↺",
                "-",
                "4",
                "5",
                "6",
                "√",
                "*",
                "7",
                "8",
                "9",
                "^2",
                "÷",
                ".",
                "0",
                "%",
                "1/",
                "←",
                "±",
                "**",
                "//",
                "=",
            ),
            number=5,
            click_method=self.standard_science_click,
            clean_method=self.clean,
        )

    def standard_science_click(self, event):
        """[标准型和科学型的回调函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """

        self.show["text"] = standard_science_calc(event, self.show["text"])

        if event.widget["text"] == "=" and self.show["text"] is not None:
            # 赋值给self.hi
            self.hi = self.show["text"]
            if "÷" in self.hi:  # 将÷换成/
                self.hi = self.hi.replace("÷", "/")
            print(self.hi)
            self.show["text"] = str("{:.2f}".format(eval(self.hi)))

    def clean(self, event):
        """[summary]
        
        Arguments:
            event {[type]} -- [description]
        """
        print
        self.show["text"] = ("",)
