from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" ADD "update_time" DATE NOT NULL  DEFAULT '2022-12-14 17:04:30.263932';
        ALTER TABLE "product" ADD "create_time" DATE NOT NULL  DEFAULT '2022-12-14 17:04:30.263921';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" DROP COLUMN "update_time";
        ALTER TABLE "product" DROP COLUMN "create_time";"""
