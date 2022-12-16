"""
Title       : Define product types
Create Time : 2022/12/14
Author      : IOInfinity x 源碼無限
"""
from enum import Enum


class ProductTypes(str, Enum):
    """ Define product types """
    DESKTOP_PC = 'Desktop PC'
    MOBILE_DEVICE = 'Mobile device'
    LAPTOP = 'Laptop'
