import os
import psycopg
from flask import flask

app = flask(__name__)
BANCO = os.environ["DATABASE_URL"]

@app.route("/")
def inicio():
    return "API com banco de dados!"

@app.route("/visitas")
def visitas():
    with psycopg.connect(BANCO) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY)")
        conn.execute("INSERT INTO visitas DEFAULT VALUES")
        total = conn.execute("SELECT COUNT(*) FROM visitas").fetchone()[0]
    return {"visitas": total}

app.run(host="0.0.0.0", port=3000)