import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Comments(SqlAlchemyBase):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)
    lastname = sqlalchemy.Column(sqlalchemy.TEXT)
    email = sqlalchemy.Column(sqlalchemy.TEXT)
    text = sqlalchemy.Column(sqlalchemy.TEXT)
    date = sqlalchemy.Column(sqlalchemy.TEXT)
