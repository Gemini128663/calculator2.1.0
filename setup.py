"""
 # @Author: chang_an
 # @Date: 2019-12-20 17:28:46
 # @LastEditors: chang_an
 # @LastEditTime: 2019-12-20 19:07:40
 # @FilePath: \calculator2.1.0\setup.py
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="calculation",  # Replace with your own username
    version="2.1.0",  # 版本信息
    packages=setuptools.find_packages(),  # 程序包列表[项目中的py文件]
    python_requires=">=3",  # python版本
    url="https://github.com/Gemini128663/calculator2.1.0",  
    author="chang_an",  # 作者
    author_email="1286631591@qq.com",  # 作者邮箱
    description="python实现简单计算器",  # 描述
)
