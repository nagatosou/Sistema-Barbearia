from controller import CadastroController

def main():
    controller = CadastroController()

    while True:
        print("Menu Principal:")
        print("1. Acessar Menu de Cadastro")
        print("2. Acessar Menu de Estoque de Produtos")
        print("0. Sair do Programa")

        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == '1':
            menu_cadastro(controller)
        elif opcao_principal == '2':
            menu_estoque(controller)
        elif opcao_principal == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
    
    

def menu_cadastro(controller):
    while True:
        print("Menu de Cadastro:")
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Deletar")
        print("4. Atualizar")
        print("5. Cadastrar plano")
        print("6. Consultar plano")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("1. Criar novo cadastro")
            print("2. Cadastrar informações adicionais")
            sub_opcao = input("Escolha uma sub-opção: ")

            if sub_opcao == '1':
                data = input("Digite a data de cadastro (DDMMAAAA): ")
                cpf = input("Digite o CPF: ")
                nome = input("Digite o nome: ")

                codigo = controller.cadastrar(data, cpf, nome)
                if codigo:
                    print("Cadastro realizado com sucesso!")
                    print("Número de cadastro gerado:", codigo)
                else:
                    print("Erro ao cadastrar.")

            elif sub_opcao == '2':
                codigo = input("Digite o código do cadastro: ")
                email = input("Digite o email: ")
                telefone = input("Digite o telefone: ")
                endereco = input("Digite o endereço: ")

                controller.cadastrar_dados_adicionais(codigo, email, telefone, endereco)
                print("Informações adicionais cadastradas com sucesso.")

            else:
                print("Opção inválida.")

        elif opcao == '2':
            id_nome_list = controller.listar_todos_ids_e_nomes()
            if id_nome_list:
                print("IDs e nomes das pessoas cadastradas:")
                for id, nome in id_nome_list:
                    print(f"ID: {id}, Nome: {nome}")

                sub_opcao = input("Digite 1 para consultar dados adicionais pelo ID, ou 0 para retornar ao menu principal: ")

                if sub_opcao == '1':
                   id_consulta = input("Digite o ID do cadastro que deseja consultar os dados adicionais: ")
                   cadastro, dados_adicionais = controller.consultar_dados_adicionais(id_consulta)

                if dados_adicionais:
                   print("Dados Adicionais:")
                   print(f"Email: {dados_adicionais[0]}, Telefone: {dados_adicionais[1]}, Endereço: {dados_adicionais[2]}")
                else:
                   print("Dados adicionais não encontrados.")

        elif opcao == '3':
            codigo = input("Digite o código do cadastro a ser deletado: ")
            if controller.deletar_cadastro_completo(codigo):
               print("Cadastro deletado com sucesso.")       
            else:
                print("Cadastro não encontrado.")

        elif opcao == '4':
            codigo = input("Digite o código do cadastro a ser atualizado: ")
            campos_disponiveis = ["nome", "cpf", "email", "endereco", "telefone"]
            print("Campos disponíveis para atualização:", ", ".join(campos_disponiveis))
            campo = input("Digite o campo que deseja atualizar: ")
            if campo in campos_disponiveis:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                if controller.atualizar_campo(codigo, campo, novo_valor):
                    print("Cadastro atualizado com sucesso.")
                else:
                    print("Cadastro não encontrado ou campo inválido.")
            else:
                print("Campo inválido.")
                      
        elif opcao == '5':
            codigo = input("Digite o ID do cadastro: ")
            duracao = int(input("Digite a duração do plano (30, 60 ou 90 dias): "))

            if duracao in [30, 60, 90]:
                controller.cadastrar_plano(codigo, duracao)
                print("Plano cadastrado com sucesso.")
            else:
                print("Duração inválida. Escolha entre 30, 60 ou 90 dias.")
                
                
        elif opcao == '6':
          codigo = input("Digite o ID do cadastro para consultar o plano: ")
          plano, dias_restantes = controller.consultar_plano(codigo)
          if plano:
           print("Plano Atual:")
           print(f"Duração: {plano[0]} dias")
           print(f"Data de Início: {plano[1]}")
           print(f"Data de Término: {plano[2]}")
           print(f"Dias Restantes: {dias_restantes}")
          else:
           print("Plano não encontrado.")      

        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_estoque(controller):
    while True:
        print("Menu de Estoque de Produtos:")
        print("1. Cadastrar Produto")
        print("2. Consultar Estoque")
        print("3. Atualizar Estoque")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
                data = input("Digite a data de cadastro (DDMMAAAA): ")
                nome_produto = input("Digite o Nome do produto: ")
                quantidade = input("Digite Quantidade: ")

                codigo = controller.produto_cadastro(data, nome_produto, quantidade)
                
                if codigo:
                    print("Cadastro realizado com sucesso!")
                    print("Codigo produto gerado:", codigo)
                else:
                    print("Erro ao cadastrar.")
                pass
        elif opcao == '2':
            id_produtos_list = controller.listar_todos_ids_e_produtos()
            if id_produtos_list:
                print("IDs e produtos cadastrados:")
                for id, produto in id_produtos_list:
                    print(f"ID: {id}, produto: {produto}")
            pass
        elif opcao == '3':
            # Implementação da atualização de estoque aqui
            pass
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
