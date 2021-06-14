import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Level(SqlAlchemyBase):
    __tablename__ = 'level'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)
    text = sqlalchemy.Column(sqlalchemy.TEXT)
    price = sqlalchemy.Column(sqlalchemy.TEXT)
    image = sqlalchemy.Column(sqlalchemy.TEXT)
