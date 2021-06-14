import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Day(SqlAlchemyBase):
    __tablename__ = 'days'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)

