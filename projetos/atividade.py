# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
lst_organizadores = ['bento','mariana','saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria']
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
  # Inicializando a variável de total de vendas
total_vendas = 0

  # Loop para somar as vendas de cada fornecedor
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor['vendas']

  # Exibindo o total de vendas
print(total_vendas)

# Os professores doaram 5000,00, cada professor doou 1000,00
# 2 - Criar um dicionario com o nome e valor
dict_professores = {"Laert" : 1000 , "Carol": 1000,"Kennedy": 1000, "João": 1000,
"Fernando":1000
}

# 3 - Criar uma lista com os nomes dos professores
  # Criando uma lista com os nomes dos professores
lista_professores = list(dict_professores.keys())

  # Exibindo a lista
print(lista_professores)

# 4 - Adicionar essa lista dos professores na lista de clientes
list_cliente.extend(lista_professores)
print(list_cliente)

# 5 - Calcular quantas pessoas estiveram e a media de gasto por pessoa
quantidade_pessoa = len(list_cliente)
media_consumidor = total_vendas/quantidade_pessoa
print(quantidade_pessoa)
print(media_consumidor)

# 6 - Encontrar quem foi o 10 consumidor e retire da lista
list_cliente.remove(list_cliente[9])

# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista
if "bola" in list_cliente:
    list_cliente.remove("bola")
    print("cliente bola removido")
else:
    print("cliente bola nao encontrado")

# 8 - Verificar se todos os organizadores estao na lista
for nome in lst_organizadores:
  if nome in list_cliente:
    print(f"{nome} esta na lista!")
  else:
    print(f"{nome} Nao esta na lista")

# 9 - Tira-los da lista
for nome in lst_organizadores:
    if nome in list_cliente:
        print(f"{nome} está na lista! Removendo {nome}.")
        list_cliente.remove(nome)
    else:
        print(f"{nome} não está na lista!")

# Exibir a lista de clientes atualizada
print("Lista de clientes atualizada:", list_cliente)

# 10 - fazer uma funçao que calcule o lucro liquido do evento
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# importe o pacote com a funcao
# chame a funcao
# execute o programa