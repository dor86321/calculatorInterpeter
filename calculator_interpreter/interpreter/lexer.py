import ply.lex as lex


tokens = (
    'NUMBER', 'TIMES', 'IDENTIFIER',
    'PLUS', 'MINUS', 'DIVIDE', 'EXPONENT',
    'ASSIGN', 'LPAREN', 'RPAREN', 'COLON',
    'IF', 'WHILE', 'NEWLINE', 'EQUALS', 'LESS_THAN', 'GREATER_THAN', 'LESS_THAN_EQUALS', 'GREATER_THAN_EQUALS'
)
# Reserved keywords
reserved = {
    'if': 'IF',
    'while': 'WHILE'
}

# Token specifications
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'[Xx]'
t_DIVIDE = r'/'
t_EXPONENT = r'\^'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_NEWLINE = r'\n'
t_EQUALS = r'=='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUALS = r'<='
t_GREATER_THAN_EQUALS = r'>='


# Token rules for reserved keywords
def t_IF(t):
    r'if'
    t.type = reserved.get(t.value, 'IF')
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value, 'WHILE')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z]*'
    if t.value.lower() == 'x':
        t.type = 'TIMES'
    else:
        t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()