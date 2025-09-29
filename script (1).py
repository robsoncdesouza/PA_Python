import random

palavras =  ["caqui","melão", "mamão", "limão", "amora"]
adivinhar = random.choice(palavras).upper()
letras_adivinhar = list(adivinhar)

resposta = ""
tentativa = 0
letras = ["_", "_", "_", "_", "_"]
letras_existentes = []


while tentativa < 6:
    tentativa += 1
    print(f"Tentativa {tentativa}/6")
    
    resposta = input("palavra: ").upper()

    while len(resposta) != 5:
        print(f"A palavra deve ter 5 letras. a palavra tem {len(resposta)} letras.")
    letras_resposta = list(resposta)
    
    if resposta == adivinhar:
        print("Parabéns! Você acertou a palavra!")
        break

    else:
        for i in range(5):

            if letras_resposta[i] == letras_adivinhar[i]:
                print(f"{letras_resposta[i].upper()} está na posição correta.")
                letras[i] = letras_resposta[i].upper()
                if letras_resposta[i].upper() not in letras_existentes:
                    letras_existentes.append(letras_resposta[i].upper())

            elif letras_resposta[i] in letras_adivinhar:
                print(f"{letras_resposta[i].upper()} está na palavra, mas na posição errada.")
                if letras_resposta[i].upper() not in letras_existentes:
                    letras_existentes.append(letras_resposta[i].upper())

            else:
                print(f"{letras_resposta[i].upper()} não está na palavra.")
    print("Palavra: " + " ".join(letras) + " | Letras Existentes: " + " ".join(letras_existentes))