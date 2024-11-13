#inicializando a lista com 20 números inteiros

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#inicializandoas listas impar e par
impar = []
par = []

#separando os números em pares e impares

for num in nums:
    if num % 2 == 0:
        par.append(num)
    else: impar.append(num)

#imprimindo as listas par e impar

print(f"listas par: ", par)
print(f"lista impar: ", impar)