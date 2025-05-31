palavra_secreta = "banana"
letras_certas = []
tentativas = 6

print("=== JOGO DA FORCA ===")

while True:
    letra = input("\nDigite uma letra: ").lower()

    if letra in letras_certas:
        print("VocÊ já tentou essa letra.")
        continue

    if letra in palavra_secreta:
        print("✅ Letra correta!")
        tentativas -= 1
        letras_certas.append(letra)
    else:
        print("❌ Letra incorreta.")
        tentativas -= 1

    # Mostrar progresso da palavra
    progresso = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            progresso += letra_secreta + " "
        else:
            progresso += "_ "
    
    print("Palavra:", progresso)
    print("Tentativas restantes:", tentativas)

    # Verificar vitória
    if all(letra in letras_certas for letra in palavra_secreta):
        print("\n Parabéns! Você venceu!")
        break
    # Verifica derrota
    if tentativas == 0:
        print("\nVocê perdeu! A palavara era:", palavra_secreta)
        break