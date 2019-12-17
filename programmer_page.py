"""
@Author: _chang_an
@Date: 2019-12-12 09:07:53
@LastEditTime: 2019-12-16 15:22:06
@LastEditors: Please set LastEditors
@Description: 程序员型页面的实现
@FilePath: \calculator2.1.0\programmer_page.py
"""
from tkinter import *
from button_name import button_name


class Programmer(Frame):
    """程序员型页面，继承Frame类"""

    def __init__(self, master=None):
        """[初始化页面]
        
        Keyword Arguments:
            master {['tkinter.Frame']} -- [页面] (default: {None})
        """
        Frame.__init__(self, master)
        self.root = master
        self.progarmmerpage()

    def progarmmerpage(self):
        """为2,8,10,16设置显示组件，并定义宽度，背景，方位以及位置

        设置文本标签的方位和位置
        设置按钮组件
        定义点击函数
        """
        self.show = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=19,
            bg="white",
            anchor=W,
        )
        self.show.pack(side=TOP, pady=1)  # 设置标签位置
        self.show1 = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=19,
            bg="white",
            anchor=W,
        )
        self.show1.pack(side=TOP, pady=1)
        self.show2 = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=19,
            bg="white",
            anchor=W,
        )
        self.show2.pack(side=TOP, pady=1)
        self.show3 = Label(
            self,
            relief=SUNKEN,
            font=("Courier New", 20),
            width=19,
            bg="white",
            anchor=W,
        )
        self.show3.pack(side=TOP, pady=1)
        label = Label(self, anchor=W, text="HEX")
        label.place(x=3, y=10)
        label = Label(self, anchor=W, text="DEC")
        label.place(x=3, y=50)
        label = Label(self, anchor=W, text="OCT")
        label.place(x=3, y=90)
        label = Label(self, anchor=W, text="BIN")
        label.place(x=3, y=130)

        p = Frame(self)
        p.pack(side=BOTTOM)
        button_name(
            p,
            name=("1", "2", "3", "↺", "4", "5", "6", "0", "7", "8", "9", "←",),
            number=4,
            click_method=self.programmer_click,
            clean_method=self.clean,
        )

    def programmer_click(self, event):
        """[程序员型点击计算]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """

        if event.widget["text"] in (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ".",
        ):
            self.show1["text"] = self.show1["text"] + event.widget["text"]  # 显示10进制
            self.show["text"] = str("{:X}".format(eval(self.show1["text"])))  # 显示16进制
            self.show2["text"] = str("{:o}".format(eval(self.show1["text"])))  # 显示8进制
            self.show3["text"] = str("{:b}".format(eval(self.show1["text"])))  # 显示2进制
        if event.widget["text"] == "←":
            self.show1["text"] = self.show1["text"][:-1]
            try:
                self.show["text"] = str("{:X}".format(eval(self.show1["text"])))
                self.show2["text"] = str("{:o}".format(eval(self.show1["text"])))
                self.show3["text"] = str("{:b}".format(eval(self.show1["text"])))
            except:
                pass
            if self.show1["text"] == "":
                self.show["text"] = ""
                self.show2["text"] = ""
                self.show3["text"] = ""

    def clean(self, event):
        """[清空函数函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """        
        self.show["text"] = ""
        try:
            self.show1["text"] = ""
            self.show2["text"] = ""
            self.show3["text"] = ""
        except:
            pass