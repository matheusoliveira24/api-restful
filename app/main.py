from fastapi import FastAPI
from pydantic import BaseModel
from model.basemodel import Serie, Ator, Motivo, Avaliacao, Categoria
from database import Database

app = FastAPI()

db = Database()

class Serie(BaseModel):
    titulo: str
    descricao: str
    ano_lancamento: int
    id_categoria: int

@app.post('/series/')
def cadastrar(serie: Serie):
    db.conectar()
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s,%s,%s)"
    db.executar(sql,(serie.titulo, serie.descricao,serie.ano_lancamento, serie.id_categoria))
    db.desconectar()
    return {"mensagem": "Série cadastrada com sucesso"}

@app.post('/atores/')
def cadastrar(ator: Ator):
    db.conectar()
    sql = "INSERT INTO ator (nome) VALUES (%s)"
    db.executar(sql,(ator.nome,))
    db.desconectar()
    return {"mensagem": "Ator Cadastrado!"}

@app.post('/Motivos/')
def cadastrar(motivo: Motivo):
    db.conectar()
    sql = "INSERT INTO motivo_assistir (id_serie, motivo) VALUES (%s, %s)"
    db.executar(sql,(motivo.id_serie, motivo.motivo,))
    db.desconectar()
    return {"mensagem": "Motivo Cadastrado!"}

@app.post('/Avaliacao/')
def cadastrar(avaliacao : Avaliacao):
    db.conectar()
    sql = "INSERT INTO avaliacao_serie (id_serie, nota, comentario) VALUES (%s, %s, %s)"
    db.executar(sql,(avaliacao.id_serie, avaliacao.nota, avaliacao.comentario,))
    db.desconectar()
    return {"mensagem": "Motivo Cadastrado!"}

@app.post('/Categoria/')
def cadastrar(categoria : Categoria):
    db.conectar()
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    db.executar(sql,(categoria.nome,))
    db.desconectar()
    return {"mensagem": "Categoria Registrada!"}

@app.post('/ator_serie/{id_ator}/Series/{id_serie}')
def associar_ator_serie(id_ator: int, id_serie: int, personagem: str):
    db.conectar()
    sql = "INSERT INTO ator_serie (id_ator, id_serie, personagem) VALUES (%s, %s, %s)"
    db.executar(sql, (id_ator, id_serie, personagem))
    db.desconectar()
    return {"mensagem": "Cadastrado Meu Parceiro!"}


#Criando as rotas para listar os dados
@app.get("/Series/")
def listar_series():
    db.conectar()
    sql = "SELECT * FROM serie"
    series = db.executar(sql)
    db.desconectar()
    return series

@app.get("/Atores/")
def listar_atores():
    db.conectar()
    sql = "SELECT * FROM ator"
    atores = db.executar(sql)
    db.desconectar()
    return atores

@app.get("/Motivos/")
def listar_motivos():
    db.conectar()
    sql = "SELECT * FROM motivo_assistir"
    motivos = db.executar(sql)
    db.desconectar()
    return motivos

@app.get("/Categoria/")
def listar_categorias():
    db.conectar()
    sql = "SELECT * FROM categoria"
    categoria = db.executar(sql)
    db.desconectar()
    return categoria

@app.get("/Avaliacao/")
def listar_avaliacao():
    db.conectar()
    sql = "SELECT * FROM avaliacao_serie"
    avaliacao = db.executar(sql)
    db.desconectar()
    return avaliacao

@app.get("/Series/{id_serie}")
def listar_autores_associados(id_serie: int):
    db.conectar()
    sql = "SELECT * FROM ator_serie WHERE id_serie = %s"
    autores = db.executar(sql, (id_serie,))
    db.desconectar()
    return autores

#Criando as rotas para apagar os dados
@app.delete("/Atores/{id_ator}")
def deletar_ator(id_ator: int):
    db.conectar()
    sql = "DELETE FROM ator WHERE id_ator = %s"
    db.executar(sql, (id_ator,))
    db.desconectar()
    return {"mensagem": "Ator deletado com sucesso!"}

@app.delete("/Series/{id_serie}")
def deletar_serie(id_serie: int):
    db.conectar()
    sql = "DELETE FROM serie WHERE id_serie = %s"
    db.executar(sql, (id_serie,))
    db.desconectar()
    return {"mensagem": "Série deletada com sucesso!"}


