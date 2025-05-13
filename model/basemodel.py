# Um dia junto ao database.py, será a parte Model (onde a lógica do banco de dados ocorre e no caso deste arquivo a adaptação para o banco de dados, por meio da validação de dados, ou seja, ele permite criar classes que representam os dados esperados em uma aplicação, garantindo que os dados recebidos ou enviados estejam no formato correto.) desta aplicação.
from pydantic import BaseModel
from typing import Optional
from database import Database
 
db = Database()
 
# Modelos Pydantic
class Serie(BaseModel):
    titulo: str
    descricao: Optional[str]
    ano_lancamento: Optional[int]
    categoria_id: int
 
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
 
 
 