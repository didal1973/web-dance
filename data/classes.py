import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Hall(SqlAlchemyBase):
    __tablename__ = 'classes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)
