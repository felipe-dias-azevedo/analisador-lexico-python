def grafo(tokens: list):
    values = dict()
    left = 0
    right = 2
    for x in tokens[1:]:
        if x[1] == 1:
            if tokens[right][0] == '(':
                aux = right + 1
                for y in tokens[aux:]:
                    if tokens[aux][0] == ')':
                        values[x[0]] = [tokens[left][0], tokens[aux+1][0]]
                        break
                    aux += 1
            elif tokens[left][0] == ')':
                aux = left - 1
                for y in tokens[:aux]:
                    if tokens[aux][1] == 1:
                        values[x[0]] = [tokens[aux][0], tokens[right][0]]
                        break
                    aux -= 1
            else:
                values[x[0]] = [tokens[left][0], tokens[right][0]]
        left += 1
        right += 1
    return values

if __name__ == "__main__":
    import tokeniza as tk
    token = tk.tokeniza("media_prova=(p1+p2)/2 # ISTO É UM COMENTÁRIO")
    # token = [['media_prova', 3], ['=', 1], ['(', 4], ['p1', 3], ['+', 1], ['p2', 3], [')', 4], ['/', 1], [2.0, 2]]
    g = grafo(tokens=token)
    print(g)