"""
 # @Author: chang_an
 # @Date: 2019-12-21 09:25:37
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-21 09:28:01
 # @FilePath: \calculator2.1.0\calculation\packages\button_names.py
"""

from tkinter import Button


def button_name(p, name, number, click_method, clean_method):
    """[实现按钮组件位置布局，命名，以及绑定回调函数]
    
    Arguments:
        p {['tkinter.Frame']} -- [容器子页面]
        name {['tuple']} -- [按钮的名字]
        number {['int']} -- [行列数]
        click_method {['function']} -- [数字键和运算键绑定的回调函数]
        clean_method {['function]} -- [清空键绑定的回调函数]
    """

    names = name
    # 遍历字符串元组
    for i, _button_name in enumerate(names):
        # 创建Button，将Button放入p组件中
        b = Button(p, text=_button_name, font=("Verdana", 20), width=5)
        b.grid(row=i // number, column=i % number)
        # 为鼠标左键的单击事件绑定事件处理方法
        b.bind("<Button-1>", click_method)
        # 为鼠标左键的双击事件绑定事件处理方法
        if b["text"] == "↺":
            b.bind("<Button-1>", clean_method)
