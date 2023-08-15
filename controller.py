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
        return False

    def deletar_cadastro_completo(self, codigo):
        cadastro_deletado = self.backend.deletar_cadastro(codigo)
        dados_adicionais_deletados = self.backend.deletar_dados_adicionais(codigo)
        plano_deletado = self.backend.deletar_plano(codigo)

        if cadastro_deletado and dados_adicionais_deletados and plano_deletado:
            return True
        else:
            return False

    
    def atualizar_campo(self, codigo, campo, novo_valor):
        return self.backend.atualizar_campo(codigo, campo, novo_valor)

        
    def listar_todos_ids_e_nomes(self):
        id_nome_list = self.backend.consultar_todos_ids_e_nomes()
        return id_nome_list  
    
    def cadastrar_plano(self, codigo, duracao):
       self.backend.cadastrar_plano(codigo, duracao)

    def verificar_dias_plano(self, codigo):
        return self.backend.verificar_dias_plano(codigo)
    
    def cadastrar_dados_adicionais(self, codigo, email, telefone, endereco):
        self.backend.cadastrar_dados_adicionais(codigo, email, telefone, endereco)
    
    def consultar_plano(self, codigo):
      dias_restantes = self.backend.verificar_dias_plano(codigo)
      if dias_restantes is not None:
        plano = self.backend.consultar_plano(codigo)
        return plano, dias_restantes
      return None, None
