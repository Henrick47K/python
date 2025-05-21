print("----- BIBLIOTECA -----")

dias_atraso = int(input("Quantos dias de atraso para a devolução do livro ?"))

if dias_atraso <= 0:
    multa = 0
elif dias_atraso <= 3:
    multa = dias_atraso * 0.50
elif dias_atraso <= 7:
    multa = dias_atraso * 1.00
else:
    multa = dias_atraso * 2.00

print(f"O valor da sua multa é R${multa:.2f}")