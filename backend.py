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
    
    def consultar_dados_adicionais(self, id):
        with open('dados_adicionais.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 1 and row[0] == id:
                    email, telefone, endereco = row[1], row[2], row[3]
                    return email, telefone, endereco
        return None  # Retornar None se os dados não forem encontrados
    
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
        arquivo_csv = None

        if campo in ['nome', 'cpf']:
            arquivo_csv = 'cadastros.csv'
        elif campo in ['email', 'endereco', 'telefone']:
            arquivo_csv = 'dados_adicionais.csv'
        else:
            return False

        with open(arquivo_csv, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        for row in rows:
            if row[0] == codigo:
                index = rows.index(row)
                if campo in ['nome']:
                    rows[index][3] = novo_valor
                elif campo in ['cpf']:
                    rows[index][2] = novo_valor
                elif campo in ['email', 'endereco', 'telefone']:
                    if campo == 'email':
                        rows[index][1] = novo_valor
                    elif campo == 'endereco':
                        rows[index][2] = novo_valor
                    elif campo == 'telefone':
                        rows[index][2] = novo_valor
                break

        with open(arquivo_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        return True
     
            
            
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




      