@app.delete("/Motivos/{id_motivo}")
def deletar_motivo(id_motivo: int):
    db.conectar()
    sql = "DELETE FROM motivo_assistir WHERE id_motivo = %s"
    db.executar(sql, (id_motivo,))
    db.desconectar()
    return {"mensagem": "Motivo deletado com sucesso!"}

@app.delete("/Categoria/{id_categoria}")
def deletar_categoria(id_categoria: int):
    db.conectar()
    sql = "DELETE FROM categoria WHERE id_categoria = %s"
    db.executar(sql, (id_categoria,))
    db.desconectar()
    return {"mensagem": "Categoria deletada com sucesso!"}

@app.delete("/ator_serie/{id_ator}/Series/{id_serie}")
def deletar_ator_serie(id_ator: int, id_serie: int):
    db.conectar()
    sql = "DELETE FROM ator_serie WHERE id_ator = %s AND id_serie = %s"
    db.executar(sql, (id_ator, id_serie))
    db.desconectar()
    return {"mensagem": "Ator e série deletados com sucesso!"}

@app.delete("/Avaliacao/{id_avaliacao}")
def deletar_avaliacao(id_avaliacao: int):
    db.conectar()
    sql = "DELETE FROM avaliacao_serie WHERE id_avaliacao = %s"
    db.executar(sql, (id_avaliacao,))
    db.desconectar()
    return {"mensagem": "Avaliação deletada com sucesso!"}

#Criando as rotas para atualizar os dados
@app.put("/Series/{id_serie}")
def atualizar_serie(id_serie: int, id_categoria: int, serie: Serie):
    db.conectar()
    sql = "UPDATE serie SET titulo = %s, descricao = %s, ano_lancamento = %s, id_categoria = %s WHERE id_serie = %s"
    db.executar(sql, (serie.titulo, serie.descricao, serie.ano_lancamento, serie.id_categoria, id_serie))
    db.desconectar()
    return {"mensagem": "Série atualizada com sucesso!"}

@app.put("/Atores/{id_ator}")
def atualizar_ator(id_ator: int, ator: Ator):
    db.conectar()
    sql = "UPDATE ator SET nome = %s WHERE id_ator = %s"
    db.executar(sql, (ator.nome, id_ator))
    db.desconectar()
    return {"mensagem": "Ator atualizado com sucesso!"}

@app.put("/Motivos/{id_motivo}")
def atualizar_motivo(id_motivo: int, motivo: Motivo):
    db.conectar()
    sql = "UPDATE motivo_assistir SET id_serie = %s, motivo = %s WHERE id_motivo = %s"
    db.executar(sql, (motivo.id_serie, motivo.motivo, id_motivo))
    db.desconectar()
    return {"mensagem": "Motivo atualizado com sucesso!"}

@app.put("/Categoria/{id_categoria}")
def atualizar_categoria(id_categoria: int, categoria: Categoria):
    db.conectar()
    sql = "UPDATE categoria SET nome = %s WHERE id_categoria = %s"
    db.executar(sql, (categoria.nome, id_categoria))
    db.desconectar()
    return {"mensagem": "Categoria atualizada com sucesso!"}

@app.put("/Avaliacao/{id_avaliacao}")
def atualizar_avaliacao(id_avaliacao: int, avaliacao: Avaliacao):
    db.conectar()
    sql = "UPDATE avaliacao_serie SET id_serie = %s, nota = %s, comentario = %s WHERE id_avaliacao = %s"
    db.executar(sql, (avaliacao.id_serie, avaliacao.nota, avaliacao.comentario, id_avaliacao))
    db.desconectar()
    return {"mensagem": "Avaliação atualizada com sucesso!"}

@app.put("/ator_serie/{id_ator}/Series/{id_serie}")
def atualizar_ator_serie(id_ator: int, id_serie: int, personagem: str):
    db.conectar()
    sql = "UPDATE ator_serie SET personagem = %s WHERE id_ator = %s AND id_serie = %s"
    db.executar(sql, (personagem, id_ator, id_serie))
    db.desconectar()
    return {"mensagem": "Ator e série atualizados com sucesso!"}
