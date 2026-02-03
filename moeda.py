import requests

def cotacao_para_brl(moeda: str):
    moeda = moeda.strip().upper()

    # AwesomeAPI: /json/last/USD-BRL
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        chave = f"{moeda}BRL"
        if chave not in data:
            print("Erro: moeda não encontrada ou formato inesperado.")
            return

        info = data[chave]

        # Campos comuns na AwesomeAPI:
        # bid (atual), high (máxima), low (mínima), create_date (data/hora)
        atual = info.get("bid")
        maxima = info.get("high")
        minima = info.get("low")
        atualizado_em = info.get("create_date")

        if not all([atual, maxima, minima, atualizado_em]):
            print("Erro: não foi possível obter todos os dados da cotação.")
            return

        print(f"\nCotação {moeda}/BRL:")
        print(f"Valor atual: {atual}")
        print(f"Máxima: {maxima}")
        print(f"Mínima: {minima}")
        print(f"Última atualização: {atualizado_em}")

    except requests.exceptions.RequestException:
        print("Erro: falha na requisição (conexão/timeout/HTTP).")
    except ValueError:
        print("Erro: resposta inválida (não veio JSON).")

if __name__ == "__main__":
    moeda = input("Digite a moeda (ex: USD, EUR, BTC): ")
    cotacao_para_brl(moeda)
