import math

def bhaskara():
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return "Raiz única:", x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "Raízes:", x1, "e", x2

# Exemplo de uso
print(bhaskara())
