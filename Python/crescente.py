print("Digite dois numeros: ")
x = int(input())
y = int(input())

while x != y: 
    if x < y:
        print("CRESCENTE!")
    else:
        print("DESCRESCENTE!")

    print("Digite outros dois numeros:")
    x = int(input())
    y = int(input())    