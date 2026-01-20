def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)



conta = float(input("Valor total da conta (R$): "))
porcentagem = float(input("Porcentagem de gorjeta (%): "))

gorjeta = calcular_gorjeta(conta, porcentagem)
print("Gorjeta: R$", round(gorjeta, 2))
