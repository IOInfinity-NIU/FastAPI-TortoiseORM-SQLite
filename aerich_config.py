"""
Title        : create a Aerich migration configration file for Tortoise ORM.
Create Time  : 2022/12/15
Author       : IOInfinity x 源碼無限           
"""

ORM_MIGRATION_SQLITE = {
    "connections": {
        "default": "sqlite://product.db",
    },
    "apps": {
        "models": {
            "models": [
                "tortoise_models",
                "tests.models",
                "aerich.models"],
            "default_connection": "default",
        },
    },
}
