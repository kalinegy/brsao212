import pandas as pd

def analisar_csv(caminho_arquivo: str):
    try:
        df = pd.read_csv(caminho_arquivo)

        if "tempo_execucao" not in df.columns:
            print("Erro: a coluna 'tempo_execucao' não existe no CSV.")
            return

        tempos = pd.to_numeric(df["tempo_execucao"], errors="coerce").dropna()

        if tempos.empty:
            print("Erro: não há valores numéricos válidos em 'tempo_execucao'.")
            return

        media = tempos.mean()
        maximo = tempos.max()

        print(f"Média de tempo_execucao: {media:.2f}")
        print(f"Máximo de tempo_execucao: {maximo:.2f}")

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: o arquivo CSV está vazio.")
    except Exception as e:
        print(f"Erro na leitura/processamento do CSV: {e}")

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo CSV: ").strip()
    analisar_csv(caminho)
