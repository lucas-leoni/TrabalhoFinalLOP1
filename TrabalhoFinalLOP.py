'''Faça um programa que preencha um vetor com os modelos de 
10 carros (exemplos de modelos: Fusca, Gol, etc). Carregue 
outro vetor com o consumo desses carros, isto é, quantos 
quilômetros cada um deles faz com um litro de combustível, 
calcule e mostre: a- O modelo de carro mais econômico e o 
menos econômico; b- quantos litros de combustível cada um 
dos carros cadastrados consome para percorrer uma distância
de 500 quilômetros;'''
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    return 0
def menu():
    print("\n \n \t \t \t PROGRAMA CARROS \n \n")
    print("\t \t ESCOLHA UMA DAS OPÇÕES \n \n")
    print("\t 1- Mostrar o modelo de carro mais econômico e o menos econômico.\n") 
    print("\t 2- Mostrar quantos litros de combustível cada um dos carros consome para percorrer 500 quilômetros.\n")
    print("\t 3- Sair do programa.\n \n")
    return 0
def entrada_dados():
    opcao = int(input())
    if ( opcao <= 0 ):
        exit()
    if ( opcao >= 3 ):
        exit()
    limpar_tela()
    modelos = []
    print("\n \t Digite os modelos de carros:\n ")
    for i in range(10):
        modelos.append(str(input()))
    limpar_tela()
    print("\n \t Esses foram os modelos inseridos: ",modelos)
    consumos = []
    print("\n \t Digite o consumo dos carros:\n ")
    for i in range(10):
        consumos.append(float(input()))
    limpar_tela()
    print("\n \t Esses foram os consumos inseridos: ",consumos,"\n")
    while ( opcao != 3 ):
        if ( opcao == 1 ):
            calculo_opcao_1(opcao,modelos,consumos)
            outra_operacao()
            menu()
            opcao = int(input())
            limpar_tela()
        if ( opcao == 2 ):
            calculo_opcao_2(opcao,modelos,consumos)
            outra_operacao()
            menu()
            opcao = int(input())
            limpar_tela()
    return 0
def calculo_opcao_1(opcao,modelos,consumos):
    if ( opcao == 1 ):
        mais_economico = -1
        for i in range(10):
            if ( consumos[i] > mais_economico ):
                modelo = modelos[i]
                mais_economico = consumos[i]
    print("\n \t O modelo mais econômico é: ",modelo,"=",mais_economico,"KM/L")
    menos_economico = 999999
    for i in range(10):
        if ( consumos[i] < menos_economico ):
            modelo = modelos[i]
            menos_economico = consumos[i]
    return print("\n \t O modelo menos econômico é: ",modelo,"=",menos_economico,"KM/L")
def calculo_opcao_2(opcao,modelos,consumos):
    if ( opcao == 2 ):
        quilometros = 500
        print()
        for i in range(10):
            modelo = modelos[i]
            litros = quilometros / consumos[i]
            print("\t O modelo",modelo,"consome {:.2f}".format(litros),"litros de combustível para percorrer 500 quilômetros")
    return 0
def outra_operacao():
    print("\n \t Deseja realizar outra operação ? (s/n)\n")
    operacao = str(input())
    if ( operacao == "s" ) or ( operacao == "S" ):
        limpar_tela()
    else:
        exit()
    return 0
menu()
entrada_dados()