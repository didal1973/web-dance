import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Subscription(SqlAlchemyBase):
    __tablename__ = 'subscriptions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    direction_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey("direction.id"))
    level_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("level.id"))
    direction = orm.relation('Direction')
    level = orm.relation('Level')
