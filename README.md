# Quartis com NumPy
Este projeto utiliza a biblioteca NumPy para calcular os quartis de um array de números. 
Os quartis são valores que dividem o conjunto de dados em quatro partes iguais, ajudando a compreender a distribuição dos dados.

## Funcionalidade
1. O código realiza as seguintes operações:
   - Cria um array de exemplo utilizando numpy.array.
   - Calcula o primeiro quartil (Q1), a mediana (Q2) e o terceiro quartil (Q3) utilizando a função numpy.percentile.
   - Exibe os valores dos quartis no console.
## Pré-requisitos
1. Certifique-se de ter o Python instalado na sua máquina, junto com a biblioteca NumPy. Caso ainda não tenha o NumPy, instale-o com o comando:
pip install numpy

## Como executar
1. Copie o código fornecido e salve-o em um arquivo, por exemplo, quartis.py.
2. Execute o arquivo no terminal ou em um ambiente de desenvolvimento Python utilizando o comando:
python quartis.py
3. O programa exibirá os valores dos quartis do array de exemplo no console.

## Exemplo de saída
1. Ao executar o código, a saída será semelhante a esta:
1º Quartil: 3.5
2º Quartil (Mediana): 6.0
3º Quartil: 8.0

## Personalização
1. Se desejar calcular os quartis de um conjunto de dados diferente, substitua o array de exemplo na linha:
arr = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9])
2. Adapte o array de acordo com os valores que você deseja analisar.

## Observação
Os quartis são calculados com base no método de interpolação padrão do NumPy (linear). 
Se precisar de métodos específicos de cálculo para os percentis, consulte a documentação do NumPy sobre a função percentile





