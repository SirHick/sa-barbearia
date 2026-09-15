from flask import Flask, render_template, request
import agendamentos

app = Flask(__name__)


# 1. Rota / : Início, nome barbearia, nº agendamentos
@app.route("/")
def index():
    nome_barbearia = "Barbearia Estilo & Corte"
    total_agendamentos = agendamentos.contar_agendamentos()

    return render_template(
        "index.html",
        nome_barbearia=nome_barbearia,
        total=total_agendamentos,
    )


# 2. Rota /agendamentos : Tabela com todos agendamentos
@app.route("/agendamentos")
def rota_agendamentos():
    lista = agendamentos.listar_agendamentos()
    return render_template("agendamentos.html", agendamentos=lista)


# 3. Rota /agendamentos/status/ : Agendamentos filtrados por status
@app.route("/agendamentos/status/")
def status_agendamentos():
    # Pega o parâmetro via Query String (ex: /agendamentos/status/?status=Pendente)
    status_filtro = request.args.get("status")

    if status_filtro:
        lista = agendamentos.listar_por_status(status_filtro)
    else:
        lista = agendamentos.listar_agendamentos()

    return render_template(
        "agendamentos_status.html",
        agendamentos=lista,
        status_atual=status_filtro,
    )


# 4. Rota /agendamento/ : Detalhe de um agendamento
@app.route("/agendamento/")
@app.route("/agendamento/<int:id_agendamento>")
def detalhe(id_agendamento=None):
    # Permite buscar por rota (/agendamento/1) ou por Query String (/agendamento/?id=1)
    if not id_agendamento:
        id_agendamento = request.args.get("id", type=int)

    agendamento_item = (
        agendamentos.buscar_agendamento(id_agendamento)
        if id_agendamento
        else None
    )

    return render_template("detalhe.html", agendamento=agendamento_item)


if __name__ == "__main__":
    app.run(debug=True)