#1 - Fatorial de um numero
"""
Fatorial de um número
1-> 1*1
2-> 2*1
3->3*2*1

"""

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num *factorial(num -1))

number = (int(input("digite um númeto para o fatorial:\n")))
print(f"O Fatorial de {number} é {factorial(number)}")

#2 soma total de um numero

def total_sum(num):
    if num ==1:
        return 1
    else:
        return (num + total_sum(num -1))

num = int(input("Digite o numero para a soma:\n"))
print(f"A soma total de um {num} é {total_sum(num)}")