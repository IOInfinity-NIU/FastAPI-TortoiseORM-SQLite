"""
Title       : API response specification
Create Time : 2022/12/14
Author      : IOInfinity x 源碼無限
"""

from pydantic import BaseModel, Field


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
