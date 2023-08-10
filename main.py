from controller import CadastroController

def main():
    controller = CadastroController()

    while True:
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Deletar")
        print("4. Atualizar")
        print("0. Sair")
        
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
            else:
                print("Nenhum cadastro encontrado.")
                
        elif opcao == '3':
            codigo = input("Digite o código do cadastro a ser deletado: ")
            if controller.deletar(codigo):
                print("Cadastro deletado com sucesso.")
            else:
                print("Cadastro não encontrado.")
                
        elif opcao == '4':
            codigo = input("Digite o código do cadastro a ser atualizado: ")
            print("Campos disponíveis para atualização:", ", ".join(controller.campos_validos))
            campo = input("Digite o campo que deseja atualizar: ")
            
            if campo in controller.campos_validos:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                if controller.atualizar_campo(codigo, campo, novo_valor):
                    print(f"{campo.capitalize()} atualizado com sucesso.")
                else:
                    print("Cadastro não encontrado.")
            else:
                print("Campo inválido.")
                
        elif opcao == '0':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
