"""
Title       : API response specification
Create Time : 2022/12/14
Author      : IOInfinity x 源碼無限
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from enum_product import ProductTypes


class BaseResponse(BaseModel):
    """Base response"""
    msg: str = Field(
        titile="Message of response",
        default="success"
    )

    code: int = Field(
        title="Code of response",
        default=0
    )


class ProductResponseModel(BaseModel):
    """Product response fields"""
    product_id: int = Field(
        title="Product ID",
        default=1,
        min=1
    )
    product_name: str = Field(
        title="Product name",
        default="Mac mini M2",
        max_length=128,
    )
    product_type: ProductTypes = Field(
        title="Product type",
        default=ProductTypes.LAPTOP,
    )
    base64_image: Optional[str] = Field(
        title="Base64-encoded image",
        default="data:image/png;base64,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",
    )


class ProductResponseListModel(BaseResponse):
    """Product response list"""
    product_list: Optional[List[ProductResponseModel]] = Field(
        title="Product list",
    )