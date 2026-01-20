def eh_palindromo(texto: str) -> bool:
    # Mantém só letras e números, e coloca tudo em minúsculo
    filtrado = "".join(ch.lower() for ch in texto if ch.isalnum())
    return filtrado == filtrado[::-1]


frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
