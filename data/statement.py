import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Statement(SqlAlchemyBase):
    __tablename__ = 'statement'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)
    lastname = sqlalchemy.Column(sqlalchemy.TEXT)
    email = sqlalchemy.Column(sqlalchemy.TEXT)
    level = sqlalchemy.Column(sqlalchemy.TEXT)
    country = sqlalchemy.Column(sqlalchemy.TEXT)
    day = sqlalchemy.Column(sqlalchemy.TEXT)
