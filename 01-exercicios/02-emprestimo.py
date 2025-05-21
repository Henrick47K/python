# variaveis
total_livros_emprestados = ""
media_diaria = ""
maior = ""

# perguntas
segunda = int(input("Quantos livros foram emprestados na segunda-feira ? "))
terca = int(input("Quantos livros foram emprestados na terça-feira ?"))
quarta = int(input("Quantos livros foram emprestados na quarta-feira ?"))
quinta = int(input("Quantos livros foram emprestados na quinta-feira ?"))
sexta = int(input("Quantos livros foram emprestados na sexta-feira ?"))
sabado = int(input("Quantos livros foram emprestados no sabado ? "))
domingo = int(input("Quantos livros foram emprestados no domingo ? "))

# calculos de livros emprestados

total_livros_emprestados = (segunda) + (terca) + (quarta) + (quinta) + (sexta) + (sabado) + (domingo)

media_diaria = total_livros_emprestados / 7

if segunda > terca and quarta and quinta and sexta and sabado and domingo:
    maior = "segunda"

elif terca > quarta and quinta and sexta and sabado and domingo:
    maior = "terca"

elif quarta > quinta and sexta and sabado and domingo:
    maior = "quarta"

elif quinta > sexta and sabado and domingo:
    maior = "quinta"

elif sexta > sabado and domingo:
    maior = "sexta"

elif sabado > domingo:
    maior = "sabado"

else:
    maior = "domingo"

print(f"O número total de livros emprestados na semana é:{total_livros_emprestados}")
print(f"A média diária de empréstimos é:{media_diaria}")
print(f"O dia com o maior número de empréstimos é:{maior}")

