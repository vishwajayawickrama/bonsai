# Parsing grammer.
# expr   = term (('+' | '-') term)*
# term   = factor (('*' | '/') factor)*
# factor = NUM | '(' expr ')'

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.position = 0

    def peek(self) -> set:
        return self.tokens[self.position]
    
    def get_token(self):
        token = self.tokens[self.position]
        self.position += 1
        return token
    
    def parse(self):
        node = self.expression()
        if self.peek()[0] != 'EOF':
            raise SyntaxError ("parser: trailing tokens")
        return node

    def print_ast(self, node, depth=0):
        indent = "  " * depth

        if not isinstance(node, tuple):
            print(f"{indent}{node}")
            return

        kind = node[0]

        if kind == 'binop':
            _, op, left, right = node
            print(f"{indent}{kind}: {op[1]}")
            self.print_ast(left, depth + 1)
            self.print_ast(right, depth + 1)
            return

        if len(node) == 2:
            kind, value = node
            print(f"{indent}{kind}: {value}")
            return

        print(f"{indent}{node}")

    def expression(self):
        node = self.term()
        while self.peek() in [('OP', '+'), ('OP', '-')]:
            op = self.get_token()
            node = ('binop', op, node, self.expression())
        
        return node

    def term(self):
        node = self.factor()
        while self.peek() in [('OP', '*'), ('OP', '/')]:
            op = self.get_token()
            node = ('binop', op, node, self.factor())
        
        return node
 
    def factor(self):
        kind, value = self.peek()
        if kind == 'NUM':
            return self.get_token()
        
        if self.peek()== ('OP', '('):
            self.get_token()
            node = self.expression() 
            if self.peek() != ('OP' ,')'):
                raise SyntaxError ("parser: expected')'")
            self.get_token()
            return node
        
        raise SyntaxError (f"parser: unexpected {self.peek()}")