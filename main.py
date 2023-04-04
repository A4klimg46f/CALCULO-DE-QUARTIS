import numpy as np

# criando um array de exemplo
arr = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9])

# quartis
q1 = np.percentile(arr, 25)
q2 = np.percentile(arr, 50)
q3 = np.percentile(arr, 75)
print("1º Quartil:", q1)
print("2º Quartil (Mediana):", q2)
print("3º Quartil:", q3)
