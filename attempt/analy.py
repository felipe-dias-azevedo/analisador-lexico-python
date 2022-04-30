DELI = [' ', '\n', '\t', '\v', '\f', '\r']
OPER = "%*/+-!^="
PARE = "()"
COMM = "#"
DIGT = "0123456789"
PONTO = "."
FLOATS = DIGT + PONTO
LETR  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sep(x: str, counter=0):
    if counter == len(DELI):
        return x
    return sep(''.join(x.split(DELI[counter])), counter+1)

def isin(a: str, b: str):
    for ele in b:
        for letr in a:
            if ele == letr:
                return True
    return False

def p(v: str):
    val = sep(x=v)
    values = []
    aux = ''

    for x in val:
        if (x in OPER or x in PARE) and x not in COMM:
            if aux == '':
                values.append(x)
            else:
                values.append(aux)
                values.append(x)
                aux = ''
        elif x in COMM:
            break
        else:
            aux += x

    if aux != '':
        values.append(aux)

    print(values)

    res = []
    for v in values:
        if v in OPER:
            #OPERADOR
            res.append([v, 1])
        elif v in PARE:
            #PARENTESES
            res.append([v, 4])
        elif isin(v, LETR):
            #VARIAVEL 
            res.append([v, 3])
        elif isin(v, FLOATS):
            #NUMERICO
            res.append([v, 2])
        
        
    print(res)
    

#p("media_prova=(p1+p2)/2")
#p("media_prova = ( p1 + p2 ) / 2")
p("media_prova=(p1+p2)/2 # ISTO É UM COMENTÁRIO\nvalor=10")
p("media_prova = ( p1 + p2 ) / 2 # ISTO É UM COMENTÁRIO \n valor = 10")