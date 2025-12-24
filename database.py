import sqlite3
from datetime import datetime

def conexao(nome="biblioteca.db"):
    return sqlite3.connect(nome)

def testar_conexao():
    try:
        conn = conexao()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False
    
def criar_tabelas():
    comandos = [
        """CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER,
            lido BOOLEAN DEFAULT 0
        )""",
        """CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao TEXT,
            FOREIGN KEY (livro_id) REFERENCES livros(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )"""
    ]

    conn = conexao()
    cursor = conn.cursor()
    for comando in comandos:
        cursor.execute(comando)
    conn.commit()
    conn.close()
    return f"Tabelas criadas com sucesso."

if __name__ == "__main__":
    if testar_conexao():
        print("Conexão com o banco de dados bem-sucedida.")
        mensagem = criar_tabelas()
        print(mensagem)
    else:
        print("Falha na conexão com o banco de dados.")