frase = ('com banana e com morango')
palavras = frase.split()
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)