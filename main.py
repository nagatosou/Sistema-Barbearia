from controller import CadastroController

def main():
    controller = CadastroController()

    while True:
        print("1. Cadastrar")
        print("2. Consultar")
        print("3. Deletar")
        print("4. Atualizar")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")  # Adicione esta linha para ler a opção
        
        if opcao == '1':
            # ... Seu código para ler os dados do usuário ...

            codigo = controller.cadastrar(data, cpf, nome, endereco, telefone)
            if codigo:
                print("Cadastro realizado com sucesso!")
                print("Número de cadastro gerado:", codigo)
            else:
                print("Erro ao cadastrar.")
        
        elif opcao == '2':
            # ... Seu código para ler o código de cadastro ...

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
            # ... Seu código para ler o código de cadastro ...

            if controller.deletar(codigo):
                print("Cadastro deletado com sucesso.")
            else:
                print("Cadastro não encontrado.")

        elif opcao == '4':
            # ... Seu código para ler os dados do usuário ...

            if controller.atualizar(codigo, novo_data, novo_cpf, novo_nome):
                print("Cadastro atualizado com sucesso.")
            else:
                print("Cadastro não encontrado.")

        # ... Resto do seu código ...

if __name__ == "__main__":
    main()
