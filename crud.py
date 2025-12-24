from database import conexao

def adicionar_livro(titulo, autor, ano_publicacao):
    conn = conexao()
    cursor = conn.cursor()
    comando = """insert into livros (titulo, autor, ano_publicacao) values (?, ?, ?)"""
    cursor.execute(comando, (titulo, autor, ano_publicacao))
    conn.commit()
    conn.close()
    return f"Livro '{titulo}' adicionado com sucesso."

def listar_livros():
    conn = conexao()
    cursor = conn.cursor()
    comando = """select id, titulo, autor, ano_publicacao, status from livros"""
    cursor.execute(comando)
    livros = cursor.fetchall()
    conn.close()
    return livros

def atualizar_livro(id, titulo=None, autor=None, ano_publicacao=None, status=None):
    conn = conexao()
    cursor = conn.cursor()
    campos = []
    valores = []
    
    if titulo is not None:
        campos.append("titulo = ?")
        valores.append(titulo)
    if autor is not None:
        campos.append("autor = ?")
        valores.append(autor)
    if ano_publicacao is not None:
        campos.append("ano_publicacao = ?")
        valores.append(ano_publicacao)
    if status is not None:
        campos.append("status = ?")
        valores.append(status)
    
    valores.append(id)
    comando = f"""update livros set {', '.join(campos)} where id = ?"""
    cursor.execute(comando, tuple(valores))
    conn.commit()
    conn.close()
    return f"Livro com ID {id} atualizado com sucesso."