import ply.lex as lex

tokens = [
    'NUM',
    'PLUS', 'MINUS',
    'TIMES', 'DIV',
    'LPAREN', 'RPAREN'
]

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIV    = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUM    = r'\d+'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
