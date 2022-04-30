DELIMITER = [' ', '\n', '\t', '\v', '\f', '\r']
OPERADORES = "%*/+-!^="

def cor(v: str):
    return v not in DELIMITER or v not in OPERADORES

def parse(value: str):
    val = value + " "
    values = []
    count = 0
    while len(val)-1 > count:
        if val[count] in DELIMITER:
            count += 1
        else:
            toincr = ''
            print(val[count])
            while cor(val[count]) and len(val)-1 > count:
                toincr += val[count]
                count += 1
            values.append(toincr)
    print(values)
    
    
if __name__ == "__main__":
    # parse("media_prova = (p1 + p2)/2")
    # parse("media_prova = (p1 + p2) / 2")
    parse("media_prova=(p1+p2)/2")
    # parse("media_prova = ( p1 + p2 ) / 2")
