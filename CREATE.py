import sqlite3 as sq

DB_PATH = 'alunos.db'

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                email TEXT UNIQUE,
                curso TEXT
             );
         ''')

if __name__ == '__main__':
    criar_tabela()
    print("Tabela criada ou já existia.")