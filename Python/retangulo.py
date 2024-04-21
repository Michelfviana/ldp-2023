import math

base = float(input("base do retângulo: "))
altura = float(input("altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"AREA = {area:.4f}")
print(f"PERÍMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
