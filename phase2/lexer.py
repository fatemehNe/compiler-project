from ply import lex


class Lexer():
    tokens = ['NUMERROR', 'WHITESPACE', 'INTEGER', 'ID', 'REAL', 'STRING', 'COMMENT', 'CLASS', 'REFERENCE', 'STATIC',
              'INT_TYPE', 'REAL_TYPE', 'BOOL_TYPE', 'STRING_TYPE', 'VOID', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'BREAK',
              'CONTINUE', 'IF', 'ELSE',
              'ELSEIF', 'WHILE', 'FOR', 'TO', 'IN', 'STEPS', 'BITWISE_AND', 'AND', 'BITWISE_OR', 'OR', 'NOT',
              'BITWISE_NOT', 'SHIFT_RIGHT',
              'SHIFT_LEFT', 'ASSIGNMENT', 'ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'MODULO', 'POWER',
              'GT', 'GE', 'LT',
              'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LP', 'RP', 'DOT', 'SEMICOLON', 'COMMA', 'TOKENERROR']

    def t_WHITESPACE(self, t):
        r"""\s+"""

    def t_NUMERROR(self, t):
        r"""([0-9]+[ac-wyzAC-WYZ][a-zA-Z]*)|(0[0-9]+\.[0-9]*[1-9])|([1-9][0-9]*\.[0-9]+0)|(0+x+0+[0-9a-fA-F]+)|(0+b+0+[01]+)|(00+[0-9]*)"""
        txt = "***ERROR*** " + "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ERROR" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        

    def t_REAL(self, t):
        r"""([1-9][0-9]*\.[0-9]*[1-9])|(0\.[0-9]*[1-9])|([1-9][0-9]*\.0)|(0\.0)"""
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "REAL" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_INTEGER(self, t):
        r"""(0x[1-9a-fA-F][0-9a-fA-F]*)|(0x0)|(0b1[01]*)|(0b0)|([1-9][0-9]*)|(0)"""
        if '0x' in t.value:
            dec = int(t.value, 16)
            txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "INTEGER" + "\t" + " Attribute: " + "\t" + str(
                dec) + "\n\n"
            
        elif '0b' in t.value:
            dec = int(t.value, 2)
            txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "INTEGER" + "\t" + " Attribute: " + "\t" + str(
                dec) + "\n\n"
            
        else:
            txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "INTEGER" + "\t" + " Attribute: " + "\t" + t.value + "\n\n"
            
        return t

    def t_STRING(self, t):
        r"""(([\"](.*?)[\"]\s*\+\s*)*(\s*[\"](.*?)[\"]))|([\"](.*?)[\"])|([\"](.*?)\s*(.*?)[\"])"""
        # list_of_tokens = t.value.split('"')
        # new_list = []
        # indexes = []
        # for a in list_of_tokens:
        #     if '+' in a:
        #         indexes.append(list_of_tokens.index(a))
        #         replaced = re.sub('[ \t\n\r\f\v]', '', a)
        #         new_list.append(replaced)
        # list_operands = []
        # flag = 0
        # for i in range(0, len(new_list)):
        #     if new_list[i] == '+':
        #         flag = 1
        #         index = indexes[i]
        #         if index - 1 == 0 or index + 1 == len(list_of_tokens) - 1:
        #             flag = 0
        #             break
        #         list_operands.append(list_of_tokens[index - 1])
        #         if i == len(new_list) - 1:
        #             list_operands.append(list_of_tokens[index + 1])
        #
        # if flag == 1:
        #     s = ''.join(list_operands)
        # else:
        #     s = t.value
        # txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "STRING" + "\t" + " Attribute: " + "\t" + s + "\n\n"
        # print("Found String : "+s)
        return t

    def t_COMMENT(self, t):
        r'(\/\/[^\n]*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
        txt = "***COMMENT*** " + "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "-" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        

    def t_CLASS(self, t):
        r'class[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "CLASS" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_REFERENCE(self, t):
        r'reference'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "REFERENCE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_STATIC(self, t):
        r'static[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "STATIC" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_INT_TYPE(self, t):
        r'int[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "INT_TYPE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_REAL_TYPE(self, t):
        r'real[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "REAL_TYPE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_BOOL_TYPE(self, t):
        r'bool[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "BOOL_TYPE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_VOID(self, t):
        r'void'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "VOID" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_TRUE(self, t):
        r'true'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "TRUE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_FALSE(self, t):
        r'false'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "FALSE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_PRINT(self, t):
        r'print'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "PRINT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_RETURN(self, t):
        r'return[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "RETURN" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_STRING_TYPE(self, t):
        r'string[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "STRING_TYPE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_BREAK(self, t):
        r'break'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "BREAK" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_CONTINUE(self, t):
        r'continue'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "CONTINUE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_IF(self, t):
        r'if'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "IF" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_ELSE(self, t):
        r'else'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ELSE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_ELSEIF(self, t):
        r'elseif'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ELSEIF" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_WHILE(self, t):
        r'while'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "WHILE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_FOR(self, t):
        r'for'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "FOR" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_TO(self, t):
        r'to[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "TO" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_IN(self, t):
        r'in[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "IN" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_STEPS(self, t):
        r'steps[ ]'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "STEPS" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_ID(self, t):
        r"""([a-zA-Z]\w*)|([a-zA-Z]\w*\_)|(\_\w*)|([a-zA-Z]\w*[\_\w]+\_\w*)|([\_\w]+\_\w+)"""
        l = len(t.value)
        if l % 2 == 0:
            txt = "***ERROR*** " + "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ERROR" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
            
        else:
            return t

    def t_AND(self, t):
        r'&&'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "AND" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_BITWISE_AND(self, t):
        r'&'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "BITWISE_AND" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_OR(self, t):
        r'\|\|'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "OR" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_NOT(self, t):
        r'!'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "NOT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_BITWISE_OR(self, t):
        r'\|'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "BITWISE_OR" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_BITWISE_NOT(self, t):
        r'~'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "BITWISE_NOT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_SHIFT_RIGHT(self, t):
        r'>>'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "SHIFT_RIGHT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_SHIFT_LEFT(self, t):
        r'<<'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "SHIFT_LEFT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_ADDITION(self, t):
        r'\+'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ADDITION" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_SUBTRACTION(self, t):
        r'-'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "SUBTRACTION" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_MULTIPLICATION(self, t):
        r'\*'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "MULTIPLICATION" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_DIVISION(self, t):
        r'\/'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "DIVISION" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_MODULO(self, t):
        r'%'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "MODULO" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_POWER(self, t):
        r'\^'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "POWER" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_GE(self, t):
        r'>='
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "GE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_LE(self, t):
        r'<='
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "LE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_GT(self, t):
        r'>'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "GT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_LT(self, t):
        r'<'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "LT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_EQ(self, t):
        r'=='
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "EQ" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_NE(self, t):
        r'!='
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "NE" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_ASSIGNMENT(self, t):
        r'='
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "ASSIGNMENT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_LCB(self, t):
        r'{'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "LCB" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_RCB(self, t):
        r'}'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "RCB" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_LP(self, t):
        r'\('
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "LP" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_RP(self, t):
        r'\)'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "RP" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_DOT(self, t):
        r'\.'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "DOT" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_SEMICOLON(self, t):
        r';'
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "SEMICOLON" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_COMMA(self, t):
        r','
        txt = "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "COMMA" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        
        return t

    def t_TOKENERROR(self, t):
        r"""(\s*(.+?)+\s*)|(\s*[^\"]+\s*)"""
        txt = "***ERROR*** " + "Lexeme: " + "\t" + t.value + "\t" + " Token: " + "\t" + "-" + "\t" + " Attribute: " + "\t" + "-" + "\n\n"
        

    def build(self, **kwargs):
        '''
        build the lexer
        '''
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer