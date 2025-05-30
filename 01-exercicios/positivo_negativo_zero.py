# Descobrir se o número digitado pelo usuário é positivo negativo ou é zero

numero = int(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é POSITIVO")

elif numero < 0:
    print(f"O número {numero} é NEGATIVO")

elif numero == 0:
    print(f"O número {numero} é ZERO")

else:
    print("Digite um NÚMERO")
