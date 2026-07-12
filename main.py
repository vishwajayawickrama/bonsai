from lexer import lexer
from parser import Parser


def main():
    calculator_language: str = "2 + 3 * 3"
    tokens = lexer(calculator_language)
    print(f"Lexered Tokens: {tokens}")
    parser = Parser(tokens)
    abstract_syntax_tree = parser.parse()
    parser.print_ast(abstract_syntax_tree)
    

main()