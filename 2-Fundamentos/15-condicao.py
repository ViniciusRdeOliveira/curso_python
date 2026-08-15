# name=input("Digite o nume do filme:\n")
# yearRealese=(int(input("Digite o ano do lançamento\n")))
# rating = float(input("Digite a nota de avaliação do filme\n"))

# if rating > 8.0 and yearRealese > 2015:
#     print(f"O filme {name} é muito bom. Recomendo assití-lo.")
# else:
#     print(f"O filme {name} ainda não atingiu uma boa nota.")

num1 = float(input("Digite o primeiro número\n"))
num2 = float(input("Digite o segundo número\n"))
operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro divisão por 0")
        result = 0
else:
    print("Operação Inválida")
    result = 0 

print(f"Resultado da operação é {result:.2f}")