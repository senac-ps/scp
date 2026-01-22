from sqlalchemy.orm import Session
from . import models, schemas

def get_transacoes(db: Session, skip: int = 0, limit: int = 100):
    """
    Busca todas as transações na base de dados.
    'skip' e 'limit' servem para paginação (ex: carregar de 10 em 10).
    """
    return db.query(models.Transacao).offset(skip).limit(limit).all()

def create_transacao(db: Session, transacao: schemas.TransacaoCreate):
    """
    Recebe os dados validados (schema), converte para o formato da tabela (model)
    e grava na base de dados.
    """
    # 1. Transforma o Schema (Pydantic) em Model (SQLAlchemy)
    # **transacao.dict() desempacota os campos (titulo, valor, etc) automaticamente
    db_transacao = models.Transacao(**transacao.dict())
    
    # 2. Adiciona à sessão (prepara para salvar)
    db.add(db_transacao)
    
    # 3. Efetiva a gravação (Commit)
    db.commit()
    
    # 4. Atualiza o objeto com dados gerados pela base (como o ID)
    db.refresh(db_transacao)
    
    return db_transacao