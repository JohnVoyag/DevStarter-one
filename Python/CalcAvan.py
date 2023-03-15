import math

def main():
    print("Bem-vindo à calculadora avançada!")
    while True:
        operacao = input("Digite a operação que deseja realizar (+, -, *, /, **, raiz, sin, cos, tan, log): ")
        
        if operacao == "raiz":
            numero = float(input("Digite o número que deseja calcular a raiz: "))
            resultado = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é {resultado}\n")
        
        elif operacao in ["sin", "cos", "tan"]:
            angulo = float(input("Digite o ângulo em graus: "))
            radianos = math.radians(angulo)
            if operacao == "sin":
                resultado = math.sin(radianos)
            elif operacao == "cos":
                resultado = math.cos(radianos)
            else:
                resultado = math.tan(radianos)
            print(f"O {operacao}({angulo}) é {resultado}\n")
        
        elif operacao == "log":
            base = float(input("Digite a base do logaritmo: "))
            numero = float(input("Digite o número do logaritmo: "))
            resultado = math.log(numero, base)
            print(f"O log na base {base} de {numero} é {resultado}\n")
        
        elif operacao in ["+", "-", "*", "/", "**"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if operacao == "+":
                resultado = num1 + num2