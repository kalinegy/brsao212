import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        user = data["results"][0]
        nome = f'{user["name"]["first"]} {user["name"]["last"]}'
        email = user["email"]
        pais = user["location"]["country"]

        print("Usuário aleatório encontrado:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print("Falha: erro na conexão ou na requisição à API.")
    except (KeyError, ValueError):
        print("Falha: resposta da API veio em formato inesperado.")

if __name__ == "__main__":
    buscar_usuario()
