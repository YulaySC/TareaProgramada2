import ply.lex as lex 

# List of token names.   This is always required
tokens = [
 # Literals (identifier, integer constant, float constant, string constant, char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST','NAME',#'NUM'

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    
    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Structure dereference (->)
    'ARROW',

    # Ternary operator (?)
    'TERNARY',
    
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',

    'FLOAT','INTEGER','CHARACTER','STRING','INCREMENT','DECREMENT','MODULO'
]
    
# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators

t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'^='

# Increment/decrement
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

# ->
t_ARROW            = r'->'

# ?
t_TERNARY          = r'\?'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers
t_ID = r'[A-Z][A-Za-z0-9_]*'
t_NAME    = r'[a-z][a-zA-Z0-9_]*'
#t_NUM=r'[0-9]*'

# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comment (C-Style)
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

# Comment (C++-Style)
def t_CPPCOMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t.type

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
#def t_NEWLINE(t):
#    r'\n'
#    t.lexer.lineno += 1
#    return t
#def t_ID(t):
#    r'[A-Z][A-Z0-9]*'
#    if t.value in keywords:
#        t.type = t.value
#    return t
    


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)

# Build the lexer

#print('PRUEBA------ DIGITE LO QUE DESEE:')
#data=input()
#lexer.input(data)

# Tokenize
def lexicalTYPE (data):
    lexer = lex.lex()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        return (tok.type)
           
        for tok in lexer:
            return (tok.type)
        
def RetlexicalTYPE(data):
    lexer = lex.lex()
    lexer.input(data)
    elem=[]
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        elem.append(tok.type)
        #return (elem)
           
        for tok in lexer:
            elem.append(tok.type)
    return (elem)

def PARENT(data):
    elementos=RetlexicalTYPE(data)
    cont=len(elementos)-1
    contador=len(elementos)-1
    
    print (cont)
    print(contador)
    existe=False
    while(cont>=0):
        if((elementos[cont])=='LPAREN'):
            if((elementos[contador-1])=='RPAREN'):
                existe=True
                return (existe)
        cont=cont-1

    return (existe)
            

def arg(data):
    lexer = lex.lex()
    lexer.input(data)
    elem=[]
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        elem.append(tok.type)
        return (elem)
           
        for tok in lexer:
            elemn.append(tok.type)
            return (elemn)
        
def lexicalVALUE (data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        return(tok.value)
           
        for tok in lexer:
            return(tok.value)

def sintaxis():
 print ('Welcome to SWI-Prolog (Multi-threaded, 32 bits, Version 6.6.4 n/Copyright (c) 1990-2013 University of Amsterdam, VU Amsterdam n/SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software, n/and you are welcome to redistribute it under certain conditions. n/Please visit http://www.swi-prolog.org for details. n/For help, use ?- help(Topic). or ?- apropos(Word).')
 val1=input()
 datos=[]
 lexer = lex.lex()
 elementos=[]
 y=False
 boolean= False
 if (val1=='<define>'):
     
     while(y==False):
    #print('entro')
         print ('>>')
         val1=input()
         data=val1
         cont=0
         elementos=RetlexicalTYPE(data)
         contlistelem=len(elementos)-1
         if (elementos[0]=='NAME'):
             if(elementos[contlistelem]=='PERIOD'):
                 if (val1!='</define>.'):
                     datos.append(val1)
        #print(datos[cont])
                     cont=cont+1
                     print ('>>')
                     val1=input()
    #print ('salio')
         if (val1=='</define>.'):
             y=True
         else:
             print ('Valor invalido')
             print ('>>')
             val1=input()
        
 if(val1=='</define>.'):
     print('?')
     val2=input()
     int=0
     x=False
     while(x==False):
         for i in range(0,len(datos)):
             cont=cont-1
             if(val2==datos[cont]):
                 boolean=True
             cont=cont-1
         x=True
     if(boolean==True):
         print('Yes')
     else:
         print('No')
       
        #print ('salio')
 else:
     print('error')

#class Aridad:
#    cont=0;
#    val=""
#    const=""
#    def contador(self,dato):
#        if 
    
