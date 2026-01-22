from pydantic import BaseModel
from datetime import date

# Classe Base: contém os campos comuns que usamos tanto para criar quanto para ler
class TransacaoBase(BaseModel):
    titulo: str
    valor: float
    tipo: str  # Ex: 'receita' ou 'despesa'
    categoria: str
    data: date

# Schema para CRIAÇÃO (Input):
# Herda tudo da Base. Se quiséssemos campos opcionais apenas na criação, colocaríamos aqui.
class TransacaoCreate(TransacaoBase):
    pass

# Schema para LEITURA (Output):
# É o que a API devolve para o Frontend.
class Transacao(TransacaoBase):
    id: int  # O ID só existe DEPOIS que salvamos no banco, por isso fica aqui

    # Configuração necessária para o Pydantic ler dados do banco de dados (ORM)
    class Config:
        from_attributes = True