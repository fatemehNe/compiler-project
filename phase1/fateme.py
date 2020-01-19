import ply.lex as lex
import re

fL = open("output.txt", "w")

tokens = [ 'NUMERROR','WHITESPACE', 'INTEGER', 'ID','REAL', 'STRING', 'COMMENT', 'CLASS', 'REFERENCE', 'SATATIC',
 'INT_TYPE', 'REAL_TYPE', 'BOOL_TYPE', 'STRING_TYPE', 'VOID', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'BREAK', 'CONTINUE', 'IF', 'ELSE',
 'ELSeIF','WHILE', 'FOR', 'TO', 'IN', 'STEPS', 'BITWISE_AND', 'AND', 'BITWISE_OR', 'OR', 'NOT', 'BITWISE_NOT', 'SHIFT_RIGHT',
 'SHIFT_LEFT', 'ASSIGNMENT', 'ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'MODULO', 'POWER', 'GT', 'GE', 'LT',
 'LE', 'EQ', 'NE', 'LCB' , 'RCB', 'LP', 'RP', 'DOT', 'SEMICOLON', 'COMMA', 'TOKENERROR']

def t_WHITESPACE(t):
    r"""\s+"""




def t_NUMERROR(t):
    r"""([0-9]+[ac-wyzAC-WYZ][a-zA-Z]*)|(0[0-9]+\.[0-9]*[1-9])|([1-9][0-9]*\.[0-9]+0)|(0+x+0+[0-9a-fA-F]+)|(0+b+0+[01]+)|(00+[0-9]*)"""
    # r"""(\s*[^\"]+\s)"""
    print("MY Error : ", t.value)
    txt ="***ERROR*** "+  "Lexem: "+ t.value +" Token: "+ "ERROR" + " Value: "+ "-" + "\n"
    fL.write(txt)

def t_REAL(t):
    r"""([1-9][0-9]*\.[0-9]*[1-9])|(0\.[0-9]*[1-9])|([1-9][0-9]*\.0)|(0\.0)"""
    print("Found real number : ", t.value  )
    txt = "Lexem: " + t.value + " Token: " + "REAL" + " Value: " + "-" + "\n"
    fL.write(txt)
    return t

def t_INTEGER(t):
    r"""(0x[1-9a-fA-F][0-9a-fA-F]*)|(0x0)|(0b1[01]*)|(0b0)|([1-9][0-9]*)|(0)"""
    if '0x' in t.value:
        dec = int(t.value, 16)
        print("Found integer : ", t.value, " , ",dec)
        txt = "Lexem: " + t.value + " Token: " + "INTEGER" + " Value: " + str(dec) + "\n"
        fL.write(txt)
    elif '0b' in t.value:
        dec = int(t.value, 2)
        txt = "Lexem: " + t.value + " Token: " + "INTEGER" + " Value: " + str(dec) + "\n"
        fL.write(txt)
        print("Found integer : ", t.value, " , ",dec)
    else:
        txt = "Lexem: " + t.value + " Token: " + "INTEGER" + " Value: " + t.value + "\n"
        fL.write(txt)
        print("Found integer : ", t.value)
    return t

def t_STRING(t):
    r"""(([\"](.*?)[\"]\s*\+\s*)*(\s*[\"](.*?)[\"]))|([\"](.*?)[\"])|([\"](.*?)\s*(.*?)[\"])"""
    list_of_tokens = t.value.split('"')
    new_list = []
    indexes = []
    for a in list_of_tokens:
        if '+' in a :
            indexes.append(list_of_tokens.index(a))
            replaced = re.sub('[ \t\n\r\f\v]', '', a)
            new_list.append(replaced)
    list_operands = []
    flag = 0
    for i in range(0, len(new_list)):
        if new_list[i] == '+':
            flag = 1
            index = indexes[i]
            if index - 1 == 0 or index+1 == len(list_of_tokens)-1:
                flag = 0
                break
            list_operands.append(list_of_tokens[index-1])
            if i == len(new_list)-1:
                    list_operands.append(list_of_tokens[index+1])

    if flag == 1:
        s = ''.join(list_operands)
    else:
        s = t.value
    txt = "Lexem: " + t.value + " Token: " + "STRING" + " Value: " + s + "\n"
    fL.write(txt)
    print("Found String : "+s)
    return t


