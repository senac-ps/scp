from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    # A chave primária (ID único de cada gasto)
    id = Column(Integer, primary_key=True, index=True)
    
    # O que foi gasto (ex: "Almoço no Shopping")
    titulo = Column(String, index=True)
    
    # O valor monetário (ex: 50.00)
    valor = Column(Float)
    
    # Define se é 'receita' ou 'despesa'
    tipo = Column(String) 
    
    # Ex: 'Alimentação', 'Transporte', 'Salário'
    categoria = Column(String)
    
    # A data do gasto. O banco vai guardar no formato YYYY-MM-DD
    data = Column(Date)