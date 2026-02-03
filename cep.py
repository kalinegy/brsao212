import requests
import re

def consultar_cep(cep: str):
    # Remove tudo que não for número
    cep_limpo = re.sub(r"\D", "", cep)

    if len(cep_limpo) != 8:
        print("Falha: CEP inválido. Digite 8 números (ex: 01001000).")
        return

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if data.get("erro") is True:
            print("Falha: CEP não encontrado.")
            return

        logradouro = data.get("logradouro", "")
        bairro = data.get("bairro", "")
        cidade = data.get("localidade", "")
        estado = data.get("uf", "")

        print("\nResultado do CEP:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException:
        print("Falha: erro na conexão ou na requisição à API.")
    except ValueError:
        print("Falha: resposta inválida (não veio JSON).")

if __name__ == "__main__":
    cep = input("Digite o CEP: ")
    consultar_cep(cep)
