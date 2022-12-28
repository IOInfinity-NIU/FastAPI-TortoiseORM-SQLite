"""
Title       : Create, Query, Update and Delete product API    
Create Time : 2022/12/28
Author      : IOInfinity x 源碼無限
"""
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI, Query
from pd_response import (
    BaseResponse,
    ProductResponseModel,
    ProductResponseListModel
)
from pd_request import (
    ProductRequestModel,
    ProductUpdateRequestModel,
)
from tortoise_models import Product
from fastapi.openapi.docs import get_redoc_html

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


@product_app.patch(
    "/products/{product_id}",
    tags=["Product"],
    response_model=BaseResponse)
async def update_product(
        product_id: int,
        product_request: ProductUpdateRequestModel,):
    """
    Update the product information.
    """
    # print the product in the terminal by product id.
    print("Product ID:")
    print(product_id)
    # Print the product request parameters
    print("Product request:")
    print(product_request.product_name)
    print(product_request.product_type)
    # Find the product id from database
    db_product = await Product.get(id=product_id)

    if db_product:
        print("Product data in database:")
        print(db_product.product_name)
        print(db_product.product_type)

        # Update product data by product id.
        if product_request.product_name:
            db_product.product_name = product_request.product_name
        if product_request.product_type:
            db_product.product_type = product_request.product_type
        await db_product.save()

    return BaseResponse(
        msg="success",
        code=0,
    ).dict()


@product_app.delete(
    "/products/{product_id}",
    tags=["Product"],
    response_model=BaseResponse)
async def delete_product(product_id:int):
    """
    Delete product by product id.
    """
    # Print the product id in the terminal.
    print(product_id)
    db_product = await Product.get(id=product_id)
    if db_product:
        await db_product.delete()
    return BaseResponse(
        msg="success",
        code=0,
    ).dict()
 

@product_app.get("/redoc", include_in_schema=False)
async def get_redoct_document():
    """Import redoc API document"""
    return get_redoc_html(
        openapi_url="/openapi.json",
        title=API_DOC_TITLE,
    )

# Register Tortoise ORM
register_tortoise(
    product_app,
    db_url="sqlite://product.db",
    modules={"models": ["tortoise_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
