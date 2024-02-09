'''
Seu projeto deve iniciar apresentando uma lista de opções sobre quais dado(s) devem ser gerados, pedindo o usuário
para escolher uma ou mais opções de dados a serem gerados entre as seguintes opções: gerar nome, gerar e-mail,
gerar telefone, gerar cidade, gerar estado, além de perguntar se os dados devem ser salvos para um arquivo também.
Finalmente o usuário deve poder digitar “parar” a qualquer momento para conseguir finalizar o programa.
De onde saíram esses dados aleatórios?
Seu programa precisa imprimir nomes, e-mails, telefones, cidades e estados, certo? Crie uma lista de 5 itens para cada
um desses dados, fica a seu critério como irá gerar esses dados, eles não precisam ser dados reais.
EX:
● Uma lista com 5 nomes
● Uma lista com 5 e-mails
● Uma lista com 5 telefones
● Uma lista com 5 cidades
● Uma lista com 5 estados
Após o usuário escolher quais dados devem ser gerados, você deve processar quais escolhas foram feitas pelo usuário
e depois gerar imprimir na tela uma nova linha contendo o dado que foi selecionado no console e também salvar estes
dados em um arquivo, caso o usuário tenha escolhido a opção de salvar os dados em um arquivo de .txt chamada
dados.txt
O programa deve continuar rodando e pedindo para gerar mais dados aleatórios que forem escolhidos pelo usuário até o ususuario digitar "parar". Quando assim o fizer, o programa deve finalizar
'''
# 1º Passo - Criar uma lista de nomes , emails, telefones, cidades e estados
# 2º Passo - Pedir para o Usuario quais dados ele quer que sejam gerados
# Dificuldade 1 - Exibir os dados caso o usuario peça mais de um.
# Dificuldade 2 - Parar o programa
# Dificuldade 3 - Incluir os dados de lista em vez dos numéros
# 3º Passo - Imprimir os dados na tela de maneira aleatoria (Modulo random)
# 4º Passo - Perguntar ao usuario se deseja salvar em um arquivo (Caso sim, with open arquivo)
# 5º Passo - Rodar o programa em loop até o Usuario digitar "parar"
# 6º Passo - Parar o programa quando o usuario digitar "parar"

nomes = ['Marcelo','Gabriel','John','Alex','Jessica']
emails = ['marcelo123@gmail.com','gabriel123@gmail.com','john123@gmail.com','alex123@gmail.com','jessica123@gmail.com']
telefones = ['5585997282003','558596291695','5585932238678','5585975648970','5585993569376']
cidades = ['Fortaleza','Recife','São Paulo','Brasília','Rio de Janeiro']
estados = ['Ceará','Pernambuco','São Paulo','Rio de Janeiro','Distrito Federal']

import random
import os



nome_usuario = input('Digite seu nome: ')
print('-----------------------------------------')
print(f'Olá {nome_usuario} \nBem vindo ao gerador de dados da SystemForAll! \n*Caso queira parar, apenas digite "parar"')
print('-----------------------------------------')
while True:
    print('Temos essas opções de dados para serem gerados: \n[1] - Nome \n[2] - E-mail \n[3] - Telefone \n[4] - Cidade \n[5] - Estado \n(Caso for gerar mais de um dado, por favor separe entre virgulas)')
    dados_a_serem_recolhidos = input('Digite qual dado ou dados você gostaria de gerar: ')
    print('-----------------------------------------')
    nome = (random.choice(nomes))
    email = (random.choice(emails))
    telefone = (random.choice(telefones))
    cidade = (random.choice(cidades))
    estado = (random.choice(estados))



    for dado in dados_a_serem_recolhidos.split(','):
        if dado == '1':
            print(nome)
        elif dado == '2':
            print(email)
        elif dado == '3':
            print(telefone)
        elif dado == '4':
            print(cidade)
        elif dado == '5':
            print(estado)
        
    
    if dado == 'parar':
        print('Programa finalizado!')
        break


    criar_arquivo = input('Deseja salvar os dados em um arquivo? (s/n) ')

    if criar_arquivo == 's':
        with open ('dados.txt','w',newline='') as arquivo:
            for dado in dados_a_serem_recolhidos.split(','):
                if dado == '1':
                    arquivo.write((nome) + os.linesep)
                elif dado == '2':
                    arquivo.write((email) + os.linesep)
                elif dado == '3':
                    arquivo.write((telefone) + os.linesep)
                elif dado == '4':
                    arquivo.write((cidade) + os.linesep)
                elif dado == '5':
                    arquivo.write((estado) + os.linesep)
    else:
        continue
    
        




  




    

   
    
   
     

    


   
    
    

    
    
    
    
