import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def inserir_aluno(nome: str, idade: int, email: str,curso: str) -> int:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO alunos (nome,idade,email,curso)VALUES (?,?,?,?)',(nome,idade,email,curso))
        conn.commit()
        return cur.lastrowid
    
if __name__ == '__main__':
    #bem vindo ao banco de dados
    print("### BEM VINDO AO DE DADOS ###")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    email= input("Digite o email: ")
    curso= input("Digite o curso: ")

    novo_id = inserir_aluno(nome,idade,email,curso)