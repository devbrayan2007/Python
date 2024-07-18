# COMANDO PRINT

print("\033[1;34mHello, World!")


# VARIÁVEIS

x = 10
cidade = 'Rio de Janeiro'

# TIPOS DE DADOS

codigo = 14
nome = "Brayan Campos"
salario = 4.500
situação = True

print(type(codigo)) # int
print(type(nome)) # str
print(type(salario)) # float
print(type(situação)) # bool

# Concatenando variáveis

print("Código: ", codigo, " Nome: ", nome, " Salário: R$",salario, " Situação: ", situação)

# Usando o print formatado
print(f"Código: {codigo} | Nome: {nome} | Salário: R${salario} | Situação: {situação}")

