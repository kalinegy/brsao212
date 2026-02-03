def salvar_tabela_txt(caminho_saida: str):
    pessoas = [
        {"nome": "Ana", "idade": 22, "cidade": "Recife"},
        {"nome": "Bruno", "idade": 30, "cidade": "Olinda"},
        {"nome": "Carla", "idade": 27, "cidade": "Jaboatão"},
        {"nome": "Diego", "idade": 25, "cidade": "Paulista"},
    ]

  
    colunas = ["nome", "idade", "cidade"]
    larguras = {c: len(c) for c in colunas}

    for p in pessoas:
        for c in colunas:
            larguras[c] = max(larguras[c], len(str(p[c])))

    linha_sep = "+-" + "-+-".join("-" * larguras[c] for c in colunas) + "-+"
    cabecalho = "| " + " | ".join(c.upper().ljust(larguras[c]) for c in colunas) + " |"

    linhas = [linha_sep, cabecalho, linha_sep]
    for p in pessoas:
        linha = "| " + " | ".join(str(p[c]).ljust(larguras[c]) for c in colunas) + " |"
        linhas.append(linha)
    linhas.append(linha_sep)

    conteudo = "\n".join(linhas)

    try:
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"Arquivo salvo com sucesso em: {caminho_saida}")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

if __name__ == "__main__":
    caminho = input("Digite o caminho/nome do arquivo para salvar (ex: pessoas.txt): ").strip()
    salvar_tabela_txt(caminho)
