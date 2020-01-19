from classes.code_generator import CodeGenerator
from classes.nonterminal import Nonterminal

#start

import ply.yacc as yacc

import lexer as l

class Parser:
    def __init__(self):
        self.scope_counter = -1
        self.t_counter = -1
        self.l_counter = -1
        self.code_generator = CodeGenerator()
        self.code_list = []
        self.TRUE_LABEL = "TRUE_LABEL"
        self.FALSE_LABEL = "FALSE_LABEL"
        self.NEXT_LABEL = "NEXT_LABEL"
        self.VARIABLES = []
        self.FuncVARIABLES = []
        self.check = False
        self.symbol_table_list = []
        self.func_table = []
        self.variable_decs = ""

    tokens = l.tokens
    def p_program(self, p):
        """program : macros classes"""
        print("""program -> macros classes""")
        p[0] = Nonterminal()

        p[0].sym_var = p[2].sym_var

        print("symbol table list :")
        print(self.symbol_table_list)

        include = "#include <stdio.h>" + "\n"
        include += "#include <stdio.h>" + "\n"
        if self.t_counter > -1:
            variables_declaration = "double "
            for i in range(0, self.t_counter + 1):
                if i == self.t_counter:
                    variables_declaration += "TT" + str(i) + ";"
                else:
                    variables_declaration += "TT" + str(i) + ", "
        else:
            variables_declaration = ""
        stack_components_declaration = "void* returnAddress;\ndouble * top = (double*) malloc(1000 * sizeof(double));\nvoid ** labelsTop = (void**) malloc(1000 * sizeof(void*));\ntop += 1000;\nlabelsTop += 1000;"
        goto_to_main = "goto _main;\n\n"
        p[0].code = include + "int main()\n{\n\n" + stack_components_declaration + "\n" + variables_declaration + "\n"+ self.variable_decs  + goto_to_main + p[2].code + "\n\nend : return 0;\n}"
        file = open("final_result.c", "w")
        file.write(p[0].code)
        file.close()



    def p_macros(self, p):
        """macros : macros macro"""
        print("""macros -> macros macro""")

    def p_macros_e(self, p):
        """macros : """
        print("""macros ->/* Lambda */""")

    def p_macro(self, p):
        """macro : reference"""
        print("""macro -> reference""")

    def p_reference(self, p):
        """reference : REFERENCE STRING"""
        print("""reference -> REFERENCE STRING""")

    def p_classes(self, p):
        """classes : classes class"""
        print("""classes -> classes class""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[2].code
        p[0].sym_var = p[1].sym_var + p[2].sym_var


    def p_classes_e(self, p):
        """classes : """
        print("""classes ->/* Lambda */""")
        p[0] = Nonterminal()
        p[0].code = ""
        p[0].sym_var = []

    def p_class(self, p):
        """class : CLASS ID LCB symbol_decs RCB"""
        print("""class -> CLASS ID LCB symbol_decs RCB""")
        p[0] = Nonterminal()
        p[0].code = p[4].code
        p[0].sym_var = p[4].sym_var


    def p_symbol_decs(self, p):
        """symbol_decs : symbol_decs symbol_dec"""
        print("""symbol_decs -> symbol_decs symbol_dec""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[2].code
        p[0].sym_var = p[1].sym_var + p[2].sym_var


    def p_symbol_decs_e(self, p):
        """symbol_decs : """
        print("""symbol_decs ->/* Lambda */""")
        p[0] = Nonterminal()
        p[0].code = ""

    def p_symbol_dec_1(self, p):
        """symbol_dec : var_dec"""
        print("""symbol_dec -> var_dec""")
        p[0] = Nonterminal()
        p[0].code = p[1].code


    def p_symbol_dec_2(self, p):
        """symbol_dec : func_dec"""
        print("""symbol_dec -> func_dec""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var


    def p_var_dec(self, p):
        """var_dec : var_type var_list SEMICOLON"""
        print("""var_dec -> var_type var_list SEMICOLON""")
        p[0] = Nonterminal()
        self.variable_decs += [p[1].rtype + " " + var + ";\n" for var in p[2].vars]
        self.VARIABLES += p[2].vars
        p[0].code = "\n" + p[2].code

    def p_var_type_1(self, p):
        """var_type : return_type"""
        print("""var_type -> return_type""")
        p[0] = Nonterminal()
        p[0].rtype = p[1].rtype

    # lvalue1
    def p_var_type_1_1(self, p):
        """var_type : lvalue1"""
        print("""var_type -> lvalue1""")

    def p_var_type_2(self, p):
        """var_type : STATIC return_type"""
        print("""var_type -> STATIC return_type""")

    def p_var_type_2_1(self, p):
        """var_type : STATIC lvalue1"""
        print("""var_type -> STATIC lvalue1""")

    def p_return_type_1(self, p):
        """return_type : INT_TYPE"""
        print("""return_type -> INT_TYPE""")
        p[0] = Nonterminal()
        p[0].rtype = "double"
        p[0].sym_rtype = "int"

    def p_return_type_2(self, p):
        """return_type : REAL_TYPE"""
        print("""return_type -> REAL_TYPE""")
        p[0] = Nonterminal()
        p[0].rtype = "double"
        p[0].sym_rtype = "real"

    def p_return_type_3(self, p):
        """return_type : BOOL_TYPE"""
        print("""return_type -> BOOL_TYPE""")
        p[0] = Nonterminal()
        p[0].rtype = "bool"
        p[0].sym_rtype = "bool"

    def p_return_type_4(self, p):
        """return_type : STRING_TYPE"""
        print("""return_type -> STRING_TYPE""")
        p[0] = Nonterminal()
        p[0].rtype = "char*"
        p[0].sym_rtype = "string"

    # def p_return_type_5(self, p):
    #     """return_type : ID"""

    def p_var_list_1(self, p):
        """var_list : var_list COMMA var_list_item"""
        print("""var_list -> var_list COMMA var_list_item""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[3].code
        p[0].vars = p[1].vars + p[3].vars


    def p_var_list_2(self, p):
        """var_list : var_list_item"""
        print("""var_list -> var_list_item""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].vars = p[1].vars


    def p_item1(self, p):
        """item1 : ID ASSIGNMENT exp"""
        print("""item1 -> ID ASSIGNMENT exp""")
        p[0] = Nonterminal()
        p[0].code = p[3].code + p[1] + " = " + p[3].get_value() + ";\n"
        p[0].vars = [p[1]]

    def p_var_list_item_2(self, p):
        """var_list_item : item1"""
        print("""var_list_item -> item1""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].vars = p[1].vars


    def p_var_list_item_1(self, p):
        """var_list_item : ID"""
        print("""var_list_item -> ID""")
        p[0] = Nonterminal()
        p[0].code = ""
        p[0].vars = [p[1]]

    ############2
    def p_func_dec(self, p):
        """func_dec : var_type func_body"""
        print("""func_dec -> var_type func_body""")
        p[0] = Nonterminal()
        p[0].code = p[2].code
        p[0].sym_var = p[2].sym_var
        dic = {}
        dic["ref"] = "NONE"
        dic["name"] = p[2].func_name
        dic["type"] = "FUNCTION"
        dic["v_type"] = "NONE"
        dic["size"] = "NONE"
        dic["address"] = "NONE"
        dic["return_type"] = p[1]
        p[0].sym_var.append(dic)

    def p_func_dec_1(self, p):
        """func_dec : VOID func_body"""
        print("""func_dec -> VOID func_body""")
        p[0] = Nonterminal()
        p[0].code = p[2].code
        p[0].sym_var = p[2].sym_var
        dic = {}
        dic["ref"] = "NONE"
        dic["name"] = p[2].func_name
        dic["type"] = "FUNCTION"
        dic["v_type"] = "NONE"
        dic["size"] = "NONE"
        dic["address"] = "NONE"
        dic["return_type"] = p[1]
        p[0].sym_var.append(dic)

    def p_func_dec_2(self, p):
        """func_dec : STATIC VOID func_body"""
        print("""func_dec -> STATIC VOID func_body""")
        p[0] = Nonterminal()
        p[0].code = p[3].code
        p[0].sym_var = p[3].sym_var
        dic = {}
        dic["ref"] = "NONE"
        dic["name"] = p[3].func_name
        dic["type"] = "FUNCTION"
        dic["v_type"] = "NONE"
        dic["size"] = "NONE"
        dic["address"] = "NONE"
        dic["return_type"] = p[2]
        p[0].sym_var.append(dic)

    def p_func_body(self, p):
        """func_body : ID LP formal_arguments RP block"""
        print("""func_body -> ID LP formal_arguments RP block""")
        p[0] = Nonterminal()

        return_phrase = "goto end;\n\n" if p[1] == "_main" else CodeGenerator.popReturnAddr(self) + "goto *returnAddress; // return from function\n\n"
        p[0].code = "//function body ----------- \n" + p[1] + ": //function decleration\n\n" + p[3].code + "\n // function body:\n" + p[5].code + "\n// function ended\n" + return_phrase
        # self.variable_decs = ""
        print(p[0].code)
        p[0].func_name = p[1]
        p[0].sym_var = p[5].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        #save a scope
        self.symbol_table_list.append(p[0].sym_var)

    def p_formal_arguments(self, p):
        """formal_arguments : formal_arguments_list"""
        print("""formal_arguments -> formal_arguments_list""")
        p[0] = Nonterminal()
        p[0].code = "// fetching arguments\n\n" + p[1].code
        p[0].t = p[1].t

    def p_formal_arguments_e(self, p):
        """formal_arguments : """
        print("""formal_arguments ->/* Lambda */""")
        p[0] = Nonterminal()
        p[0].t = 0
        p[0].code = ""

    def p_formal_arguments_list(self, p):
        """formal_arguments_list : formal_arguments_list COMMA formal_argument"""
        print("""formal_arguments_list -> formal_arguments_list COMMA formal_argument""")
        p[0] = Nonterminal()
        p[0].code = p[3].code + p[1].code
        p[0].t = p[1].t + p[3].t

    def p_formal_arguments_list_1(self, p):
        """formal_arguments_list : formal_argument"""
        print("""formal_arguments_list -> formal_argument""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].t = 1

    def p_formal_argument(self, p):
        """formal_argument : return_type ID"""
        print("""formal_argument -> return_type ID""")
        p[0] = Nonterminal()
        p[0].code = CodeGenerator.popVariable(self, p[2])
        p[0].t = 1

    # lvalue1
    def p_formal_argument_1(self, p):
        """formal_argument : lvalue1 ID"""
        print("""formal_argument -> lvalue1 ID""")


    def p_block(self, p):
        """block : LCB statements_list RCB"""
        print("""block -> LCB statements_list RCB""")
        p[0] = Nonterminal()
        p[0].code = p[2].code
        p[0].sym_var = p[2].sym_var

    def p_block_s(self, p):
        """block : statement"""
        print("""block -> statement""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_statements_list(self, p):
        """statements_list : statements_list statement"""
        print("""statements_list -> statements_list statement""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[2].code
        p[0].sym_var = p[1].sym_var + p[2].sym_var


    def p_statements_list_e(self, p):
        """statements_list : """
        p[0] = Nonterminal()
        p[0].code = ""
        print("""statements_list ->/* Lambda */""")

    def p_statement(self, p):
        """statement : SEMICOLON"""
        print("""statement -> SEMICOLON""")
        p[0] = Nonterminal()
        p[0].code = ";"

    def p_statement0(self, p):
        """statement : exp SEMICOLON"""
        # %prec EXPE
        print("""statement -> exp""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + ";\n"

    def p_statement_1(self, p):
        """statement : assignment"""
        print("""statement -> assignment""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        self.check= False
        print(p[0].code)


    def p_statement_2(self, p):
        """statement : print"""
        print("""statement -> print""")
        p[0] = Nonterminal()
        p[0].code = p[1].code

    def p_statement_3(self, p):
        """statement : statement_var_dec"""
        print("""statement -> statement_var_dec""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var


    def p_statement_4(self, p):
        """statement : if"""
        print("""statement -> if""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_statement_5(self, p):
        """statement : for"""
        print("""statement -> for""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_statement_6(self, p):
        """statement : while"""
        print("""statement -> while""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_statement_7(self, p):
        """statement : return"""
        print("""statement -> return""")
        p[0] = Nonterminal()
        p[0].code = p[1].code

    def p_statement_8(self, p):
        """statement : break"""
        print("""statement -> break""")

    def p_statement_9(self, p):
        """statement : continue"""
        print("""statement -> continue""")

    ############3
    def p_assignment(self, p):
        """assignment : lvalue ASSIGNMENT exp SEMICOLON"""
        # print("""assignment -> lvalue ASSIGNMENT exp SEMICOLON""")
        p[0] = Nonterminal()
        if p[3].func == 1:
            p[0].code = p[3].code + "\n" + p[1].get_value() + "=" + p[3].get_value() +";\n"
            print(p[0].code)
            self.check = True
        else:
            p[0].code = p[3].code + p[1].place + " = " + p[3].get_value() + ";\n"

        if self.check == False:
            self.FuncVARIABLES.append(p[1].get_value())

    def p_lvalue_1(self, p):
        """lvalue : lvalue1 %prec LVALI"""
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].place = p[1].place
        print("""lvalue -> lvalue1""")

    def p_lvalue_2(self, p):
        """lvalue : lvalue2 %prec LVAL"""
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].place = p[1].place
        print("""lvalue -> lvalue2""")

    def p_lval2(self, p):
        """lvalue2 : ID DOT ID"""
        print("""lvalue2 -> ID DOT ID""")

    def p_lval1(self, p):
        """lvalue1 : ID"""
        print("""lvalue1 -> ID""")
        p[0] = Nonterminal()
        p[0].place = p[1]


    def p_print(self, p):
        """print : PRINT LP STRING RP SEMICOLON"""
        print("""print -> PRINT LP STRING RP SEMICOLON""")
        p[0] = Nonterminal()
        p[0].code = 'printf("%lf", ' + p[3].split('{')[1].split('}')[0] + '); \n'


    def p_statement_var_dec(self, p):
        """statement_var_dec : return_type var_list SEMICOLON"""
        print("""statement_var_dec -> return_type var_list SEMICOLON""")
        p[0] = Nonterminal()
        self.variable_decs += "\n".join([p[1].rtype + " " + var + ";\n" for var in p[2].vars])
        self.VARIABLES += p[2].vars
        p[0].code = "\n" + p[2].code
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        for i in range(0, len(p[2].vars)):
            dic = {}
            dic["ref"]="NONE"
            dic["name"] = p[2].vars[i]
            dic["type"] = "VARIABLE"
            dic["v_type"] = p[0].sym_rtype
            if dic["v_type"] == "int":
                dic["size"] = 4
            elif dic["v_type"] == "real":
                dic["size"] = 8
            elif dic["v_type"] == "bool":
                dic["size"] = 1
            elif dic["v_type"] == "string":
                dic["size"] = 6
            else:
                dic["size"] = 0

            if i == 0 :
                dic["address"] = "NONE"
            else:
                dic["address"] = "NONE"

            dic["return_type"] = "NONE"

            p[0].sym_var.append(dic)

        print(p[0].sym_var)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    def p_statement_var_dec_1(self, p):
        """statement_var_dec : lvalue1 var_list SEMICOLON"""
        print("""statement_var_dec -> lvalue1 var_list SEMICOLON""")


    # def p_if_1(self, p):
    #     """if : IF LP exp RP block %prec IF"""
    #     print("""if -> IF LP exp RP block""")
    #     print("*****************************************************************")
    #     p[0] = Nonterminal()
    #     p[3].code = p[3].ifexp if p[3].ifexp else p[3].code
    #
    #     print("*****************************************************************")
    #     # print(p[3].true_list)
    #     # print(p[5].code)
    #     #
    #     # token_list = p[5].code.split(':')
    #     # self.backpatch(p[3].true_list, token_list[0])
    #     #
    #     # token_list = token_list[-2].split(";")
    #     # # print(token_list[-1])
    #     #
    #     # num = int(token_list[-1].replace("L", ""))
    #     # num = num + 1
    #     #
    #     # self.backpatch(p[3].false_list, "L"+ str(len(self.code_list)))
    #     # code = "L"+ str(len(self.code_list)) + ": "
    #     # self.code_list.append(code)
    #     #
    #     # print(self.code_list)
    #     # self.produce_output()
    #
    #
    # def p_if_2(self, p):
    #     """if : IF LP exp RP block ELSE block %prec ELSE"""
    #     #%prec IF2
    #     print("""if -> IF LP exp RP block ELSE block""")
    #     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #     p[0] = Nonterminal()
    #     print("true list")
    #     print(p[3].true_list)
    #     print("false list")
    #     print(p[3].false_list)
    #     print("if code")
    #     print(p[5].code)
    #     true_code = p[5].code
    #     print("else code")
    #     false_code = p[7].code
    #     print(p[7].code)
    #
    #     token_list = true_code.split(':')
    #     self.backpatch(p[3].true_list, token_list[0])
    #     #
    #     token_list = false_code.split(':')
    #     self.backpatch(p[3].false_list, token_list[0])
    #
    #     print(self.code_list)
    #     self.produce_output()
    #
    # def p_if_3(self, p):
    #     """if : IF LP exp RP block elseifs %prec prec2"""
    #     print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #     p[0] = Nonterminal()
    #     p[0].list = []
    #     p[3].list = []
    #     p[3].list.append(p[3].true_list)
    #     p[3].list.append(p[3].false_list)
    #
    #     num_of_elseifs = len(p[6].list)
    #
    #     p[0].list = p[6].list
    #     p[0].list.insert(0, p[3].list)
    #     # print(p[0].list)
    #     p[0].code_list = p[6].code
    #     p[0].code_list.insert(0, p[5].code)
    #     # print(p[0].code)
    #
    #     next_code_label = str(self.get_num_of_last_label(p[0].code_list[-1]) + 1)
    #     code = "L" + next_code_label + ": "
    #     self.code_list.append(code)
    #
    #     if_list = p[0].list[0]
    #     self.backpatch(if_list[0], self.get_start(p[0].code_list[0]))
    #     self.backpatch(if_list[1], "L" + str(p[0].list[1][0][0]))
    #
    #     for i in range(1, num_of_elseifs + 1):
    #         c = p[0].code_list[i]
    #         c_list = c.split(";")
    #         code_in_code_list = c_list[-2] + ";"
    #         index = self.code_list.index(code_in_code_list)
    #         new_code_in_code_list = code_in_code_list + "goto " + "L" + next_code_label + ";"
    #         self.code_list.insert(index, new_code_in_code_list)
    #         self.code_list.pop(index + 1)
    #         c = c + "goto " + "L" + next_code_label + ";"
    #         p[0].code_list[i] = c
    #
    #     for i in range(1, num_of_elseifs + 1):
    #         list = p[0].list[i]
    #         self.backpatch(list[0], self.get_start(p[0].code_list[i]))
    #         if i == num_of_elseifs:
    #             self.backpatch(list[1], self.get_start(p[0].code_list[-1]))
    #         else:
    #             self.backpatch(list[1], code)
    #
    #     print(self.code_list)
    #     self.produce_output()
    #     print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #
    # def p_if_4(self, p):
    #     """if : IF LP exp RP block elseifs ELSE block %prec prec1"""
    #     print("""if -> IF LP exp RP block elseifs ELSE block""")
    #     print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    #     p[0] = Nonterminal()
    #     p[0].list = []
    #     p[3].list = []
    #     p[3].list.append(p[3].true_list)
    #     p[3].list.append(p[3].false_list)
    #
    #     num_of_elseifs = len(p[6].list)
    #
    #     p[0].list = p[6].list
    #     p[0].list.insert(0, p[3].list)
    #     # print(p[0].list)
    #     p[0].code_list = p[6].code
    #     p[0].code_list.insert(0, p[5].code)
    #     p[0].code_list.insert(len(p[0].code_list), p[8].code)
    #     # print(p[0].code)
    #
    #     next_code_label = str(self.get_num_of_last_label(p[0].code_list[-1])+1)
    #     code = "L"+next_code_label+": "
    #     self.code_list.append(code)
    #
    #     if_list = p[0].list[0]
    #     self.backpatch(if_list[0], self.get_start(p[0].code_list[0]))
    #     self.backpatch(if_list[1], "L" + str(p[0].list[1][0][0]))
    #
    #     for i in range(1, num_of_elseifs+1):
    #         c = p[0].code_list[i]
    #         c_list = c.split(";")
    #         code_in_code_list = c_list[-2]+";"
    #         index = self.code_list.index(code_in_code_list)
    #         new_code_in_code_list = code_in_code_list + "goto " + "L" + next_code_label + ";"
    #         self.code_list.insert(index, new_code_in_code_list)
    #         self.code_list.pop(index+1)
    #         c = c + "goto " + "L" + next_code_label + ";"
    #         p[0].code_list[i] = c
    #
    #     for i in range(1, num_of_elseifs + 1):
    #         list = p[0].list[i]
    #         self.backpatch(list[0], self.get_start(p[0].code_list[i]))
    #         if i == num_of_elseifs:
    #             self.backpatch(list[1], self.get_start(p[0].code_list[-1]))
    #         else:
    #             self.backpatch(list[1], "L" + str(p[0].list[i + 1][0][0]))
    #
    #     print(self.code_list)
    #     self.produce_output()
    def p_if(self, p):
        r"""if : IF LP exp RP block elseif_blocks else_block"""
        print("""if : IF LP exp RP block elseif_blocks else_block""")

        p[3].code = p[3].ifexp if p[3].ifexp else p[3].code
        p[0] = Nonterminal()

        ####sym_table
        p[0].sym_var = p[5].sym_var + p[6].sym_var + p[7].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        self.symbol_table_list.append(p[0].sym_var)

        p[0].true = self.new_label()
        p[0].next = self.new_label()
        falselabel = None

        # back patch true block
        self.code_generator.back_patch_true(p[3], p[0].true)

        elseifblock = ""
        elseblock = ""

        elselabel = None
        # create label for else block and set next for it
        if p[7].code:
            elselabel = self.new_label()
            elseblock = elselabel + ": //else\n" + p[7].code

        elseiflabel = None
        # check if there is elseif block
        if p[6].code:
            elseiflabel = self.new_label()
            self.code_generator.back_patch_false(p[3], elseiflabel)
            falselabel = elseiflabel

            self.code_generator.back_patch_next(p[6], p[0].next)

            # check for else
            if p[7].code:
                self.code_generator.back_patch_false(p[6], elselabel)
            else:
                self.code_generator.back_patch_false(p[6], p[0].next)

            elseifblock = elseiflabel + ": //elseifs\n" + p[6].code
        # NO elseif check if there is else block
        elif p[7].code:
            self.code_generator.back_patch_false(p[3], elselabel)
            falselabel = elselabel
        # NO elseif NO else
        else:
            self.code_generator.back_patch_false(p[3], p[0].next)
            falselabel = None

        true_block = p[0].true + ": " + p[5].code + "goto " + p[0].next + "; //next label\n\n"

        false_block = ""
        if falselabel:
            false_block = elseifblock + elseblock

        next_block = p[0].next + ": //end of if statement - next\n"

        p[0].code = "// if statement\n//new\n" + p[3].code + true_block + false_block + next_block
        print("********************************************************************************************")
        print(p[0].code)
        print("********************************************************************************************")

    def p_elseif_blocks_1(self, p):
        r"""elseif_blocks : elseifs %prec PREC1"""
        print("""elseif_blocks : elseifs %prec PREC1""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_elseif_blocks_2(self, p):
        """elseif_blocks : """
        print("""elseif_blocks : """)
        p[0] = Nonterminal()
        p[0].code = None

    def p_elseifs_1(self, p):
        r"""elseifs : elseifs elseif %prec PREC1"""
        print("""elseifs : elseifs elseif %prec PREC1""")
        p[0] = Nonterminal()

        elseif_label = self.new_label()
        self.code_generator.back_patch_false(p[1], elseif_label)
        p[0].code = p[1].code + elseif_label + ": //elseif \n" + p[2].code + "\n"

        p[0].sym_var = p[1].sym_var + p[2].sym_var

    def p_elseifs_2(self, p):
        r"""elseifs : elseif %prec PREC2"""
        print("""elseifs : elseif %prec PREC2""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].sym_var = p[1].sym_var

    def p_elseif(self, p):
        r"""elseif : ELSEIF LP exp RP block %prec PREC2"""
        print("""elseif : ELSEIF LP exp RP block %prec PREC2""")
        p[0] = Nonterminal()

        truelabel = self.new_label()
        self.code_generator.back_patch_true(p[3], truelabel)
        p[0].code = p[3].code + truelabel + ": //elseif expression\n" + p[5].code + "goto " + self.NEXT_LABEL + "; // next label\n\n"

        p[0].sym_var = p[5].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        self.symbol_table_list.append(p[0].sym_var)

    def p_else_block_1(self, p):
        r"""else_block : ELSE block %prec PREC2"""
        print("""else_block : ELSE block %prec PREC2""")
        p[0] = Nonterminal()
        p[0].code = p[2].code + "\n"

        p[0].sym_var = p[2].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        self.symbol_table_list.append(p[0].sym_var)

    def p_else_block_2(self, p):
        r"""else_block : %prec PREC1"""
        print("""else_block : %prec PREC1""")
        p[0] = Nonterminal()
        p[0].code = ""



    # def p_elseifs_1(self, p):
    #     """elseifs : elseifs elseif"""
    #     print("""elseifs -> elseifs elseif""")
    #     p[0] = Nonterminal()
    #     p[0].code = p[1].code
    #     p[0].code.append(p[2].code)
    #     p[0].list = p[1].list
    #     p[0].list.append(p[2].list)
    #     # print(p[0].list)
    #     # print(p[0].code)
    #
    #
    #
    # def p_elseifs_2(self, p):
    #     """elseifs : elseif"""
    #     print("""elseifs -> elseif""")
    #     p[0] = Nonterminal()
    #     p[0].code = []
    #     p[0].code.append(p[1].code)
    #     p[0].list = []
    #     p[0].list.append(p[1].list)
    #     # print("))))))))))))))))))))))))))))))))))))))))))))))")
    #     # print(p[0].list)
    #     # print(p[0].code)
    #
    #
    #
    # def p_elseif(self, p):
    #     """elseif : ELSEIF LP exp RP block %prec ELSEIF"""
    #     print("""elseif -> ELSEIF LP exp RP block""")
    #     # print("true_list")
    #     # print(p[3].true_list)
    #     # print("false_list")
    #     # print(p[3].false_list)
    #     # print("code block")
    #     # print(p[5].code)
    #
    #     p[0] = Nonterminal()
    #     p[0].code = p[5].code
    #     p[0].list = []
    #     p[0].list.append(p[3].true_list)
    #     p[0].list.append(p[3].false_list)
    #     # print("****************************")
    #     # print(p[0].list)
    #
    #
    #     # p[0].pure_code_list



    def p_for(self, p):
        """for : FOR LP ID IN exp TO exp STEPS exp RP block"""
        print("""for -> FOR LP ID IN exp TO exp STEPS exp RP block""")
        p[0] = Nonterminal()

        p[0].sym_var = p[11].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        self.symbol_table_list.append(p[0].sym_var)


        begin = self.new_label()
        code_begin = self.new_label()
        after = self.new_label()

        initialization = "double " + p[3] + ";\n" + p[3] + " = " + p[5].get_value() + "; // FOR initialization\n"
        check_bundry = "if ( " + p[3] + " < " + p[7].get_value() + " ) goto " + code_begin + "; // FOR check\n"
        check_bundry += "goto " + after + ";\n\n"
        iteration = p[3] + " = " + p[3] + " + " + p[9].get_value() + "; // FOR iteration\n"
        p[0].code = "// FOR BEGIN\n\n" + p[5].code + p[9].code + initialization + begin + ": // for begin\n\n" + p[7].code + check_bundry + code_begin + ": // for code begin\n" + p[11].code + iteration + "goto " + begin + "; //back to for begin\n\n" + after + ": // end of for\n\n"
        print("*******************************************************************************")
        print(p[0].code)
        print("*******************************************************************************")


    def p_while(self, p):
        """while : WHILE LP exp RP block"""
        print("""while -> WHILE LP exp RP block""")

        p[0] = Nonterminal()

        p[0].sym_var = p[5].sym_var
        self.add_ref(p[0].sym_var, self.new_scope_name())
        self.symbol_table_list.append(p[0].sym_var)


        begin = self.new_label()
        code_begin = self.new_label()
        after = self.new_label()

        self.code_generator.back_patch_false(p[3], after)
        self.code_generator.back_patch_true(p[3], code_begin)
        p[0].code = begin + ": // while begin\n\n" + p[3].code + code_begin + ": // while code begin\n" + p[5].code + "goto " + begin + "; //back to while begin\n\n" + after + ": // end of while\n\n"

        print("*******************************************************************************")
        print(p[0].code)
        print("*******************************************************************************")
        # print(p[3].true_list)
        # print(p[3].false_list)
        # print(p[5].code)
        # self.backpatch(p[3].true_list, self.get_start(p[5].code))
        # next_code_label = str(self.get_num_of_last_label(p[5].code) + 1)
        # code = "L" + next_code_label + ": "
        # self.code_list.append(code)
        # self.backpatch(p[3].false_list, "L" + next_code_label)
        #
        #
        # c_list = p[5].code.split(";")
        # code_in_code_list = c_list[-2] + ";"
        # index = self.code_list.index(code_in_code_list)
        # new_code_in_code_list = code_in_code_list + "goto " + "L" + str(p[3].true_list[0]) + ";"
        # self.code_list.insert(index, new_code_in_code_list)
        # self.code_list.pop(index + 1)
        # p[5].code = p[5].code + "goto " + "L" + str(p[3].true_list[0]) + ";"
        #
        #
        #
        # print(self.code_list)
        # self.produce_output()

    def p_return(self, p):
        """return : RETURN exp SEMICOLON"""
        print("""return -> RETURN exp SEMICOLON""")
        p[0] = Nonterminal()
        p[0].code = "// push return value to stack\n" + p[2].code + CodeGenerator.popReturnAddr(self)
        p[0].code += CodeGenerator.pushVariable(self, p[2].get_value()) + "goto *returnAddress; // return from function\n\n"

    def p_break(self, p):
        """break : BREAK SEMICOLON"""
        print("""break -> BREAK SEMICOLON""")

    def p_continue(self, p):
        """continue : CONTINUE SEMICOLON"""
        print("""continue -> CONTINUE SEMICOLON""")

    #######4
    # fourth page
    def p_exp(self, p):
        """exp : INTEGER"""
        print("""exp -> INTEGER""")
        p[0] = Nonterminal()
        p[0].value = p[1]

    def p_exp_1(self, p):
        """exp : REAL"""
        p[0] = Nonterminal()
        p[0].value = p[1]
        print("""exp -> REAL""")

    def p_exp_2(self, p):
        """exp : TRUE"""
        p[0] = Nonterminal()
        p[0].value = p[1]
        print("""exp -> TRUE""")

    def p_exp_3(self, p):
        """exp : FALSE"""
        print("""exp -> FALSE""")
        p[0] = Nonterminal()
        p[0].value = p[1]

    def p_exp_4(self, p):
        """exp : STRING"""
        print("""exp -> STRING""")
        p[0] = Nonterminal()
        p[0].value = p[1]

    def p_exp_5(self, p):
        """exp : lvalue"""
        print("""exp -> lvalue""")
        p[0] = Nonterminal()
        p[0].place = p[1].place
        p[0].ifexp = "if ( " + p[1].place + " ) goto " + self.TRUE_LABEL + ";\n" + "goto " + self.FALSE_LABEL + ";\n\n"

    def p_exp_6(self, p):
        """exp : binary_operation %prec BIOP"""
        print("""exp -> binary_operation""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].place = p[1].get_value()

    def p_exp_7(self, p):
        """exp : logical_operation"""
        print("""exp -> logical_operation""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].place = p[1].get_value()

    def p_exp_8(self, p):
        """exp : comparison_operation %prec COMOP"""
        print("""exp -> comparison_operation""")
        p[0] = Nonterminal()
        p[0].code = p[1].code

    def p_exp_9(self, p):
        """exp : bitwise_operation %prec BITOP"""
        print("""exp -> bitwise_operation""")
        p[0] = Nonterminal()
        p[0].code = "NOT YET BITWISE"

    def p_exp_10(self, p):
        """exp : unary_operation"""
        print("""exp -> unary_operation""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].place = p[1].get_value()

    def p_exp_11(self, p):
        """exp : LP exp RP"""
        print("""exp -> LP exp RP""")
        p[0] = Nonterminal()
        p[0].place = p[2].place
        p[0].code = p[2].code

    def p_exp_12(self, p):
        """exp : function_call"""
        print("""exp -> function_call""")
        p[0] = Nonterminal()
        p[0] = p[1]
        p[0].code = p[1].code
        p[0].place = p[1].get_value()
        p[0].func = 1

    def p_binary_operation(self, p):
        """binary_operation : exp ADDITION exp """
        print("""binary_operation -> exp ADDITION exp """)
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_1(self, p):
        """binary_operation : exp SUBTRACTION exp"""
        print("""binary_operation -> exp SUBTRACTION exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_2(self, p):
        """binary_operation : exp MULTIPLICATION exp"""
        print("""binary_operation -> exp MULTIPLICATION exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_3(self, p):
        """binary_operation : exp DIVISION exp"""
        print("""binary_operation -> exp DIVISION exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_4(self, p):
        """binary_operation : exp MODULO exp"""
        print("""binary_operation -> exp MODULO exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_5(self, p):
        """binary_operation : exp POWER exp"""
        print("""binary_operation -> exp POWER exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_6(self, p):
        """binary_operation : exp SHIFT_LEFT exp"""
        print("""binary_operation -> exp SHIFT_LEFT exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_binary_operation_7(self, p):
        """binary_operation : exp SHIFT_RIGHT exp"""
        print("""binary_operation -> exp SHIFT_RIGHT exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_logical_operation(self, p):
        """logical_operation : exp AND exp"""
        print("""logical_operation -> exp AND exp""")
        p[0] = Nonterminal()

        true_label = self.new_label()
        self.code_generator.back_patch_true(p[1], true_label)
        p[0].code = p[1].code + true_label + ": // logical calculation (AND)\n" + p[3].code


    def p_logical_operation_1(self, p):
        """logical_operation : exp OR exp"""
        print("""logical_operation -> exp OR exp""")
        p[0] = Nonterminal()

        false_label = self.new_label()
        self.code_generator.back_patch_false(p[1], false_label)
        p[0].code = p[1].code + false_label + ": // logical calculation (OR)\n" + p[3].code

    #######5
    def p_comparison_operation_1(self, p):
        """comparison_operation : exp LT exp"""
        print("""comparison_operation -> exp LT exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)


    def p_comparison_operation_2(self, p):
        """comparison_operation : exp LE exp"""
        print("""comparison_operation -> exp LE exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)

    def p_comparison_operation_3(self, p):
        """comparison_operation : exp GT exp"""
        print("""comparison_operation -> exp GT exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)

    def p_comparison_operation_4(self, p):
        """comparison_operation : exp GE exp"""
        print("""comparison_operation -> exp GE exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)

    def p_comparison_operation_5(self, p):
        """comparison_operation : exp EQ exp"""
        print("""comparison_operation -> exp EQ exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)

    def p_comparison_operation_6(self, p):
        """comparison_operation : exp NE exp"""
        print("""comparison_operation -> exp NE exp""")
        p[0] = Nonterminal()
        self.code_generator.comparison_operation_code(p)

    def p_bitwise_operation_1(self, p):
        """bitwise_operation : exp BITWISE_AND exp"""
        print("""bitwise_operation -> exp BITWISE_AND exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_bitwise_operation_2(self, p):
        """bitwise_operation : exp BITWISE_OR exp"""
        print("""bitwise_operation -> exp BITWISE_OR exp""")
        p[0] = Nonterminal()
        self.code_generator.binary_operation_code(p, self.new_temp())

    def p_unary_operation_1(self, p):
        """unary_operation : SUBTRACTION exp %prec UMINUS"""
        print("""unary_operation -> SUBTRACTION exp""")
        p[0] = Nonterminal()
        self.code_generator.unary_operation_code(p, self.new_temp())

    def p_unary_operation_2(self, p):
        """unary_operation : NOT exp"""
        print("""unary_operation -> NOT exp""")
        p[0] = Nonterminal()
        self.code_generator.unary_operation_code(p, self.new_temp())

    def p_unary_operation_3(self, p):
        """unary_operation : BITWISE_NOT exp"""
        print("""unary_operation -> BITWISE_NOT exp""")
        p[0] = Nonterminal()
        self.code_generator.unary_operation_code(p, self.new_temp())

    def p_function_call_2(self, p):
        """function_call : lvalue2 function_call_body"""
        print("""function_call -> lvalue2 function_call_body""")

    def p_function_call_1(self, p):
        """function_call : lvalue1 function_call_body"""
        print("""function_call -> lvalue1 function_call_body""")
        p[0] = Nonterminal()
        label = self.new_label()
        p[0].args = p[2].args
        if self.t_counter > -1 :
            for i in range(0, self.t_counter):
                self.FuncVARIABLES.append("TT"+str(i))
        p[0].code = CodeGenerator.storeVariables(self, self.FuncVARIABLES) + CodeGenerator.pushAddress(self,label)
        p[0].code += "// store arguments\n" + p[2].code + CodeGenerator.storeArgs(self,p[2].args)+  "\n goto " + p[1].get_value() + ";\n"
        p[0].place = self.new_temp()
        p[0].code += "// return label:\n" + label + ":\n" + "// load return value\n" + CodeGenerator.popVariable(self,p[0].place) +"\n  //varaiables:" + CodeGenerator.loadVariables(self,self.FuncVARIABLES)
        print(p[0].code)
        print("-------------function call--------------")


    def p_function_call_body(self, p):
        """function_call_body : LP actual_arguments RP"""
        print("""function_call_body -> LP actual_arguments RP""")
        p[0] = Nonterminal()
        p[0] = p[2]

    def p_actual_arguments(self, p):
        """actual_arguments : actual_arguments_list"""
        print("""actual_arguments -> actual_arguments_list""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0]=p[1]


    def p_actual_arguments_e(self, p):
        """actual_arguments : """
        print("""actual_arguments ->/* Lambda */""")
        p[0] = Nonterminal()
        p[0].code = ""
        p[0].args = ""

    def p_actual_arguments_list_1(self, p):
        """actual_arguments_list : actual_arguments_list COMMA exp"""
        print("""actual_arguments_list -> actual_arguments_list COMMA exp""")
        p[0] = Nonterminal()
        p[0].code = p[1].code + p[3].code
        p[0].args = p[1].args
        p[0].args.append(p[3].get_value())

    def p_actual_arguments_list_2(self, p):
        """actual_arguments_list : exp"""
        print("""actual_arguments_list -> exp""")
        p[0] = Nonterminal()
        p[0].code = p[1].code
        p[0].args.append(p[1].get_value())


    precedence = (
        ('nonassoc', 'PREC2'),
        ('nonassoc', 'PREC1'),
        ('nonassoc', 'LVALI'),
        ('nonassoc', 'LVAL'),
        ('nonassoc', 'BIOP'),
        ('nonassoc', 'COMOP'),
        ('nonassoc', 'BITOP'),
        ('left', 'IF'),
        ('left', 'ELSE'),
        ('left', 'ELSEIF'),
        ('left', 'COMMA'),
        ('left', 'ASSIGNMENT'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'NOT'),
        ('left', 'BITWISE_OR'),
        ('left', 'BITWISE_AND'),
        ('left', 'BITWISE_NOT'),
        ('left', 'LE', 'EQ', 'NE', 'GE', 'GT', 'LT'),
        # ('left', 'SHIFT_LEFT', 'SHIFT_RIGHT'),
        ('left', 'ADDITION', 'SUBTRACTION'),
        ('left', 'MULTIPLICATION', 'DIVISION'),
        ('left', 'SHIFT_LEFT', 'SHIFT_RIGHT'),
        ('left', 'POWER'),
        ('left', 'MODULO'),
        ('left', 'UMINUS'),
        ('left', 'RP', 'LP'),
        # ('right', 'PREC3'),
        # ('right', 'PREC2'),
        # ('right', 'PREC1'),
        # ('right', 'ELSEIF')

    )


    def add_ref(self, list_dic, scope_name):
        for dic in list_dic:
            dic["ref"] = scope_name

    def new_scope_name(self):
        self.scope_counter += 1
        return "scope" + str(self.t_counter)

    def new_temp(self):
        self.t_counter += 1
        return "TT" + str(self.t_counter)

    def new_label(self):
        self.l_counter += 1
        return "L" + str(self.l_counter)

    def backpatch(self, in_list, m):
        # print("backpatch")
        # print(in_list)
        # print(m)
        for index in in_list:
            # print("in for")
            # print(index)
            # print(m)
            code = self.code_list[index]
            # print(code)
            new_code = code.replace("_", str(m))
            # print(code)
            self.code_list[index] = new_code

    def get_start(self, s):
        s_list = s.split(":")
        return s_list[0]
    def get_num_of_last_label(self, s):
        s_list = s.split(";")
        s_list = s_list[-2].split(':')
        num = int(s_list[0].replace("L",""))
        return num

    def produce_output(self):
        file = open("final_result.c", "w")
        s = "#include <stdio.h>"+"\n"
        s += "int main(){"+"\n"
        # if self.t_counter > -1 :
        #     s += "double "
        #     for i in range(0, self.t_counter+1):


        s += "\n".join(self.code_list)
        s += "\n" + "}"
        file.write(s)
        file.close()

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
