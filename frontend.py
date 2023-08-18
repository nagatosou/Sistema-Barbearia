import tkinter as tk
from controller import CadastroController

class Application:
    def __init__(self, root):
        self.controller = CadastroController()

        self.root = root
        self.root.title("Sistema de Cadastro e Estoque")
        self.root.geometry('700x450')

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Menu Principal:")
        self.label.pack()

        self.cadastro_button = tk.Button(self.root, text="Acessar Menu de Cadastro", command=self.create_menu_cadastro)
        self.cadastro_button.pack()

        self.estoque_button = tk.Button(self.root, text="Acessar Menu de Estoque de Produtos", command=self.create_menu_estoque)
        self.estoque_button.pack()

        self.sair_button = tk.Button(self.root, text="Sair do Programa", command=self.root.quit)
        self.sair_button.pack()

    def create_menu_cadastro(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Menu de Cadastro:")
        self.label.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack()

        self.consultar_button = tk.Button(self.root, text="Consultar", command=self.consultar)
        self.consultar_button.pack()

        self.deletar_button = tk.Button(self.root, text="Deletar", command=self.deletar)
        self.deletar_button.pack()

        self.atualizar_button = tk.Button(self.root, text="Atualizar", command=self.atualizar)
        self.atualizar_button.pack()

        self.cadastrar_plano_button = tk.Button(self.root, text="Cadastrar Plano", command=self.cadastrar_plano)
        self.cadastrar_plano_button.pack()

        self.consultar_plano_button = tk.Button(self.root, text="Consultar Plano", command=self.consultar_plano)
        self.consultar_plano_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu Principal", command=self.create_main_menu)
        self.voltar_button.pack()

    def create_menu_estoque(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Menu de Estoque de Produtos:")
        self.label.pack()

        # Implemente as opções do menu de estoque aqui

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu Principal", command=self.create_main_menu)
        self.voltar_button.pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def cadastrar(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Cadastrar:")
        self.label.pack()

        self.data_label = tk.Label(self.root, text="Digite a data de cadastro (DDMMAAAA):")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack()

        self.cpf_label = tk.Label(self.root, text="Digite o CPF:")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack()

        self.nome_label = tk.Label(self.root, text="Digite o nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.realizar_cadastro)
        self.cadastrar_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_cadastro(self):
        data = self.data_entry.get()
        cpf = self.cpf_entry.get()
        nome = self.nome_entry.get()

        codigo = self.controller.cadastrar(data, cpf, nome)
        if codigo:
            self.result_label = tk.Label(self.root, text="Cadastro realizado com sucesso!")
            self.result_label.pack()
            self.codigo_label = tk.Label(self.root, text=f"Número de cadastro gerado: {codigo}")
            self.codigo_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Erro ao cadastrar.")
            self.result_label.pack()
            
    def create_menu_cadastro(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Menu de Cadastro:")
        self.label.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack()

        self.cadastrar_dados_button = tk.Button(self.root, text="Cadastrar Dados Adicionais", command=self.cadastrar_dados_adicionais)
        self.cadastrar_dados_button.pack()

        self.consultar_button = tk.Button(self.root, text="Consultar", command=self.consultar)
        self.consultar_button.pack()
            
    def create_menu_cadastro(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Menu de Cadastro:")
        self.label.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.cadastrar_button.pack()

        self.cadastrar_dados_button = tk.Button(self.root, text="Cadastrar Dados Adicionais", command=self.cadastrar_dados_adicionais)
        self.cadastrar_dados_button.pack()

        self.consultar_button = tk.Button(self.root, text="Consultar", command=self.consultar)
        self.consultar_button.pack()

        self.deletar_button = tk.Button(self.root, text="Deletar", command=self.deletar)
        self.deletar_button.pack()

        self.atualizar_button = tk.Button(self.root, text="Atualizar", command=self.atualizar)
        self.atualizar_button.pack()

        self.cadastrar_plano_button = tk.Button(self.root, text="Cadastrar Plano", command=self.cadastrar_plano)
        self.cadastrar_plano_button.pack()

        self.consultar_plano_button = tk.Button(self.root, text="Consultar Plano", command=self.consultar_plano)
        self.consultar_plano_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu Principal", command=self.create_main_menu)
        self.voltar_button.pack()

    def cadastrar_dados_adicionais(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Cadastrar Dados Adicionais:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o código do cadastro:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.email_label = tk.Label(self.root, text="Digite o email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.telefone_label = tk.Label(self.root, text="Digite o telefone:")
        self.telefone_label.pack()
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack()

        self.endereco_label = tk.Label(self.root, text="Digite o endereço:")
        self.endereco_label.pack()
        self.endereco_entry = tk.Entry(self.root)
        self.endereco_entry.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.realizar_cadastro_dados_adicionais)
        self.cadastrar_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_cadastro_dados_adicionais(self):
        codigo = self.codigo_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()

        self.controller.cadastrar_dados_adicionais(codigo, email, telefone, endereco)
        self.result_label = tk.Label(self.root, text="Informações adicionais cadastradas com sucesso.")
        self.result_label.pack()   

    def consultar(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Consultar:")
        self.label.pack()

        id_nome_list = self.controller.listar_todos_ids_e_nomes()
        if id_nome_list:
            self.result_label = tk.Label(self.root, text="IDs e nomes das pessoas cadastradas:")
            self.result_label.pack()
            for id, nome in id_nome_list:
                label = tk.Label(self.root, text=f"ID: {id}, Nome: {nome}")
                label.pack()

            self.sub_opcao_label = tk.Label(self.root, text="Digite 1 para consultar dados adicionais pelo ID, ou 0 para retornar ao menu principal:")
            self.sub_opcao_label.pack()
            self.sub_opcao_entry = tk.Entry(self.root)
            self.sub_opcao_entry.pack()

            self.consultar_button = tk.Button(self.root, text="Consultar", command=self.realizar_consulta_dados_adicionais)
            self.consultar_button.pack()
        else:
            self.result_label = tk.Label(self.root, text="Nenhum cadastro encontrado.")
            self.result_label.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_consulta_dados_adicionais(self):
        id_consulta = self.sub_opcao_entry.get()
        dados_adicionais = self.controller.consultar_dados_adicionais(id_consulta)
        if dados_adicionais:
            self.result_label = tk.Label(self.root, text="Dados Adicionais:")
            self.result_label.pack()
            email_label = tk.Label(self.root, text=f"Email: {dados_adicionais[0]}")
            email_label.pack()
            telefone_label = tk.Label(self.root, text=f"Telefone: {dados_adicionais[1]}")
            telefone_label.pack()
            endereco_label = tk.Label(self.root, text=f"Endereço: {dados_adicionais[2]}")
            endereco_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Dados adicionais não encontrados.")
            self.result_label.pack()

    def cadastrar_dados_adicionais(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Cadastrar Dados Adicionais:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o código do cadastro:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.email_label = tk.Label(self.root, text="Digite o email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.telefone_label = tk.Label(self.root, text="Digite o telefone:")
        self.telefone_label.pack()
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack()

        self.endereco_label = tk.Label(self.root, text="Digite o endereço:")
        self.endereco_label.pack()
        self.endereco_entry = tk.Entry(self.root)
        self.endereco_entry.pack()

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.realizar_cadastro_dados_adicionais)
        self.cadastrar_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_cadastro_dados_adicionais(self):
        codigo = self.codigo_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()

        self.controller.cadastrar_dados_adicionais(codigo, email, telefone, endereco)
        self.result_label = tk.Label(self.root, text="Informações adicionais cadastradas com sucesso.")
        self.result_label.pack()

    def deletar(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Deletar:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o código do cadastro a ser deletado:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.deletar_button = tk.Button(self.root, text="Deletar", command=self.realizar_delecao)
        self.deletar_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_delecao(self):
        codigo = self.codigo_entry.get()
        if self.controller.deletar_cadastro_completo(codigo):
            self.result_label = tk.Label(self.root, text="Cadastro deletado com sucesso.")
            self.result_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Cadastro não encontrado.")
            self.result_label.pack()

    def atualizar(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Atualizar:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o código do cadastro a ser atualizado:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.campos_disponiveis = ["nome", "cpf", "email", "endereco", "telefone"]
        self.campos_disponiveis_label = tk.Label(self.root, text=f"Campos disponíveis para atualização: {', '.join(self.campos_disponiveis)}")
        self.campos_disponiveis_label.pack()

        self.campo_label = tk.Label(self.root, text="Digite o campo que deseja atualizar:")
        self.campo_label.pack()
        self.campo_entry = tk.Entry(self.root)
        self.campo_entry.pack()

        self.novo_valor_label = tk.Label(self.root, text="Digite o novo valor:")
        self.novo_valor_label.pack()
        self.novo_valor_entry = tk.Entry(self.root)
        self.novo_valor_entry.pack()

        self.atualizar_button = tk.Button(self.root, text="Atualizar", command=self.realizar_atualizacao)
        self.atualizar_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_atualizacao(self):
        codigo = self.codigo_entry.get()
        campo = self.campo_entry.get()
        novo_valor = self.novo_valor_entry.get()

        if campo in self.campos_disponiveis:
            if self.controller.atualizar_campo(codigo, campo, novo_valor):
                self.result_label = tk.Label(self.root, text="Cadastro atualizado com sucesso.")
                self.result_label.pack()
            else:
                self.result_label = tk.Label(self.root, text="Cadastro não encontrado ou campo inválido.")
                self.result_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Campo inválido.")
            self.result_label.pack()

    def cadastrar_plano(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Cadastrar Plano:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o ID do cadastro:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.duracao_label = tk.Label(self.root, text="Digite a duração do plano (30, 60 ou 90 dias):")
        self.duracao_label.pack()
        self.duracao_entry = tk.Entry(self.root)
        self.duracao_entry.pack()

        self.cadastrar_plano_button = tk.Button(self.root, text="Cadastrar Plano", command=self.realizar_cadastro_plano)
        self.cadastrar_plano_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_cadastro_plano(self):
        codigo = self.codigo_entry.get()
        duracao = int(self.duracao_entry.get())

        if duracao in [30, 60, 90]:
            self.controller.cadastrar_plano(codigo, duracao)
            self.result_label = tk.Label(self.root, text="Plano cadastrado com sucesso.")
            self.result_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Duração inválida. Escolha entre 30, 60 ou 90 dias.")
            self.result_label.pack()

    def consultar_plano(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Consultar Plano:")
        self.label.pack()

        self.codigo_label = tk.Label(self.root, text="Digite o ID do cadastro para consultar o plano:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.pack()

        self.consultar_plano_button = tk.Button(self.root, text="Consultar Plano", command=self.realizar_consulta_plano)
        self.consultar_plano_button.pack()

        self.voltar_button = tk.Button(self.root, text="Voltar ao Menu de Cadastro", command=self.create_menu_cadastro)
        self.voltar_button.pack()

    def realizar_consulta_plano(self):
        codigo = self.codigo_entry.get()
        plano, dias_restantes = self.controller.consultar_plano(codigo)
        if plano:
            self.result_label = tk.Label(self.root, text="Plano Atual:")
            self.result_label.pack()
            duracao_label = tk.Label(self.root, text=f"Duração: {plano[0]} dias")
            duracao_label.pack()
            inicio_label = tk.Label(self.root, text=f"Data de Início: {plano[1]}")
            inicio_label.pack()
            fim_label = tk.Label(self.root, text=f"Data de Término: {plano[2]}")
            fim_label.pack()
            dias_restantes_label = tk.Label(self.root, text=f"Dias Restantes: {dias_restantes}")
            dias_restantes_label.pack()
        else:
            self.result_label = tk.Label(self.root, text="Plano não encontrado.")
            self.result_label.pack()

    # Implemente as demais funções de funcionalidades de estoque

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
