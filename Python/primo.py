def primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True


# Exemplo de uso
numero = 17
if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
