import ply.lex as lex
import re
import sys 

tokens = (
#OPERADORES ARITMETICOS Y RELACIONALES    
"SUMA", "MENOS", "MULTIPLICAR", "DIVISION",
"IGUALQUE", "MENORQUE", "MENORIGUALQUE", "MAYORQUE", "MAYORIGUALQUE", "PARENTIZQ", "PARENTDER", "COMA",
"PTCOMA", "PUNTO","IGUALIGUAL","CORCHETEIZQ","CORCHETEDER","COMILLA","DOPUNTOS","MODULO", "LLAVEIZQ", "LLAVEDER", 
#PALABRAS RESERVADAS  
"AND", "BREAK", "CLASS", "DEF", "PASS", "FOR", "FROM", "PRINT",
"IF", "IMPORT", "IN", "IS","CONTINUE", "FINALLY","LEN", "RANGE", "STR",
#OTHERS
"ID","NUMBER", "COMMENT"

)

#IGNORAR CARACTER
t_ignore =        '\t'

def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Caracter Illegal" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)

#OPERADORES ARITMETICOS Y RELACIONALES 

t_SUMA = r'\+'
t_MENOS = r'\-'
t_MULTIPLICAR = r'\*'
t_DIVISION = r'/'
t_IGUALQUE = r'='
t_MENORQUE = r'<'
t_MENORIGUALQUE = r'<='
t_MAYORQUE = r'>'
t_MAYORIGUALQUE = r'>='
t_IGUALIGUAL = r'=='
t_COMILLA = r'"'
t_MODULO = r'%'
#SIMBOLOS
t_PARENTIZQ =     r'\('
t_PARENTDER =     r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_COMA =          r','
t_PTCOMA =        r';'
t_PUNTO =         r'\.'
t_DOPUNTOS =      r':'

#PALABRAS RESERVADAS

def t_AND(t):
    r'and'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_DEF(t):
    r'def'
    return t

def t_PASS(t):
    r'pass'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FROM(t):
    r'from'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_IN(t):
    r'in'
    return t

def t_IS(t):
    r'is'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_LEN(t):
    r'len'
    return t

def t_RANGE(t):
    r'range'
    return t

def t_STR(t):
    r'str'
    return t

#OTROS

def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_COMMENT(t):
    r'[\/{2}\w+\s+]+'
    pass 


lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]

        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27) + "[0;36m" + "INICIA ANALISIS LEXICO" + chr(27) + "[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(
                "\t"
                + str(i)
                + " - "
                + "Line: "
                + str(tok.lineno)
                + "\t"
                + str(tok.type)
                + "\t-->  "
                + str(tok.value)
            )
            i += 1

        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")

    else:
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp py como parametro")
        print(
            chr(27)
            + "[0;36m"
            + "\t$ python AnalizadorLexico.py"
            + chr(27)
            + "[1;31m"
            + " <filename>.py"
            + chr(27)
            + "[0m"
        )
