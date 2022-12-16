"""
Title       : Create product API    
Create Time : 2022/12/14
Author      : IOInfinity x 源碼無限
"""
from tortoise.contrib.fastapi import register_tortoise 
from fastapi import FastAPI
from pd_response import BaseResponse
from pd_request import ProductRequestModel
from tortoise_models import Product


API_DOC_TITLE = "Simple product management API [IOInfinity x 源碼無限]"

SUCCESS_RESPONSE = {
    "msg": "success",
    "code": 0
}
product_app = FastAPI(title=API_DOC_TITLE)


@product_app.get(
    "/ok",
    tags=["General"],
    response_model=BaseResponse)
def health_check():
    """Check the <b>health</b> of product API"""
    return SUCCESS_RESPONSE


@product_app.post(
    "/products",
    tags=["Product"], response_model=BaseResponse)
async def create_product(product: ProductRequestModel):
    """<b>Create</b> a product"""
    await Product.create(
        product_name=product.product_name,
        product_type=product.product_type,
        base64_image=product.base64_image
    )
    return SUCCESS_RESPONSE


# Register Tortoise ORM
register_tortoise(
    product_app,
    db_url="sqlite://product.db",
    modules={"models": ["tortoise_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)