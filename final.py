def jogo_da_forca():
    
    print('Seja bem-vindo ao jogo da forca!\n')    

    import random as rd
    lista = ['LIMAO','ABACAXI','JABUTICABA','UVA','MELANCIA','ABACATE','MORANGO','ABACATE','PEQUI']


    #Função para escolher uma palavra da lista aleatoriamente
    def palavra_aleatoria(lista):    
        tamanho = len(lista)
        sorteio = rd.randint(1,tamanho)    
        palavra_aleatoria = lista[sorteio] 
        return palavra_aleatoria
    
    #função para localizar as posições de uma letra em uma palavra
    def localizar(texto,palavra):
        posicoes = []
        for i in range(0,len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes


    palavra = palavra_aleatoria(lista)
    print(f'DICA: A palavra tem {len(palavra)} letras')


    chances = 0
    palavr_secret = list('_' * len(palavra))
    while chances <= 5:
        letra_digitada = input('Digite somente uma letra: ').upper()    
        if letra_digitada in palavra:
            print(f'A letra {letra_digitada} está contida na frase')                 
            posicao = localizar(palavra,letra_digitada)
            for i in posicao:    
                palavr_secret[i] = letra_digitada            
            print(palavr_secret)        
                         
        else:
            print(f'A letra {letra_digitada} NÃO está contida na frase')
            print(palavr_secret) 
            print(f'Você ainda tem mais {5-int(chances)} chances') 

        chances +=1
        if chances >= 5:
            print('-------- X GAME OVER X --------') 
            print(f'A Palavra correta é {palavra}!')
            break


jogo_da_forca()