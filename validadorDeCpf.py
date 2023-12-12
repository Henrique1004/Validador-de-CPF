import re
import sys

"""
Cálculo do primeiro dígito do CPF

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10;
Somar todos os resultados;
Multiplicar o resultado anterior por 10;
Obter o resto da divisão da conta anterior por 11;
Se o resultado anterior for maior que 9:
    resultado é 0.
contrário disso:
    resultado é o valor da conta.
"""

entrada = input('Digite o seu CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você digitou um CPF inválido')
    sys.exit()

cpf_1 = cpf[0:9]
contador_regressivo = 10
resultado_digito_1 = 0

for digito in cpf_1:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

"""
Calculo do segundo dígito do CPF

Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11;
Somar todos os resultados;
Multiplicar o resultado anterior por 10;
Obter o resto da divisão da conta anterior por 11;
Se o resultado anterior for maior que 9:
    resultado é 0.
contrário disso:
    resultado é o valor da conta.
"""

cpf_1 = cpf + str(digito_1)
cpf_2 = cpf[0:10]
contador_regressivo = 11
resultado_digito_2 = 0

for digito in cpf_2:
    resultado_digito_2 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

if (str(digito_1) == cpf[9]) and (str(digito_2) == cpf[10]):
    print('CPF válido')
else:
    print('CPF inválido')
