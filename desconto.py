produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))
