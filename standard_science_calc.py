"""
@Author: _chang_an
@Date: 2019-12-11 17:05:41
@LastEditTime: 2019-12-16 15:11:56
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \calculator2.1.0\standard_science_calc.py
"""
import math


def standard_science_calc(event, text):
    """[标准型和科学型计算过程的实现]
    
    Arguments:
        event {['tkinter.Event']} -- ['点击事件']
        text {['str']} -- [显示组件显示的文本]
    
    Returns:
        [str] -- [计算后需要显示的文本]
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
        "%",
        "**",
        "//",
    ):
        return text + event.widget["text"]
    if (event.widget["text"]) in ("+", "-", "÷", "*",):
        if text[-1] in ("+", "-", "÷", "*",):
            try:
                text[-1] = event.widget["text"]
            except:
                text = text[:-1]

        text = text + event.widget["text"]
        return text
    # 不需要按下等于号的  先输入数字，再输入运算符
    elif event.widget["text"] == "log":  # 以10为底的对数
        return str("{:.2f}".format(math.log10(eval(text))))
    elif event.widget["text"] == "log2":  # 以2为底的对数
        return str("{:.2f}".format(math.log2(eval(text))))
    elif event.widget["text"] == "ln":  # 以10为底的对数
        return str("{:.2f}".format(math.log1p(eval(text) - 1)))
    elif event.widget["text"] == "1/":  # 倒数
        return str("{:.2f}".format(1 / eval(text)))
    elif event.widget["text"] == "√":  # 二次开根号
        return str("{:.2f}".format(math.sqrt(eval(text))))
    elif event.widget["text"] == "^2":  # 平方
        return str("{:.2f}".format(eval(text) ** 2))
    elif event.widget["text"] == "tan":  # tan函数
        return str("{:.2f}".format(math.tan(math.radians(eval(text)))))
    elif event.widget["text"] == "sin":  # sin函数
        return str("{:.2f}".format(math.sin(math.radians(eval(text)))))
    elif event.widget["text"] == "cos":  # cos函数
        return str("{:.2f}".format(math.cos(math.radians(eval(text)))))
    elif event.widget["text"] == "n!":  # 实现阶乘
        return str("{:.2f}".format(math.factorial(eval(text))))
    elif event.widget["text"] == "←":  # 退格键
        return text[:-1]
    elif event.widget["text"] == "±":  # 正负号
        if "-" in text:
            return text[1:]
        else:
            return "-" + text
