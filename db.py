import sqlite3
from config import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                tipo TEXT,
                valor REAL,
                conforme TEXT,
                horario TEXT
            );
        ''')

def guardar_resultado(timestamp, tipo, valor, conforme, horario):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            INSERT INTO resultados (timestamp, tipo, valor, conforme, horario)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, tipo, valor, conforme, horario))
