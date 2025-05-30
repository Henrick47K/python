while True:
    print("Descubra se o número é PAR ou IMPAR")
    par_impar = int(input("Digite um número: "))

    if par_impar <0:
        print("Valor inválido. Tente novamente.")
        continue

    if par_impar %2 == 0:
        print(f"O número {par_impar} é PAR")
    else:
        print(f"O número {par_impar} é IMPAR")
    
    continuar = input("Deseja continuar(s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado.")
        break     