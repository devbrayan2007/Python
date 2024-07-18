# ENTRADA DE DADOS

produto = str(input("Digite o nome do produto: "))
print(produto)

codigo = int(input("Informe o código: "))
nome = str(input("Digite seu nome: "))
salario = str(input("Informe seu salário: R$"))
situação = bool(input("Informe sua situação atual: "))

print(f"Código: {codigo}\n Nome: {nome}\n Salário: R${salario}\n Situação: {situação}")
