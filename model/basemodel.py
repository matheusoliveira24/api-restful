from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id_serie: str
    titulo: str
    descricao: str
    ano_lancamento: int
    id_categoria: int

class Ator(BaseModel):
    nome: str

class Motivo(BaseModel):
    id_serie: int
    motivo: str

class Avaliacao(BaseModel):
    id_serie: int
    nota: int
    comentario: Optional[str]

class Categoria(BaseModel):
    nome: str