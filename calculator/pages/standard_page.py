"""
 # @Author: chang_an
 # @Date: 2019-12-17 10:52:10
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-18 13:57:25
 # @FilePath: \calculator2.1.0\standard_page.py
"""


from tkinter import *

from pages.button_names import button_name
from calculation.calculator_standard_science import standard_science_calc


class StandardFrame(Frame):
    """[标准型页面实现]
    
    Arguments:
        Frame {[class]} -- [tkinter子类]
    """

    def __init__(self, master=None):
        """[初始化页面]
        
        """
        Frame.__init__(self, master)

        self.standpage()  # 初始化页面

    def standpage(self):
        """[标准页面的实现]
        
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
        """[清空函数]
        
        Arguments:
            event {['tkinter.Event']} -- [点击事件]
        """
        print
        self.show["text"] = ("",)
