from backend import Backend
from datetime import datetime

class CadastroController:
    def __init__(self):
        self.backend = Backend()
        self.campos_validos = ['nome', 'cpf', 'telefone']

    def formatar_data(self, data):
        try:
            data_obj = datetime.strptime(data, '%d%m%Y')
            return data_obj.strftime('%d/%m/%Y')
        except ValueError:
            print("Data inválida. Use o formato DDMMAAAA.")
            return None

    def cadastrar(self, data, cpf, nome):
        data_formatada = self.formatar_data(data)
        if data_formatada:
            codigo = self.backend.cadastrar(data_formatada, cpf, nome)
            return codigo
        return None

    def consultar_por_id(self, id):
        dados_adicionais = self.backend.consultar_dados_adicionais(id)  # Correção aqui
        if dados_adicionais:
            cadastro = self.backend.consultar_por_id(id)
            email, telefone, endereco = dados_adicionais  # Desempacote aqui
            return cadastro, (email, telefone, endereco)
        return None, None

    def deletar(self, codigo):
        success = self.backend.deletar(codigo)
        return success
    
    def atualizar_campo(self, codigo, campo, novo_valor):
        if campo == 'nome':
            return self.backend.atualizar_nome(codigo, novo_valor)
        elif campo == 'cpf':
            return self.backend.atualizar_cpf(codigo, novo_valor)
        elif campo == 'telefone':
            return self.backend.atualizar_telefone(codigo, novo_valor)
        else:
            return False
        
    def listar_todos_ids_e_nomes(self):
        id_nome_list = self.backend.consultar_todos_ids_e_nomes()
        return id_nome_list  
    
    def cadastrar_plano(self, codigo, duracao):
       self.backend.cadastrar_plano(codigo, duracao)

    def verificar_dias_plano(self, codigo):
        return self.backend.verificar_dias_plano(codigo)
    
    def consultar_dados_adicionais(self, id):
        return self.backend.consultar_dados_adicionais(id)
    
    def consultar_plano(self, codigo):
      dias_restantes = self.backend.verificar_dias_plano(codigo)
      if dias_restantes is not None:
        plano = self.backend.consultar_plano(codigo)
        return plano, dias_restantes
      return None, None
