<!--
 * @Author: chang_an
 * @Date: 2019-12-16 19:14:57
 * @LastEditTime : 2019-12-20 15:54:40
 * @LastEditors  : chang_an
 * @Description: 
 * @FilePath: \calculator2.1.0\one-1\README.md
 -->

# 使用Python实现简单计算器

## Python版本

+ Python 3.7.4

## 依赖库

- [x] tkinter
- [x] time、datetime
- [x] math

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

1. main：主函数，只需运行这个文件就可以。  

2. calculation/calculator_page：用来初始化四个菜单的文件。

3. calculation/standard_page：标准型页面的具体内容。

4. calculation/science_page：科学型页面的具体内容。

5. calculation/programmer_page：程序员页面的具体内容。

6. calculation/calculator_date_page：日期计算页面的具体内容。

7. calculation/button_name：用来实现按钮的命名、位置、以及回调函数。

8. calculation/calculator_date：日期计算处理过程。

9. calculation/calculator_standard_science：标准型和科学型的计算处理过程。

\# 程序员型的计算处理过程是在 programmer_page 中实现的。

## download:

&#8195;&#8195;&#8195;&#8195;[download-zip](https://github.com/Gemini128663/calculator2.1.0
)

