senha = input("Digite sua senha: ")

tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
        break

if len(senha) >= 8 and tem_numero:
    print("Senha válida ✔️")
else:
    print("Senha inválida ❌")
    print("A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")
