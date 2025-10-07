import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def atualizar_aluno(aluno_id, nome, idade, email, curso):
    """Atualiza os dados de um aluno pelo ID. Retorna quantas linhas foram alteradas."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            '''
            UPDATE alunos
            SET nome = ?, idade = ?, email = ?, curso = ?
            WHERE id = ?
            ''',
            (nome, idade, email, curso, aluno_id)
        )
        conn.commit()
        return cur.rowcount  # número de linhas modificadas

if __name__ == '__main__':
    print("Atualizando aluno")
    aluno_id = int(input("Digite o id para alterar: "))
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    email = input("Digite o email: ")
    curso = input("Digite o curso: ")

    qtd = atualizar_aluno(aluno_id, nome, idade, email, curso)
    if qtd:
        print(f"{qtd} registro(s) atualizado(s).")
    else:
        print("Nenhum registro foi alterado.")