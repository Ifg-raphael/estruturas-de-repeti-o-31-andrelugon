# Programa que calcula o somatório S = soma de i/(i*(i-1)) de i=2 até n

# Entrada de dados: o usuário fornece o valor de n
n = int(input("Digite um valor para n: "))

# Processamento: cálculo do somatório
soma = 0
for i in range(2, n + 1):
    soma = soma + (i / (i * (i - 1)))

# Saída de dados: imprime o valor do somatório
print(f"Resultado do somatório: {soma:.2f}")

