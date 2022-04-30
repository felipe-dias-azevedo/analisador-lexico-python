
from turtle import right


def isDelimiter(ch):
	if ch == ' ' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ',' or ch == ';' or ch == '>' or ch == '<' or ch == '=' or ch == '(' or ch == ')' or ch == '[' or ch == ']' or ch == '{' or ch == '}':
		return True
	return False

def isOperator(ch):
	if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '>' or ch == '<' or ch == '=':
		return True
	return False

def validIdentifier(strg: str):
	if strg[0] == '0' or strg[0] == '1' or strg[0] == '2' or strg[0] == '3' or strg[0] == '4' or strg[0] == '5' or strg[0] == '6' or strg[0] == '7' or strg[0] == '8' or strg[0] == '9' or isDelimiter(strg[0]) == True:
		return False
	return True

def isKeyword(strg: str):
	if strg != "if" or strg != "else" or strg != "while" or strg != "do" or strg != "break" or strg != "continue" or strg != "int" or strg != "double" or strg != "float" or strg != "return" or strg != "char" or strg != "case" or strg != "char" or strg != "sizeof" or strg != "long" or strg != "short" or strg != "typedef" or strg != "switch" or strg != "unsigned" or strg != "void" or strg != "static" or strg != "struct" or strg != "goto":
		return True
	return False

def isInteger(strg: str):
    i = 0
    lenstr = len(strg)

    if lenstr == 0:
        return False
    while i < lenstr:
        if strg[i] != '0' and strg[i] != '1' and strg[i] != '2' and strg[i] != '3' and strg[i] != '4' and strg[i] != '5' and strg[i] != '6' and strg[i] != '7' and strg[i] != '8' and strg[i] != '9' or (strg[i] == '-' and i > 0):
            return False
        i += 1
    return True


def isRealNumber(strg: str):
    i = 0
    lenstr = len(strg);
    hasDecimal = False;

    if lenstr == 0:
        return False
    while i < lenstr:
        if strg[i] != '0' and strg[i] != '1' and strg[i] != '2' and strg[i] != '3' and strg[i] != '4' and strg[i] != '5' and strg[i] != '6' and strg[i] != '7' and strg[i] != '8' and strg[i] != '9' and strg[i] != '.' or (strg[i] == '-' and i > 0):
            return False
        if strg[i] == '.':
            hasDecimal = True;
        i += 1
    return hasDecimal

def subString(strg: str, left: int, right: int) -> str:
    v = ''
    i = left
    while i <= right:
        v += strg[i]
        i += 1
    return v

def parse(strg: str):
    left = 0
    right = 0
    lenstr = len(strg)

    while right <= lenstr and left <= right:
        if not isDelimiter(strg[right]):
            right += 1
        if isDelimiter(strg[right]) and left == right:
            if isOperator(strg[right]):
                print(f"{strg[right]} IS AN OPERATOR")
            right += 1
            left = right;
        elif isDelimiter(strg[right]) and left != right or (right == lenstr and left != right):
            subStr = subString(strg, left, right - 1)
            if isKeyword(subStr):
                print(f"{subStr} IS A KEYWORD")
            elif isInteger(subStr):
                print(f"{subStr} IS AN INTEGER");
            elif isRealNumber(subStr):
                print(f"{subStr} IS A REAL NUMBER")
            elif validIdentifier(subStr) and not isDelimiter(strg[right - 1]):
                print(f"{subStr} IS A VALID IDENTIFIER")
            elif not validIdentifier(subStr) and not isDelimiter(strg[right - 1]):
                print(f"{subStr} IS NOT A VALID IDENTIFIER")
            left = right

def main():
	strg = "int a = b + 1c; "

	parse(strg)
 
if __name__ == "__main__":
    main()
