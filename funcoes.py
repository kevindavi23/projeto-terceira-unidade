import numpy as np
import matplotlib.pyplot as plt
import json
def verificar_senha(senha1, senha2):
    if(senha1 == senha2):
        return True
    else:
        return False
def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if(user['email']== email):
            existe = True
            break
    return existe
def verificar_senha_correta(senha, usuarios):
    existe = False
    for user in usuarios:
        if(user['senha'] == senha):
            existe = True
            break
    return existe
def buscar_evento(nomeev, eventos):
    existe = False
    for evs in eventos:
        if(evs[0] == nomeev):
            existe = True
            print('\033[0;32mEvento encontrado com sucesso\033[m\n')
            print(evs[0],"\n")
            print(f'Descrição do evento: {evs[1]}\n')
            print(f'Data do evento: {evs[2]}.\n')
            print(f'Local do evento: {evs[3]}.\n')
            print(f'Valor da inscrição: R${evs[4]}.\n')        
    if(existe == False):
        print('\033[0;31mEvento não encontrado\033[m\n')
    voltar = input('Digite qualquer coisa para voltar ao incio: ')
def retorna_nomes(email, usuarios):
    for i in usuarios:
        if(i['email'] == email):
            return i['nome']

def opcao_1(eventos, validação1):
    events = input('Digite o titulo do seu evento: ')
    sinopse = input('Fale qual o intuito do seu evento: ')
    data = input('Digite a data do seu evento: ')
    local = input('Digite o local do seu evento: ')
    valor = int(input('Digite o valor de inscrição do seu evento: '))
    lista = [events, sinopse, data, local, valor, validação1]
    eventos.append(lista)
    salvar_txt(eventos,"eventos.txt")
    print('\033[0;32mEvento inscrito com sucesso\033[m\n')

def opcao_3(eventos):
 for i in eventos:
    print(i[0],"\n")
    print(f'Descrição do evento: {i[1]}\n')
    print(f'Data do evento: {i[2]}.\n')
    print(f'Local do evento: {i[3]}.\n')
    print(f'Valor da inscrição: R${i[4]}.\n')
    
 voltar = input('Digite qualquer coisa para voltar ao início: ') 

def opcao_4(eventos, validação1):
    exclusao = input('Digite o nome do evento que você deseja excluir: ')
    contador = 0
    for i in eventos:
        if(i[5] == validação1 and i[0] == exclusao):
            contador += 1
            exclusao2 = input("Digite seu email para confirmar exclusão do evento: ")
            if(exclusao2 == validação1):
               eventos.remove(i)
               salvar_txt(eventos,"eventos.txt")
               print('\033[0;32mEvento removido com sucesso\033[m\n')
            else:
                print('\033[0;31mEmail invalido.\033[m\n')
    if(contador <= 0):    
        print('\033[0;31mVocê não possue nenhum evento com esse nome\033[m\n')

def opcao_5(eventos, validação1, usuarios):
    contador = 0
    inscricao = input('Digite o nome do evento que você deseja participar: ')
    for i in eventos:
        if(i[0] == inscricao):
            contador += 1
            print(f'O valor da inscrição nesse evento é R$ {i[4]}.\n')
            confirma = input('Digite seu email para confirmar a inscrição: ')
            if(confirma == validação1 and i[5] != confirma):
                nome = retorna_nomes(confirma, usuarios)
                i.append(nome)
                salvar_txt(eventos,"eventos.txt")
                print('\033[0;32mInscrição realizada com sucesso\033[m\n')
            else:
                print('\033[0;31mEmail invalido.\033[m\n')    
    if(contador == 0):
        print('\033[0;31mEsse evento não existe\033[m\n')

def opcao_contagem(i):
    contador = 0
    for participantes in range (6,len(i)):
        contador += 1
        print(f'\033[0;32m{i[participantes]}\033[m\n')
    print(f'O valor arrecardado do seu evento é :R${contador * i[4]}')   

def opcao_6(eventos):
    verificar = input('Digite seu email para ver os participantes do seu evento(S): ')
    for i in eventos:
        if(i[5] == verificar):
            print(f'{i[0]}')
            print('Estes são os participantes do seu evento: ')
            opcao_contagem(i)

def opcao_7(eventos, validação1, usuarios):
    nomeUs = retorna_nomes(validação1, usuarios)
    contador = 0
    for i in eventos:
        contador += 1
        if(nomeUs in i):                    
            print('\033[0;32m-------------------------------------------  EVENTIN  ------------------------------------\033[m')
            print('\nEvento : ', i[0],'                ========== Ticket de compra ========       cliente :',nomeUs)
            print('Data de realização do evento : ',i[2], '                                        Local do evento:', i[3] )
            print(                            "Valor da inscrição :", i[4],"R$"                         )
            print('\033[0;32m--------------------------------------Desejamos um ótimo evento!-------------------------------\033[m\n') 
    if(contador == 0):
        print('\033[0;31mVocê não esta inscrito em nenhum evento.\033[m\n')             

def opcao_8(eventos, validação1):
    eventin = input('Digite o nome do evento em que você deseja adicionar o participante: ')
    add = input('Digite o nome do participante que você deseja adicionar: ')
    contador = 0
    for i in eventos:
            if(i[5] == validação1 and i[0] == eventin):
                contador += 1
                add2 = input("Digite seu email para confirmar: ")
                if(add2 == validação1):
                    i.append(add)
                    salvar_txt(eventos,"eventos.txt")
                    print('\033[0;32mParticipante adicionado com sucesso\033[m\n')
                else:
                    print('\033[0;31mEmail invalido.\033[m\n')
    if(contador == 0):    
        print('\033[0;31mVocê não possue nenhum evento com esse nome\033[m\n')

def salvar_txt(lista,nomeArquivo ):
    with open(nomeArquivo,"w") as arquivo:
        json.dump(lista,arquivo) 

def carregar_txt(nomeArquivo):
    try:
        with open(nomeArquivo,"r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []

def quantidade_pessoas(eventos):
    contador = 0
    for participantes in range (6,len(eventos)):
        contador += 1
    return contador

def opcao_9(eventos, validação1):
    nomeev = []
    quantidadeev = []
    contador = 0
    for i in eventos:
        if(validação1 == i[5]):
            contador += 1
            nomeev.append(i[0])
            quantidadeev.append(quantidade_pessoas(i))
    if(contador == 0):
         print('\033[0;31mVocê não possue nenhum evento\033[m\n')             
    plt.bar(nomeev, quantidadeev)    
    plt.show()

def opcao_10(eventos, validação1):
    nomeev = []
    quantidadeev = []
    contador = 0
    for i in eventos:
        if(validação1 == i[5]):
            contador = 0
            for participantes in range (6,len(i)):
                contador += 1
            valor = i[4]*contador
            nomeev.append(i[0])
            quantidadeev.append(valor)
    if(contador == 0):
         print('\033[0;31mVocê não possue nenhum evento\033[m\n')    
    plt.bar(nomeev, quantidadeev)    
    plt.show()