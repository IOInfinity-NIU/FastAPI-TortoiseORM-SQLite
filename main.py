"""
Title       : Create and Query product API    
Create Time : 2022/12/14
Author      : IOInfinity x 源碼無限
"""
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI, Query
from pd_response import BaseResponse, ProductResponseModel, ProductResponseListModel
from pd_request import ProductRequestModel
from tortoise_models import Product


API_DOC_TITLE = "Simple product management API [IOInfinity x 源碼無限]"

product_app = FastAPI(title=API_DOC_TITLE)


@product_app.get(
    "/ok",
    tags=["General"],
    response_model=BaseResponse)
def health_check():
    """Check the <b>health</b> of product API"""
    return BaseResponse(
        msg="success",
        code=0,
    ).dict()


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
    return BaseResponse(
        msg="success",
        code=0,
    ).dict()


@product_app.get(
    "/products",
    tags=["Product"],
    response_model=ProductResponseListModel)
async def query_products(
        product_id: int | None = Query(default=None, min=1)):
    """<b>Query</b> products"""
    query = dict(id=product_id) if product_id else dict()
    # Query data from database
    products = await Product.filter(**query)
    product_list = []
    for product in products:
        product_list.append(
            ProductResponseModel(
               product_id=product.id,
               product_type=product.product_type,
               product_name=product.product_name,
               base64_image=product.base64_image,
            ).dict()
        )
    return ProductResponseListModel(
        msg="success",
        code=0,
        product_list=product_list,
    ).dict()


# Register Tortoise ORM
register_tortoise(
    product_app,
    db_url="sqlite://product.db",
    modules={"models": ["tortoise_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
