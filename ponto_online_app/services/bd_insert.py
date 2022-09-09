from ponto_online_app import bcrypt

from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.point_model import Point
from ponto_online_app.models.users_model import Users



def insert_session(name, email, cnpj_id, level, password):
    
    password = bcrypt.generate_password_hash(password)

    an: Users = Users(name=name, email=email, 
                      cnpj_id=cnpj_id, level=level,
                      password=password)

    with create_session() as session:
        session.add(an)
        session.commit()


def insert_point(cpf_user: str, date: str, time: str):

    points: Point = Point(cpf_user=cpf_user, date=date, time=time)

    with create_session() as session:
        session.add(points)
        session.commit()

from ponto_online_app.database.db_session_sql import conecta_db

# Função para consultas no banco

def consultar_db(sql):
    
    con = conecta_db()
    cur = con.cursor()
    cur.execute(f'select * from public.{sql}')
    
    recset = cur.fetchall()
    registros = []
    
    for rec in recset:
        registros.append(rec)
        
    con.close()
    return registros
