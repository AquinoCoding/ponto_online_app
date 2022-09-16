from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.point_model import Point
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees

def read_user_session(email: str):

    with create_session() as session_db:
        users = session_db.query(Users).filter(Users.email == email)
        return [users]
    
def read_user_single_session(email: str):

    with create_session() as session_db:
        user = session_db.query(Users).filter(Users.email == email).first()
        
        return user
        
        #find_acess_employees = session_db.query(Employees).filter(Employees.cpf_id == usuario).first()