import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Time(SqlAlchemyBase):
    __tablename__ = 'time'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    time = sqlalchemy.Column(sqlalchemy.TEXT)

