import psycopg2

# Função para criar conexão no banco

def conecta_db():
    
    con = psycopg2.connect(host='ec2-54-147-36-107.compute-1.amazonaws.com', 
                         database='d1l8b7e0vn1bdo',
                         user='wryowogktuskud', 
                         password='5f23bd64f3a214419e951e5c7d7ce9ead3775018c11bd0d8cc4346dd32ec36f9')
    return con
    conn_str = 'postgres://hzwtrwnbqzymjl:e9a295bd21d9fb38470a6effbd9171e3dd41b63c9aa75b72f45fd6d7af94555b@ec2-34-199-68-114.compute-1.amazonaws.com:5432/d9s9bd88052min'

