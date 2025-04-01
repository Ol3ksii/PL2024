import ply.yacc as yacc
from exp_analex import tokens

def p_exp_binop(p):
    """
    exp : exp PLUS term
        | exp MINUS term
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:  # '-'
        p[0] = p[1] - p[3]

def p_exp_term(p):
    """
    exp : term
    """
    p[0] = p[1]

def p_term_binop(p):
    """
    term : term TIMES factor
         | term DIV factor
    """
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:  # '/'
        p[0] = p[1] / p[3]

def p_term_factor(p):
    """
    term : factor
    """
    p[0] = p[1]

def p_factor_group(p):
    """
    factor : LPAREN exp RPAREN
    """
    p[0] = p[2]

def p_factor_num(p):
    """
    factor : NUM
    """
    p[0] = int(p[1])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            result = parser.parse(line)
            print(f"Result: {result}")
        except Exception as e:
            print("Error:", e)
