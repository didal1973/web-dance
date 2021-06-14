import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Mail(SqlAlchemyBase):
    __tablename__ = 'mail'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.TEXT)
    text = sqlalchemy.Column(sqlalchemy.TEXT)
