import json

def salvar_json(caminho: str, dados: dict):
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("JSON salvo com sucesso!")
    except Exception as e:
        print(f"Falha ao salvar o JSON: {e}")

def ler_json(caminho: str):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
        print("\nDados lidos do JSON:")
        print(f"Nome: {dados.get('nome')}")
        print(f"Idade: {dados.get('idade')}")
        print(f"Cidade: {dados.get('cidade')}")
    except FileNotFoundError:
        print("Falha: arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        print("Falha: o arquivo existe, mas o JSON está inválido/corrompido.")
    except Exception as e:
        print(f"Falha ao ler o JSON: {e}")

if __name__ == "__main__":
    caminho = input("Digite o nome/caminho do arquivo JSON (ex: pessoa.json): ").strip()

    pessoa = {
        "nome": "Kaline",
        "idade": 20,
        "cidade": "Recife"
    }

    salvar_json(caminho, pessoa)
    ler_json(caminho)
