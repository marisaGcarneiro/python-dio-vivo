nome = "Gusmao"
idade = 48
profissao =  "Programador"
linguagem = "Python"
saldo = 45.434

dados = {"nome": "Gusmao", "idade": 48}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(nome, idade))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}" .format( age=idade, name=nome))
print("Nome: {name} Idade: {age} {name} {name} {age}" .format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")