from ponto_online_app.database.db_session import create_session

def insert_session(an):

    with create_session() as session:
        session.add(an)
        session.commit()