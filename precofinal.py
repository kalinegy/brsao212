def calcular_desconto(preco: float, percentual: float) -> float:
    return preco * (percentual / 100)

def preco_final(preco: float, percentual: float) -> float:
    return preco - calcular_desconto(preco, percentual)


produto = input("Nome do produto: ")
preco = float(input("Preço original (R$): "))
percentual = float(input("Desconto (%): "))

desconto = calcular_desconto(preco, percentual)
final = preco_final(preco, percentual)

print("\nProduto:", produto)
print("Preço original: R$", round(preco, 2))
print("Desconto: R$", round(desconto, 2))
print("Preço final: R$", round(final, 2))
