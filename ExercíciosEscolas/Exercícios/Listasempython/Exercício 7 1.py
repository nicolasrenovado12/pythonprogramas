lista = []

for i in range(0, 10, 1):
    
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)

tiranumerosduplicados = list(set(lista) & set(lista))
print(tiranumerosduplicados)

    
