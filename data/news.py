import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.TEXT)
    text = sqlalchemy.Column(sqlalchemy.TEXT)
