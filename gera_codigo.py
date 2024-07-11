from random import randint
# Código tenha sempre 3 dígitos, pode modificar a função para adicionar zeros à esquerda quando necessário
# A função gera_codigo gera um número inteiro aleatório entre 0 e 999 (inclusive), converte esse número em uma string e o retorna.
def gera_codigo():
    return f"{randint(0, 999):03}"

# Chamando a função e imprimindo o resultado
codigo = gera_codigo()
print(codigo)