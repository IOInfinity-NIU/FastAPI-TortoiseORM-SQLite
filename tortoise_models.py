"""
Title        : create a product ORM model.
Create Time  : 2022/12/15
Author       : IOInfinity x 源碼無限      
"""


from tortoise import fields
from tortoise.models import Model
import datetime

class Product(Model):
    """Product model"""
    id = fields.IntField(pk=True)
    product_name = fields.CharField(max_length=64)
    product_type = fields.CharField(max_length=16)
    base64_image = fields.TextField(null=True)
    create_time = fields.DateField(
        default=datetime.datetime.utcnow())
    update_time = fields.DateField(
        default=datetime.datetime.utcnow())

    def __str__(self):
        return self.product_name
