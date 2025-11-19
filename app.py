from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# ============================
# DADOS DE EXEMPLO
# ============================

pacientes = [
    {
        "id": 1,
        "nome": "Cesar Alves",
        "idade": 17,
        "condicao": "Perna Quebrada",
        "imagem": "https://avatars.githubusercontent.com/u/225071834?s=400&u=38703be4eca876451f24ff61c82a1a7bd7124c37&v=4"
    },
    {
        "id": 2,
        "nome": "Paulo Varelo",
        "idade": 23,
        "condicao": "Diabetes Tipo 2",
        "imagem": "https://avatars.githubusercontent.com/u/61802190?v=4"
    }
]

medicos = [
    {
        "id": 1,
        "nome": "Dra. Ana Luisa",
        "especialidade": "Cardiologia",
        "experiencia": 20,
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPd1ag04qAxUqyFsA1waifXN9eNnce45gdKQ&s"
    },
    {
        "id": 2,
        "nome": "Dr. Carlinhos",
        "especialidade": "Endocrinologia",
        "experiencia": 15,
        "imagem": "data:image/jpeg;base64,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"
    }
]

# ============================
# ROTAS
# ============================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pacientes")
def listar_pacientes():
    return render_template("listar_pacientes.html", pacientes=pacientes)

@app.route("/medicos")
def listar_medicos():
    return render_template("listar_medicos.html", medicos=medicos)

@app.route("/paciente/<int:paciente_id>")
def detalhe_paciente(paciente_id):
    for paciente in pacientes:
        if paciente["id"] == paciente_id:
            return render_template("detalhe_paciente.html", paciente=paciente)
    abort(404)

@app.route("/medico/<int:medico_id>")
def detalhe_medico(medico_id):
    for medico in medicos:
        if medico["id"] == medico_id:
            return render_template("detalhe_medico.html", medico=medico)
    abort(404)

# ============================
# EXECUÇÃO
# ============================

if __name__ == "__main__":
    app.run(debug=True)
