import backend
from datetime import datetime

class CadastroController:
    def __init__(self):
        self.backend = backend

    def formatar_data(self, data):
        try:
            data_obj = datetime.strptime(data, '%d%m%Y')
            return data_obj.strftime('%d/%m/%Y')
        except ValueError:
            print("Data inválida. Use o formato DDMMAAAA.")
            return None

    def cadastrar(self, data, cpf, nome, endereco, telefone):
        data_formatada = self.formatar_data(data)
        if data_formatada:
            codigo = self.backend.cadastrar(data_formatada, cpf, nome, endereco, telefone)
            return codigo
        return None

    def consultar(self, codigo):
        cadastro = self.backend.consultar(codigo)
        return cadastro

    def deletar(self, codigo):
        success = self.backend.deletar(codigo)
        return success

    def atualizar(self, codigo, novo_data, novo_cpf, novo_nome):
        success = self.backend.atualizar(codigo, novo_data, novo_cpf, novo_nome)
        return success
