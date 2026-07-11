def lexer(text: str) -> list:
    tokens = []
    i = 0 
    while i < len(text):
        c = text[i]
        if c == ' ':
            i += 1
        elif c in '+-*/()':
            tokens.append(('OP', c))
            i += 1
        elif c.isDigit():
            j = i
            while j < len(text) and text[j].isDigit():
                j += 1
            tokens.append(('NUM', int(text[i:j])))
            i = j
        else:
            raise SyntaxError (f"lexer: unexpected character {c!r}")
    tokens.append(('EOF', None))
    return tokens

        