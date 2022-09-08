from ponto_online_app.database.db_session import create_session
from ponto_online_app.models.point_model import Point


def insert_session(an):

    with create_session() as session:
        session.add(an)
        session.commit()


def insert_point(cpf_user: str, date: str, time: str):

    points: Point = Point(cpf_user=cpf_user, date=date, time=time)

    with create_session() as session:
        session.add(points)
        session.commit()
