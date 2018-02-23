#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "ufzhapi",
    version = "0.1.1",
    keywords = ("pip", "ufzhapi"),
    description = "深度学习实现知乎验证码识别",
    long_description = "深度学习实现知乎验证码识别",
    license = "MIT Licence",

    url = "https://github.com/littlepai/Unofficial-Zhihu-API.git",
    author = "littlepai",
    author_email = "txgyswh@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['requests', "bs4", 'tensorflow==1.2.1', 'pillow', 'numpy', 'tqdm']
)
