import ply.lex as lex
import sys

tokens = (
    'SELECT',
    'WHERE',
    'LIMIT',
    'PREFIX',
    'A',
    'COLON',
    'PREFIXNAME',
    'TERM',
    'VAR',
    'STRING',
    'COMMENT',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'DOT',
    'LANGTAG',
    'TYPE',
    'IRI',
)

t_SELECT   = r'(?i)select'
t_WHERE    = r'(?i)where'
t_LIMIT    = r'(?i)limit'
t_PREFIX   = r'(?i)prefix'
t_A        = r'(?i)\ba\b'

t_COLON    = r':'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_DOT      = r'\.'
t_LANGTAG  = r'@[a-zA-Z]+(\-[a-zA-Z0-9]+)*'
t_TYPE     = r'\^\^'

def t_PREFIXNAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*(?=\:)'
    return t

def t_TERM(t):
    r'(?<=\:)[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

def t_VAR(t):
    r'\?[a-zA-Z0-9_]+'
    return t

def t_STRING(t):
    r'\"([^"\\]|\\.)*\"'
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IRI(t):
    r'<[^>]*>'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = sys.stdin.read()
    lexer.input(data)
    for token in lexer:
        print(token)
