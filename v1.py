# PROBLEMAS AQUI:
# Pede para fazer apTudo virar integer
# Quando apTudo tem int(), não consegue fazer operações [:2] e [-2]
    # "TypeError: 'int' object is not subscriptable"
# Por algum motivo, ele não conhece a operação % (divide por 2 e vê o resto)

# Exemplo de números para teste: 1123, 789.
# ! Testar apenas 1123. Falta contagem de caracteres para 3. !

# INTERFONE!

# apTudo = número total do apartamento ("inteiro")
# apDir = direção para o apartamento (esquerda/direita)
# apNum = número do apartamento
# apUp = andar do apartamento

title = "INTERFONE!"

print(title)
print()
print("Digite o número do endereço.")

apTudo = int(input())
apDir = "abacaxi"

# checar se dividir por 2 dá resultado inteiro/zero
if (apTudo %2) == 0:
    apDir = "esquerda"
else:
    apDir = "direita"
    
apNum = apTudo[:2] # dois primeiros números
apUp = apTudo[-2] # dois últimos números

res = """
1.Para o apartamento n° {}, vá ao {}° andar.
2. Quando chegar, vire à {}
3. Ao virar, procure o corredor pelo apartamento de número {}.
""".format(apTUDO, apUp, apDir, apNum)

print()
print(res)
