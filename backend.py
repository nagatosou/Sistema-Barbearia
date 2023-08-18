import csv
import random
from datetime import datetime, timedelta

class Backend:

    @staticmethod
    def gerar_codigo():
        return ''.join(random.choices('0123456789', k=3))

    def cadastrar(self, data, cpf, nome):
        codigo = self.gerar_codigo()
        with open('cadastros.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([codigo, data, cpf, nome])
        return codigo

    def consultar_todos_ids_e_nomes(self):
        id_nome_list = []
        with open('cadastros.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 4:
                    id_nome_list.append((row[0], row[3]))
        return id_nome_list

    def cadastrar_dados_adicionais(self, codigo, email, telefone, endereco):
        with open('dados_adicionais.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([codigo, email, telefone, endereco])


    def cadastrar_plano(self, codigo, duracao):
        data_inicio = datetime.now().strftime('%d/%m/%Y')
        data_fim = (datetime.strptime(data_inicio, '%d/%m/%Y') + timedelta(days=duracao)).strftime('%d/%m/%Y')
        with open('planos.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([codigo, data_inicio, data_fim, duracao])

    def verificar_dias_plano(self, codigo):
        data_atual = datetime.now()
        with open('planos.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 4 and row[0] == codigo:
                    data_fim = datetime.strptime(row[2], '%d/%m/%Y')
                    dias_restantes = (data_fim - data_atual).days
                    return dias_restantes
        return None
    
    def consultar_dados_adicionais(self, codigo):
        dados_adicionais = []
        with open('dados_adicionais.csv', 'r', newline='') as csvfile:
           reader = csv.reader(csvfile)
           for row in reader:
               if len(row) >= 1 and row[0] == codigo:
                dados_adicionais = row[1], row[2], row[3]
                break
        return dados_adicionais
    
    def consultar_plano(self, codigo):
      plano = []
      with open('planos.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 4 and row[0] == codigo:
                plano = row[3], row[1], row[2]  # Assume que os dados estão na ordem duracao, data_inicio, data_fim
                break  # Já encontrou o plano, pode sair do loop
      return plano
  
  
    def deletar_cadastro(self, codigo):
        registros = []
        with open('cadastros.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != codigo:
                    registros.append(row)
        with open('cadastros.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(registros)

    def deletar_dados_adicionais(self, codigo):
        registros = []
        with open('dados_adicionais.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != codigo:
                    registros.append(row)
        with open('dados_adicionais.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(registros)

    def deletar_plano(self, codigo):
        registros = []
        with open('planos.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] != codigo:
                    registros.append(row)
        with open('planos.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(registros)
            
            
            
            
    def atualizar_campo(self, codigo, campo, novo_valor):
        if campo in ['nome', 'cpf']:
            arquivo_csv = 'cadastros.csv'
        elif campo in ['email', 'endereco']:
            arquivo_csv = 'dados_adicionais.csv'
        elif campo == 'telefone':
            arquivo_csv = 'dados_adicionais.csv'
        else:
            return False

        registros = []
        with open(arquivo_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == codigo:
                    if campo == 'nome':
                        row[3] = novo_valor
                    elif campo == 'cpf':
                        row[2] = novo_valor
                    elif campo == 'email':
                        row[1] = novo_valor
                    elif campo == 'endereco':
                        row[3] = novo_valor
                    elif campo == 'telefone':
                        row[2] = novo_valor
                registros.append(row)

        with open(arquivo_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(registros)
            
            
    def produto_cadastro(self, data, nome_produto, quantidade):
        codigo = self.gerar_codigo()
        with open('estoque.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([codigo, data, nome_produto, quantidade])
        return codigo

    def listar_todos_ids_e_produtos(self):
        id_produto_list = []
        with open('estoque.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 4:
                    id_produto_list.append((row[0], row[2]))
        return id_produto_list


        return True



      
