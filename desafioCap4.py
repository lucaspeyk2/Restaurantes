import os 
dados_pessoas = [{'nome': 'Alice', 'idade': 30}, {'nome': 'Bob', 'idade': 25}]
def exibir_dados():
    os.system('cls')
    for dado in dados_pessoas:
        print(f"Nome: {dado['nome']}, Idade: {dado['idade']}")
exibir_dados()
pergunta1=input('Quer a tualizar a idade de Algum ? (s/n) ')
if pergunta1 == 's':
    nome_pessoa = input('Digite o nome da pessoa: ')
    nova_idade = int(input('Digite a nova idade: '))
    for pessoa in dados_pessoas:
        if pessoa['nome'] == nome_pessoa:
            pessoa['idade'] = nova_idade
            print(f"Idade de {nome_pessoa} atualizada para {nova_idade}.")
    exibir_dados()