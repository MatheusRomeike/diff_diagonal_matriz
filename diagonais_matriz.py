#gerar matriz
matriz = []

ordem_matriz = int(input("Informe a ordem da matriz (maior que 0): "))
while ordem_matriz <= 0:
    ordem_matriz = int(input("Valor incorreto, informe a ordem da matriz (maior que 0): "))

for linha in range(ordem_matriz):
    lista = []
    for coluna in range(ordem_matriz):
        valor = int(input("Informe um valor inteiro para a posiçao ["+str(linha)+"/"+str(coluna)+"]: "))
        lista.append(valor)
    matriz.append(lista)


numero_quadrado = len(matriz)

# coluna principal
coluna_principal = 0

for linha in range(numero_quadrado):
    for coluna in range(numero_quadrado):

        if linha == coluna and numero_quadrado > 1:
            coluna_principal += matriz[linha][coluna]

        elif linha == coluna and numero_quadrado == 1:
            coluna_principal += matriz[linha]
# coluna secundaria
coluna_secundaria = 0

holder = numero_quadrado - 1

for linha in range(numero_quadrado):
    for coluna in range(numero_quadrado):

        if coluna == holder and numero_quadrado > 1:
            coluna_secundaria += matriz[linha][coluna]
            holder -= 1

        elif coluna == holder and numero_quadrado == 1:
            coluna_secundaria += matriz[linha]
            holder -= 1


# fim
valor_absoluto = coluna_principal - coluna_secundaria
if valor_absoluto < 0:
    valor_absoluto = valor_absoluto * -1

print(valor_absoluto)
