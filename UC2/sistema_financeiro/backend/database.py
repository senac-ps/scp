from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados. 
# Para usar PostgreSQL no futuro, basta alterar esta string.
SQLALCHEMY_DATABASE_URL = "sqlite:///./financeiro.db"

# Cria o "motor" de conexão. 
# "check_same_thread": False é necessário apenas para SQLite.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma fábrica de sessões (cada requisição terá sua própria sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os nossos modelos (tabelas) herdarem
Base = declarative_base()

# Função utilitária para pegar a conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()