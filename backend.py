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

def atualizar_nome(codigo, novo_nome):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == codigo:
                row[3] = novo_nome
                registros.append(row)
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

def atualizar_cpf(codigo, novo_cpf):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == codigo:
                row[2] = novo_cpf
                registros.append(row)
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

def atualizar_telefone(codigo, novo_telefone):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == codigo:
                row[4] = novo_telefone
                registros.append(row)
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

def atualizar_campo(self, codigo, campo, novo_valor):
    registros = []
    encontrado = False
    with open('cadastros.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == codigo:
                row[self.campos_indices[campo]] = novo_valor
                registros.append(row)
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
