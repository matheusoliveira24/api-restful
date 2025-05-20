from fastapi import FastAPI
from model.basemodel import Serie, Ator, Motivo, Avaliacao, Categoria
from database import Database

app = FastAPI()
db = Database()

def executar_sql(sql, params=(), fetch=False):
    db.conectar()
    result = db.executar(sql, params) if fetch else None
    db.desconectar()
    return result

# --- CREATE ---
@app.post('/series/')
def criar_serie(serie: Serie):
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s, %s, %s)"
    executar_sql(sql, (serie.titulo, serie.descricao, serie.ano_lancamento, serie.id_categoria))
    return {"mensagem": "Série cadastrada com sucesso"}

@app.post('/atores/')
def criar_ator(ator: Ator):
    sql = "INSERT INTO ator (nome) VALUES (%s)"
    executar_sql(sql, (ator.nome,))
    return {"mensagem": "Ator cadastrado com sucesso"}

@app.post('/motivos/')
def criar_motivo(motivo: Motivo):
    sql = "INSERT INTO motivo_assistir (id_serie, motivo) VALUES (%s, %s)"
    executar_sql(sql, (motivo.id_serie, motivo.motivo))
    return {"mensagem": "Motivo cadastrado com sucesso"}

@app.post('/avaliacoes/')
def criar_avaliacao(avaliacao: Avaliacao):
    sql = "INSERT INTO avaliacao_serie (id_serie, nota, comentario) VALUES (%s, %s, %s)"
    executar_sql(sql, (avaliacao.id_serie, avaliacao.nota, avaliacao.comentario))
    return {"mensagem": "Avaliação cadastrada com sucesso"}

@app.post('/categorias/')
def criar_categoria(categoria: Categoria):
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    executar_sql(sql, (categoria.nome,))
    return {"mensagem": "Categoria cadastrada com sucesso"}

@app.post('/ator_serie/{id_ator}/series/{id_serie}')
def associar_ator_serie(id_ator: int, id_serie: int, personagem: str):
    sql = "INSERT INTO ator_serie (id_ator, id_serie, personagem) VALUES (%s, %s, %s)"
    executar_sql(sql, (id_ator, id_serie, personagem))
    return {"mensagem": "Associação cadastrada com sucesso"}

# --- READ (reduzido) ---
def listar_tabela(nome_tabela):
    sql = f"SELECT * FROM {nome_tabela}"
    return executar_sql(sql, fetch=True)

@app.get("/series/")
def listar_series():
    return listar_tabela("serie")

@app.get("/atores/")
def listar_atores():
    return listar_tabela("ator")

@app.get("/motivos/")
def listar_motivos():
    return listar_tabela("motivo_assistir")

@app.get("/categorias/")
def listar_categorias():
    return listar_tabela("categoria")

@app.get("/avaliacoes/")
def listar_avaliacoes():
    return listar_tabela("avaliacao_serie")

@app.get("/series/{id_serie}/atores")
def listar_atores_por_serie(id_serie: int):
    sql = "SELECT * FROM ator_serie WHERE id_serie = %s"
    return executar_sql(sql, (id_serie,), fetch=True)

# --- DELETE (reduzido) ---
def deletar_por_id(nome_tabela, nome_id, valor_id):
    sql = f"DELETE FROM {nome_tabela} WHERE {nome_id} = %s"
    executar_sql(sql, (valor_id,))
    return {"mensagem": f"{nome_tabela.capitalize()} deletado(a) com sucesso"}

@app.delete("/atores/{id_ator}")
def deletar_ator(id_ator: int):
    return deletar_por_id("ator", "id_ator", id_ator)

@app.delete("/series/{id_serie}")
def deletar_serie(id_serie: int):
    return deletar_por_id("serie", "id_serie", id_serie)

@app.delete("/motivos/{id_motivo}")
def deletar_motivo(id_motivo: int):
    return deletar_por_id("motivo_assistir", "id_motivo", id_motivo)

@app.delete("/categorias/{id_categoria}")
def deletar_categoria(id_categoria: int):
    return deletar_por_id("categoria", "id_categoria", id_categoria)

@app.delete("/ator_serie/{id_ator}/series/{id_serie}")
def deletar_ator_serie(id_ator: int, id_serie: int):
    sql = "DELETE FROM ator_serie WHERE id_ator = %s AND id_serie = %s"
    executar_sql(sql, (id_ator, id_serie))
    return {"mensagem": "Associação deletada com sucesso"}

@app.delete("/avaliacoes/{id_avaliacao}")
def deletar_avaliacao(id_avaliacao: int):
    return deletar_por_id("avaliacao_serie", "id_avaliacao", id_avaliacao)

# --- UPDATE ---
# (mantém igual, mas pode ser reduzido com funções auxiliares também)