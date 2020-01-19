from classes.nonterminal import Nonterminal

class CodeGenerator:
    def __init__(self):
        self.TRUE_LABEL = "TRUE_LABEL"
        self.FALSE_LABEL = "FALSE_LABEL"
        self.NEXT_LABEL = "NEXT_LABEL"

    def generate_arithmetic_code(self, p, tmp, code_list):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        p[0] = Nonterminal()
        p[0].place = tmp
        if len(p) == 4:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^4")
            arg1 = ""
            arg2 = ""

            if p[1].place == "":
                arg1 = p[1].value
            else:
                arg1 = p[1].place

            if p[3].place == "":
                arg2 = p[3].value
            else:
                arg2 = p[3].place

            p[0].code = "L" + str(len(code_list)) + ": " + p[0].place + "=" + arg1 + p[2] + arg2 + ";"
            print(p[0].code)
            code_list.append(p[0].code)
            print(code_list)

        elif len(p) == 3:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^3")
            arg1 = ""
            arg2 = ""

            if p[2].place == "":
                arg1 = p[2].value
            else:
                arg1 = p[2].place

            p[0].code = "L" + str(len(code_list)) + ": " + p[0].place + "=" + p[1] + arg1 + ";"
            print(p[0].code)
            code_list.append(p[0].code)
            print(code_list)

    def generate_boolean_code(self, p, code_list):
        p[0] = Nonterminal()
        next_quad = len(code_list)
        p[0].true_list = [next_quad]
        p[0].false_list = [next_quad + 1]

        if p[1].place != "" and p[3].place != "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].place + p[2] + p[3].place + " goto _" + ";"
        elif p[1].place != "" and p[3].place == "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].place + p[2] + p[3].value + " goto _" + ";"
        elif p[1].place == "" and p[3].place != "":
            code = "L" + str(next_quad) + ": " + "if " + p[1].value + p[2] + p[3].place + " goto _" + ";"
        else:
            code = "L" + str(next_quad) + ": " + "if " + p[1].value + p[2] + p[3].value + " goto _" + ";"

        code_list.append(code)

        code = "L" + str(next_quad + 1) + ": " + 'goto _' + ";"
        code_list.append(code)

        p[0].m = next_quad + 2
        p[0].code = code_list
        p[0].type = "bool"

        print("comparison_operation -> exp "+p[2]+" exp")
        print(code_list)

    def binary_operation_code(self, p, tmp):
        # reg = Register('double')

        # p[0].place = reg.place
        p[0].place = tmp
        p[0].code = p[1].code + p[3].code + p[0].place + " = " + p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";\n"

    def unary_operation_code(self, p, tmp):
        # reg = Register('double')
        # p[0].place = reg.place
        p[0].place = tmp
        p[0].code = p[2].code + p[0].place + " = " + p[1] + p[2].get_value() + ";\n"
        print("...**__", id(p[0]))

    def comparison_operation_code(self, p):
        p[0].code = p[1].code + p[3].code + "if(" + p[1].get_value() + p[2] + p[3].get_value() + ") goto " + self.TRUE_LABEL + ";\n" + "goto " + self.FALSE_LABEL + ";\n\n"

    def back_patch_true(self, exp, true_label):
        exp.code = exp.code.replace(self.TRUE_LABEL, true_label)

    def back_patch_false(self, exp, false_label):
        exp.code = exp.code.replace(self.FALSE_LABEL, false_label)

    def back_patch_next(self, exp, next_label):
        exp.code = exp.code.replace(self.NEXT_LABEL, next_label)


    #function

    def pushVariable(self, variable):
        code_list = "top = top - 1; // push " + variable + "\n"
        code_list += "*top = " + variable + ";\n\n"
        return code_list

    def popVariable(self, variable):
        code_list = variable + " = *top; // pop " + variable + "\n"
        code_list += "top = top + 1;\n"
        return code_list

    def pushAddress(self, label):
        code_list = "labelsTop = labelsTop - 1; // push address{" + label + "}\n"
        code_list += "*labelsTop = &&" + label + ";\n\n"
        return code_list

    def storeVariables(self, variables):
        code_list = "\n"
        for variable in variables:
            code_list += CodeGenerator.pushVariable(self, variable)
        return code_list

    def storeArgs(self, args):
        code_list = "\n"
        for arg in (args):
            code_list += CodeGenerator.pushVariable(self, arg)
        code_list += "\n"
        return code_list

    def loadVariables(self, variables):
        code_list = "\n"
        for variable in reversed(variables):
            code_list += CodeGenerator.popVariable(self, variable) + "\n"
        code_list += "\n"
        return code_list

    def popReturnAddr(self):
        code = "returnAddress = *labelsTop; // pop return address\n"
        code += "labelsTop = labelsTop + 1;\n\n"
        return code





