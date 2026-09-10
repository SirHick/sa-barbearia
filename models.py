class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data_agendamento, status_agendamento):
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data_agendamento = data_agendamento
        self.status_agendamento = status_agendamento

    def exibir(self):
        print(f"Cliente: {self.cliente} | Telefone: {self.telefone} | Serviço: {self.servico} | Preço: {self.preco} | Barbeiro: {self.barbeiro} | Data: {self.data_agendamento} | Status: {self.status_agendamento}")

    def converte_tupla(self):
        return self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data_agendamento, self.status_agendamento

    @staticmethod
    def reverte_tupla(tupla):
        agendamento = Agendamento(
            cliente = tupla[1],
            telefone = tupla[2],
            servico = tupla[3],
            preco = tupla[4],
            barbeiro = tupla[5],
            data_agendamento = tupla[6],
            status_agendamento = tupla[7]
        )
        agendamento.id = tupla[0]
        return agendamento