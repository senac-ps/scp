from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importando nossos modulos locais
from . import crud, models, schemas
from .database import SessionLocal, engine

# Cria as tabelas no banco de dados automaticamente ao iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia: Pega uma sessao do banco para cada requisicao
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Rotas (Endpoints) ---

@app.post("/transacoes/", response_model=schemas.Transacao)
def criar_transacao(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar uma nova receita ou despesa.
    """
    return crud.create_transacao(db=db, transacao=transacao)

@app.get("/transacoes/", response_model=List[schemas.Transacao])
def ler_transacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Endpoint para ler a lista de gastos.
    """
    transacoes = crud.get_transacoes(db, skip=skip, limit=limit)
    return transacoes

@app.get("/")
def home():
    """
    Rota raiz apenas para verificar se a API esta no ar.
    """
    return {"msg": "API Financeira rodando com sucesso!"}