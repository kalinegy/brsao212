def ler_arquivo_txt(caminho: str):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for i, linha in enumerate(f, start=1):
                print(f"{i}: {linha.rstrip()}")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo TXT para ler: ").strip()
    ler_arquivo_txt(caminho)
