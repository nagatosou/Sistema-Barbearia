import csv
import random

def gerar_codigo():
    return ''.join(random.choices('0123456789', k=3))

def cadastrar(data, cpf, nome, endereco, telefone):
    codigo = gerar_codigo()
    with open('cadastros.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([codigo, data, cpf, nome, endereco, telefone])
    return codigo

def consultar(codigo):
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 1 and row[0] == codigo:
                return row
    return None

def deletar(codigo):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 1 and row[0] == codigo:
                encontrado = True
            else:
                registros.append(row)
    
    if encontrado:
        with open('cadastros.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for registro in registros:
                writer.writerow(registro)
        return True
    else:
        return False

def atualizar(codigo, novo_data, novo_cpf, novo_nome):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == codigo:
                registros.append([codigo, novo_data, novo_cpf, novo_nome])
                encontrado = True
            else:
                registros.append(row)
    if encontrado:
        with open('cadastros.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for registro in registros:
                writer.writerow(registro)
        return True
    return False
