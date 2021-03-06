

TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

DELIMITADORES = ':;'

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')
DELIMITADOR = 5

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp: str) -> list:
    """
    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    def splitter(string: str, counter=0):
        if counter == len(BRANCOS):
            return string
        chars = string.split(BRANCOS[counter])
        return splitter(''.join(chars), counter + 1)

    def isin(string_a: str, string_b: str):
        for a in string_a:
            for b in string_b:
                if a == b:
                    return True
        return False

    def parser(string: str):
        values = []
        chars = ''

        for char in string:
            assert isin(char, DELIMITADORES + OPERADORES + ABRE_FECHA_PARENTESES + COMENTARIO + FLOATS + LETRAS + (''.join(BRANCOS))), \
                f"O caractere '{char}' não é esperado"
            if (char in OPERADORES or char in DELIMITADORES or char in ABRE_FECHA_PARENTESES) and char not in COMENTARIO:
                if chars == '':
                    values.append(char)
                else:
                    values.append(chars)
                    values.append(char)
                    chars = ''
            elif char in COMENTARIO:
                break
            else:
                chars += char

        if chars != '':
            values.append(chars)

        return values

    value = splitter(string=exp)
    parsed = parser(value)

    results = []
    for char in parsed:
        if char in OPERADORES:
            results.append([char, OPERADOR])
        elif char in DELIMITADORES:
            results.append([char, DELIMITADOR])
        elif char in ABRE_FECHA_PARENTESES:
            results.append([char, PARENTESES])
        elif isin(char, LETRAS):
            results.append([char, VARIAVEL])
        elif isin(char, FLOATS):
            results.append([float(char), NUMERO])

    return results
