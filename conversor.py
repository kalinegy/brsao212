reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar = reais / taxa_dolar
euro = reais / taxa_euro

print("Valor em reais: R$", reais)
print("Valor em dólar: US$", round(dolar, 2))
print("Valor em euro: €", round(euro, 2))
