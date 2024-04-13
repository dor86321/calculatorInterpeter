import ply.yacc as yacc
from .lexer import tokens, lexer


# Parsing rules and precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'EXPONENT'),
    ('nonassoc', 'UMINUS'),
)

# Dictionary of names (for storing variables)
names = {}

def p_program(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_statement(p):
    '''statement : assignment
                 | expr
                 | if_statement
                 | while_statement
                 | empty'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : IDENTIFIER EQUALS expr'
    names[p[1]] = p[3]

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr EXPONENT expr'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == 'x' or p[2] == 'X': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    elif p[2] == '^': p[0] = p[1] ** p[3]

def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = -p[2]

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_expr_identifier(p):
    'expr : IDENTIFIER'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_if_statement(p):
    'if_statement : IF expr COLON statement_list'
    if p[2]:
        p[0] = p[4]

def p_while_statement(p):
    'while_statement : WHILE expr COLON statement_list'
    while p[2]:
        p[0] = p[4]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
