# Definir as funções para cada operação matemática
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Imprimir as opções do usuário
print("Selecione a operação desejada:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Obter a entrada do usuário
choice = input("Digite sua opção (1/2/3/4): ")

# Obter a entrada dos números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executar a operação selecionada
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Opção inválida")