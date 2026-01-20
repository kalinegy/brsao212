from datetime import date

ano = int(input("Ano de nascimento (AAAA): "))
mes = int(input("Mês de nascimento (1-12): "))
dia = int(input("Dia de nascimento (1-31): "))

data_nascimento = date(ano, mes, dia)
hoje = date.today()

dias_vivo = (hoje - data_nascimento).days

if dias_vivo < 0:
    print("Data de nascimento inválida (no futuro).")
else:
    print("Você está vivo há", dias_vivo, "dias.")
    print("Data de hoje:", hoje.strftime("%d/%m/%Y"))
