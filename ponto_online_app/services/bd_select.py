from ponto_online_app.database.db_session import create_session


def select_session(an):

    with create_session() as session:
        pass