def t_COMMENT(t):
    r'(\/\/[^\n]*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
    txt = "***COMMENT*** "+ "Lexem: " + t.value + " Token: " + "-" + " Value: " + "-" + "\n"
    fL.write(txt)
    print("comment: "+t.value)

def t_CLASS(t):
    r'class[ ]'
    txt = "Lexem: " + t.value + " Token: " + "CLASS" + " Value: " + "-" + "\n"
    fL.write(txt)
    print("this is class type : "+t.value)
    return t

def t_REFERENCE(t):
    r'reference'
    txt = "Lexem: " + t.value + " Token: " + "REFERENCE" + " Value: " + "-" + "\n"
    fL.write(txt)
    print("this is reference type : "+t.value)
    return t

def t_SATATIC(t):
    r'static[ ]'
    txt = "Lexem: " + t.value + " Token: " + "SATATIC" + " Value: " + "-" + "\n"
    fL.write(txt)
    print("this is static type : "+t.value)
    return t

def t_INT_TYPE(t):
    r'int[ ]'
    txt = "Lexem: " + t.value + " Token: " + "INT_TYPE" + " Value: " + "-" + "\n"
    fL.write(txt)
    print("this is int type : "+t.value)
    return t
def t_REAL_TYPE(t):
    r'real[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "REAL_TYPE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_BOOL_TYPE(t):
    r'bool[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "BOOL_TYPE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_VOID(t):
    r'void'
    txt = "Lexem: "+ t.value +" Token: "+ "VOID" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_TRUE(t):
    r'true'
    txt = "Lexem: "+ t.value +" Token: "+ "TRUE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_FALSE(t):
    r'false'
    txt = "Lexem: "+ t.value +" Token: "+ "FALSE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_PRINT(t):
    r'print'
    txt = "Lexem: "+ t.value +" Token: "+ "PRINT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_RETURN(t):
    r'return[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "RETURN" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_STRING_TYPE(t):
    r'string[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "STRING_TYPE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_BREAK(t):
    r'break'
    txt = "Lexem: "+ t.value +" Token: "+ "BREAK" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_CONTINUE(t):
    r'continue'
    txt = "Lexem: "+ t.value +" Token: "+ "CONTINUE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_IF(t):
    r'if'
    txt = "Lexem: "+ t.value +" Token: "+ "IF" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_ELSE(t):
    r'else'
    txt = "Lexem: "+ t.value +" Token: "+ "ELSE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_ELSEIF(t):
    r'elseif'
    txt = "Lexem: "+ t.value +" Token: "+ "ELSEIF" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_WHILE(t):
    r'while'
    txt = "Lexem: "+ t.value +" Token: "+ "WHILE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_FOR(t):
    r'for'
    txt = "Lexem: "+ t.value +" Token: "+ "FOR" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_TO(t):
    r'to[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "TO" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_IN(t):
    r'in[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "IN" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_STEPS(t):
    r'steps[ ]'
    txt = "Lexem: "+ t.value +" Token: "+ "STEPS" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_ID(t):
    r"""([a-zA-Z]\w*)|([a-zA-Z]\w*\_)|(\_\w*)|([a-zA-Z]\w*[\_\w]+\_\w*)|([\_\w]+\_\w+)"""
    l = len(t.value)
    if l%2 == 0:
        txt = "***ERROR*** "+ "Lexem: " + t.value + " Token: " + "ERROR" + " Value: " + "-" + "\n"
        fL.write(txt)
        print("this is error id : " + t.value)
    else:
        txt = "Lexem: " + t.value + " Token: " + "ID" + " Value: " + "-" + "\n"
        fL.write(txt)
        print("this is identifier : " + t.value)
        return t



