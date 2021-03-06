[![version](https://img.shields.io/badge/version-2.1.0-orange)](https://github.com/Gemini128663/calculator2.1.0/blob/master/ChangeLog.txt
)
[![install](https://img.shields.io/badge/install-calculator-red)](https://pypi.org/manage/project/calculator8/release/2.0.0/
)
[![](https://img.shields.io/badge/LICENSE-MIT-green)](https://github.com/Gemini128663/calculator2.1.0/blob/master/LICENSE
)

# 使用Python实现简单计算器
<!-- TOC -->

- [使用Python实现简单计算器](#使用python实现简单计算器)
  - [Python版本](#python版本)
  - [依赖库](#依赖库)
  - [项目背景](#项目背景)
  - [已有功能](#已有功能)
  - [计算器具体页面](#计算器具体页面)
  - [使用说明](#使用说明)
  - [文件对应说明](#文件对应说明)
  - [download](#download)
  - [计算器程序实例说明](#计算器程序实例说明)

<!-- /TOC -->
## Python版本

+ Python 3.7.4

## 依赖库

+ [x] tkinter
+ [x] time、datetime
+ [x] math

## 项目背景

计算器作为大多数新手程序员上路必做的一个项目，可强化自己的逻辑编程能力。

## 已有功能

1. 标准型：加减乘除、开根号、平方、倒数、幂次方、取余取整。
2. 科学型：tan 函数、sin 函数、cos 函数、阶乘、log、ln。

3. 程序员型：进制转换。

4. 日期计算：日期相加减计算天数。

## 计算器具体页面

![简单计算器的具体页面](docs/具体页面.png)

## 使用说明

1. 标准型：加减乘除、取余取整、幂次方的计算结果需要按下等于键来看到最后的结果；倒数、开根号、平方是不需要按下等于键的。

2. 科学型：对于所有的运算需要先按下数字，再按下函数键。

3. 程序员型：输入十进制的数，显示框会从上而下显示16进制、10进制、8进制、2进制。

4. 日期计算：
   1. 加法：输入日期，加号之前的输入要带有年月份且以 . 进行分割，后面可输入一个数字进行等于相加，计算多少天之后是那一天

   2. 减法
      1. 两个日期进行等于相减。

      2. 一个日期和一个数字进行等于相减，具体同加法。

    \#  日期相减的范围是3019.1.19~1970.1.1

## 文件对应说明

1. calculation\calculator：主函数，只需运行这个文件就可以。  

2. packages\calculator_page：用来初始化四个菜单的文件。

3. packages\standard_page：标准型页面的具体内容。

4. packages\science_page：科学型页面的具体内容。

5. packages\programmer_page：程序员页面的具体内容。

6. packages\calculator_date_page：日期计算页面的具体内容。

7. packages\button_name：用来实现按钮的命名、位置、以及回调函数。

8. packages\calculator_date：日期计算处理过程。

9. packages\calculator_standard_science：标准型和科学型的计算处理过程。

\# 程序员型的计算处理过程是在 programmer_page 中实现的。

## download

1. &#8195;&#8195;[download-zip](https://github.com/Gemini128663/calculator2.1.0)  

   ![下载](docs/download.png)

 ```python
2.   pip install calculator8
 ```

## 计算器程序实例说明

```python

from calculator8 import calculator
calculator.calc()
```

即可计算器实例化
