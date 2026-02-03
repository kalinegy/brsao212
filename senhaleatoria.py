import random
import string

def gerar_senha(tamanho: int) -> str:
    if tamanho < 4:
        raise ValueError("O tamanho mínimo recomendado é 4.")

    letras = string.ascii_letters  
    numeros = string.digits        
    simbolos = string.punctuation  

  
    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos),
    ]


    todos = letras + numeros + simbolos
    senha += [random.choice(todos) for _ in range(tamanho - 3)]

    random.shuffle(senha)
    return "".join(senha)

def main():
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        senha = gerar_senha(tamanho)
        print(f"\nSenha gerada ({tamanho} caracteres): {senha}")
    except ValueError as e:
        print(f"Falha: {e}")

if __name__ == "__main__":
    main()
