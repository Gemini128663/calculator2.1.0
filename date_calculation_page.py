"""
@Author: your name
@Date: 2019-12-17 10:52:10
@LastEditTime: 2019-12-18 10:36:04
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \calculator2.1.0\date_calculation_page.py
"""
from tkinter import *
from date_calc import date_calculation_click
from standard_science_calc import standard_science_calc
from button_name import button_name


class dateFrame(Frame):
    """日期计算页面，继承Frame类"""

    def __init__(self, master=None):
        """[日期计算页面初始化]
        
        Keyword Arguments:
            master {['tkinter.Frame']} -- [页面] (default: {None})
        """
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.datepage()

    def datepage(self):

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
        label = Label(
            self, anchor=W, text="日期计算(请输入类似日期：2019.12.9+(-)12或者2019.12.9-2019.2.2)"
        )
        label.place(x=0, y=62)
        p = Frame(self)
        p.pack(side=BOTTOM)
        button_name(
            p,
            name=(
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "0",
                "+",
                "-",
                ".",
                "=",
                "←",
                "↺",
            ),
            number=4,
            click_method=self.date_click,
            clean_method=self.clean,
        )

    def date_click(self, event):
        """[点击函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """
        """显示组件计算函数"""
        if event.widget["text"] == "=" and self.show["text"] is not None:
            self.show["text"] = date_calculation_click(event, self.show["text"])

        self.show["text"] = standard_science_calc(event, self.show["text"])

    def clean(self, event):
        """[日期计算清空函数]

        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """
        self.show["text"] = ""
