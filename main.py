from lexer import lexer


def main():
    calculator_language: str = "2 + 3"
    print(lexer(calculator_language))

main()