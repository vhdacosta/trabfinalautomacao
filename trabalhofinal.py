#Trabalho Final de Automação Industrial

import mysql.connector
from prettytable import PrettyTable
import requests

# Para rodar esse programa você deve rodar o balanca.py primeiro em python.
peso = requests.get('http://127.0.0.1:5000').json()["peso"]
db_connection = mysql.connector.connect(
    host='localhost', user='root', password='', database='phpmyadmin')
cursor = db_connection.cursor()

valorretirado = 5  # CONFIGURÁVEL

codigo_silos = {"Silo 1": "4782911109837",
                "Silo 2": "4782201942124",
                "Silo 3": "4782334190212",
                "Silo 4": "4782132000987",
                "Silo 5": "4788392029111"}

processo = int(input(f"Se você deseja adicionar ou atualizar algum produto no estoque, digite 1.\nSe você deseja retirar {valorretirado}kg de algum silo digite 2.\nSe você deseja uma lista com todos os produtos e suas respec. quantidades, digite 3.\n"))

#PROCESSO 1

if processo == 1:
    produto = str(
        input("Qual o nome do produto que está sendo colocado na balança?\n")).upper()
    cursor.execute(
        "SELECT * FROM `silos` WHERE `Produto` LIKE '{0}'".format(produto))
    check = cursor.fetchall()

    if check != []:
        oldpeso = int(check[0][2])
        for i in codigo_silos:
            if check[0][0] == codigo_silos[i]:
                print(f"Seu produto está no {i}\n")
                aux = int(input(
                    f"Deseja adicionar o peso {peso} a esse produto?\nDigite 1 para sim e 2 para não.\n"))
                if aux == 1:
                    cursor.execute("UPDATE `silos` SET `Peso`='{0}' WHERE `Produto`='{1}'".format(
                        peso+oldpeso, produto))
    else:
        cursor.execute(
            "SELECT * FROM `silos` WHERE `Produto` LIKE '{0}'".format(""))
        check = cursor.fetchall()
        if check != []:
            for i in codigo_silos:
                if codigo_silos[i] == check[0][0]:
                    print(
                        f"Seu produto será inserido no {i}, que está vazio.\nGuarde o código de barras para esse silo caso queira retirar seu produto.\nCódigo de Barras: {codigo_silos[i]}")
                    aux = codigo_silos[i]
            cursor.execute("UPDATE `silos` SET `Produto`='{0}',`Peso`='{1}' WHERE `Codigo`='{2}'".format(
                produto, peso, aux))
        else:
            print(
                f"Não há silos vazios para adicionar seu produto, esvazie algum primeiro!\n")
    db_connection.commit()

#PROCESSO 2

elif processo == 2:
    codigo = input(
        f"Qual o código do produto que você gostaria de retirar {valorretirado}kg?\n")
    cursor.execute(
        "SELECT * FROM `silos` WHERE `Codigo` LIKE '{0}'".format(codigo))
    check = cursor.fetchall()

    if check != []:
        oldpeso = int(check[0][2])
        if oldpeso >= valorretirado:
            aux = int(input(
                f"Seu produto {check[0][1]} tem o peso {check[0][2]} e ficará com peso {int(check[0][2])-valorretirado}.Deseja prosseguir?\nDigite 1 para sim e 2 para não.\n"))
            if aux == 1:
                cursor.execute("UPDATE `silos` SET `Peso`='{0}' WHERE `Codigo`='{1}'".format(
                    oldpeso-valorretirado, codigo))
        else:
            aux = input(
                f"Seu produto {check[0][1]} tem o peso {check[0][2]}, que é menor do que {valorretirado}, fazendo com que o silo fique vazio.Deseja prosseguir?\nDigite 1 para sim e 2 para não.\n")
            cursor.execute("UPDATE `silos` SET `Produto`='{0}',`Peso`='{1}' WHERE `Codigo`='{2}'".format(
                "", "", codigo))
    else:
        print("Esse código de barra não está inserido no programa. Tente novamente.")
    db_connection.commit()

#PROCESSO 3

cursor.execute('SELECT * FROM silos')
check = cursor.fetchall()
x = PrettyTable()
x.field_names = ["Silo", "Produto", "Peso"]
for i in range(len(check)):
    x.add_row(["Silo {0}".format(i+1), check[i][1], check[i][2]])
print(x)

# FINALIZAÇÃO DO PROGRAMA
cursor.close()
db_connection.commit()
db_connection.close()
