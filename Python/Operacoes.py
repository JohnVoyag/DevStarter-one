#Ordem de precedência, ou melhor, ordem de resolução da expressões matemáticas.
#1 () -Parenteses
#2 ** -Potência
#3 *, /, //, % - Multiplicaçã, divisão, divisão inteira e resto da divisão.
#4 +, -, -Soma e subtração.
#/n significa quebra de linha.

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
nome = input('Qual é o seu nome?')
print('Prazer em te conhecer{:=^20}!'.format(nome))
print('O resultado é {}, {} e {:.3f} respectivamente!'.format(s, m, d,))
print('O resultado é {} e {} respectivamente!'.format(di, e))
