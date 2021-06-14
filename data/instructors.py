import sqlalchemy
from .db_session import SqlAlchemyBase
# from sqlalchemy import orm

class Instructor(SqlAlchemyBase):
    __tablename__ = 'instructors'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT)
    about = sqlalchemy.Column(sqlalchemy.TEXT)

