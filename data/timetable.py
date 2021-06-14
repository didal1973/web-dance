import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Timetable(SqlAlchemyBase):
    __tablename__ = 'timetable'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    day_id = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("days.id"))
    time_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("time.id"))
    group_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("groups.id"))
    hall_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("classes.id"))

    day = orm.relation('Day')
    time = orm.relation('Time')
    group = orm.relation('Group')
    hall = orm.relation('Hall')