def t_AND(t):
    r'&&'
    txt = "Lexem: "+ t.value +" Token: "+ "AND" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_BITWISE_AND(t):
    r'&'
    txt = "Lexem: "+ t.value +" Token: "+ "BITWISE_AND" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_OR(t):
    r'\|\|'
    txt = "Lexem: "+ t.value +" Token: "+ "OR" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_NOT(t):
    r'!'
    txt = "Lexem: "+ t.value +" Token: "+ "NOT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_BITWISE_OR(t):
    r'\|'
    txt = "Lexem: "+ t.value +" Token: "+ "BITWISE_OR" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_BITWISE_NOT(t):
    r'~'
    txt = "Lexem: "+ t.value +" Token: "+ "BITWISE_NOT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_SHIFT_RIGHT(t):
    r'>>'
    txt = "Lexem: "+ t.value +" Token: "+ "SHIFT_RIGHT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_SHIFT_LEFT(t):
    r'<<'
    txt = "Lexem: "+ t.value +" Token: "+ "SHIFT_LEFT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_ADDITION(t):
    r'\+'
    txt = "Lexem: "+ t.value +" Token: "+ "ADDITION" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_SUBTRACTION(t):
    r'-'
    txt = "Lexem: "+ t.value +" Token: "+ "SUBTRACTION" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_MULTIPLICATION(t):
    r'\*'
    txt = "Lexem: "+ t.value +" Token: "+ "MULTIPLICATION" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_DIVISION(t):
    r'\/'
    txt = "Lexem: "+ t.value +" Token: "+ "DIVISION" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_MODULO(t):
    r'%'
    txt = "Lexem: "+ t.value +" Token: "+ "MODULO" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_POWER(t):
    r'\^'
    txt = "Lexem: "+ t.value +" Token: "+ "POWER" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t


def t_GE(t):
    r'>='
    txt = "Lexem: "+ t.value +" Token: "+ "GE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_LE(t):
    r'<='
    txt = "Lexem: "+ t.value +" Token: "+ "LE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_GT(t):
    r'>'
    txt = "Lexem: "+ t.value +" Token: "+ "GT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_LT(t):
    r'<'
    txt = "Lexem: "+ t.value +" Token: "+ "LT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t


def t_EQ(t):
    r'=='
    txt = "Lexem: "+ t.value +" Token: "+ "EQ" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_NE(t):
    r'!='
    txt = "Lexem: "+ t.value +" Token: "+ "NE" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_ASSIGNMENT(t):
    r'='
    txt = "Lexem: "+ t.value +" Token: "+ "ASSIGNMENT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_LCB(t):
    r'{'
    txt = "Lexem: "+ t.value +" Token: "+ "LCB" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_RCB(t):
    r'}'
    txt = "Lexem: "+ t.value +" Token: "+ "RCB" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_LP(t):
    r'\('
    txt = "Lexem: "+ t.value +" Token: "+ "LP" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_RP(t):
    r'\)'
    txt = "Lexem: "+ t.value +" Token: "+ "RP" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_DOT(t):
    r'\.'
    txt = "Lexem: "+ t.value +" Token: "+ "DOT" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_SEMICOLON(t):
    r';'
    txt = "Lexem: "+ t.value +" Token: "+ "SEMICOLON" + " Value: "+ "-"+"\n"
    print(txt)
    fL.write(txt)
    return t

def t_COMMA(t):
    r','
    txt = "Lexem: "+ t.value +" Token: "+ "COMMA" + " Value: "+ "-" +"\n"
    print(txt)
    fL.write(txt)
    return t

def t_TOKENERROR(t):
    r"""(\s*(.+?)+\s*)|(\s*[^\"]+\s*)"""
    txt = "***ERROR*** "+"Lexem: "+ t.value +" Token: "+ "-" + " Value: "+ "-" +"\n"
    print(txt)
    fL.write(txt)

lexer = lex.lex()

path = "input.txt"
f = open(path, 'r')
text = f.read()
f.close()


lexer.input(text)
while True:
 tok = lex.token()
 if not tok:
     break
