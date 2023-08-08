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
            data = input("Digite a data de cadastro (DDMMAAAA): ")
            cpf = input("Digite o CPF: ")
            nome = input("Digite o nome: ")
            endereco = input("Digite o endereço: ")
            telefone = input("Digite o telefone: ")
            
            codigo = controller.cadastrar(data, cpf, nome, endereco, telefone)
            if codigo:
                print("Cadastro realizado com sucesso!")
                print("Número de cadastro gerado:", codigo)
            else:
                print("Erro ao cadastrar.")
        
        elif opcao == '2':
            codigo = input("Digite o código do cadastro: ")
            cadastro = controller.consultar(codigo)
            if cadastro:
                print("Código:", cadastro[0])
                print("Data de Cadastro:", cadastro[1])
                print("CPF:", cadastro[2])
                print("Nome:", cadastro[3])
                print("Endereço:", cadastro[4])
                print("Telefone:", cadastro[5])
            else:
                print("Cadastro não encontrado.")
                
        elif opcao == '3':
            codigo = input("Digite o código do cadastro a ser deletado: ")
            if controller.deletar(codigo):
                print("Cadastro deletado com sucesso.")
            else:
                print("Cadastro não encontrado.")
                
        elif opcao == '4':
            codigo = input("Digite o código do cadastro a ser atualizado: ")
            novo_data = input("Digite a nova data de cadastro (DD/MM/AAAA): ")
            novo_cpf = input("Digite o novo CPF: ")
            novo_nome = input("Digite o novo nome: ")
            if controller.atualizar(codigo, novo_data, novo_cpf, novo_nome):
                print("Cadastro atualizado com sucesso.")
            else:
                print("Cadastro não encontrado.")
                
        elif opcao == '0':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
