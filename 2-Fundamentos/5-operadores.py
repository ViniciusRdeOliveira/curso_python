num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

    #aritiméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 #resto da divisão
exp = num1 ** num2 #exponenciação


print(sum)
print(sub)
print(div)
print(mult)
print(mod)
print(exp)

#comparaçao

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2


print(bigger)
print(smaller)

print(f"Os números são iguais? {equal}")
print(f"Os números são diferentes? {different}")
print(f"O primeiro número é maior ou igual ao segundo? {biggerEqual}")
print(f"O primeiro número é menor ou igual ao segundo? {smallerEqual}")

#atribuição

num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 2 #num1 = num1 * 2
num1 /= 2 #num1 = num1 / 2