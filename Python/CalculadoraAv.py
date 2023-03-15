import math

print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz quadrada")
print("7 - Seno")
print("8 - Cosseno")
print("9 - Tangente")

op = int(input("Digite a opção (1/2/3/4/5/6/7/8/9): "))

if op == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1, "+", num2, "=", num1 + num2)

elif op == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1, "-", num2, "=", num1 - num2)

elif op == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1, "*", num2, "=", num1 * num2)

elif op == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1, "/", num2, "=", num1 / num2)

elif op == 5:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(num1, "^", num2, "=", num1 ** num2)

elif op == 6:
    num = float(input("Digite o número: "))
    print("√", num, "=", math.sqrt(num))

elif op == 7:
    num = float(input("Digite o ângulo em graus: "))
    print("sin(", num, ")=", math.sin(math.radians(num)))

elif op == 8:
    num = float(input("Digite o ângulo em graus: "))
    print("cos(", num, ")=", math.cos(math.radians(num)))

elif op == 9:
    num = float(input("Digite o ângulo em graus: "))
    print("tan(", num, ")=", math.tan(math.radians(num)))

else:
    print("Opção inválida.")