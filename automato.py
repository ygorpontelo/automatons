def formata_transicoes(num_transicoes):
    '''
    Le as transicoes e guarda em um dicionario no formato:
        {Estado: {input: [lista de estados de ida validos]}, Estado2...}

    Parametros:
        num_transicoes: numero de transicoes
    
    Retorno:
        transicoes: retorna o dicionario com as transicoes 
    '''
    
    transicoes = {}
    # Para cada estado, cria lista de estados de ida validos para cada input
    for i in range(num_transicoes):
        t = input().split()
        if t[0] in transicoes:                      
            if t[1] in transicoes[t[0]]:            
                transicoes[t[0]][t[1]].append(t[2]) 
            else:
                transicoes[t[0]][t[1]] = [t[2]]     
        else:
            transicoes[t[0]] = {t[1]: [t[2]]}       
    return transicoes

def testa_cadeia(cadeia, estado, transicoes, estados_aceitacao):
    '''
    Funcao recursiva para testar uma determinada cadeia
    
    Parametros:
        cadeia:             string representando a cadeia
        estado:             estado atual, comecando pelo estado inicial
        transicoes:         dicionario contendo as transicoes
        estados_aceitacao:  lista de estados de aceitacao
    
    Retorno:
        True:   cadeia valida
        False:  cadeia invalida
    '''

    if len(cadeia) > 0: # condicao de parada
        r = False
        try:
            # testa cada estado de ida valido 
            for e in transicoes[estado][cadeia[0]]:
                r = r or testa_cadeia(cadeia[1:], e, transicoes, estados_aceitacao)
            return r
        except KeyError: # caso nao exista transicao para o input
            return False
    else:
        return estado in estados_aceitacao 

def aceita_cadeia(cadeia, estados_i, transicoes, estados_aceitacao):
    '''
    Funcao que retorna se o automato aceita ou rejeita a cadeia

    Parametros:
        cadeia:             string representando a cadeia
        estados_i:          qtd de estados iniciais
        transicoes:         dicionario contendo as transicoes
        estados_aceitacao:  lista de estados de aceitacao

    Retorno:
        String: "aceita" ou "rejeita"
    '''

    # testa para cada estado inicial
    for i in range(estados_i):
        if testa_cadeia(cadeia, str(i), transicoes, estados_aceitacao):
            print('aceita')
            break
    else:
        print('rejeita')

if __name__ == "__main__":
    num_estados         = input()
    carac_terminais     = input().split()[1:]
    estados_i           = int(input())
    estados_aceitacao   = input().split()[1:]
    num_transicoes      = int(input())
    transicoes          = formata_transicoes(num_transicoes) # le transicoes
    qtd_cadeias         = int(input())

    # Valida cada cadeia
    for i in range(qtd_cadeias):
        cadeia = input()
        aceita_cadeia(cadeia, estados_i, transicoes, estados_aceitacao)

    # aguarda para sair
    try:
        i=input()
    except:
        pass