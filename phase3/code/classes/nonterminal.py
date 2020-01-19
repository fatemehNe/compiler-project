
class Nonterminal:
    def __init__(self):
        self.id = ""
        self.place = "EMPTY"
        self.type = ""
        self.dic = {}
        self.value = ""
        self.code = ""
        self.label = ""
        self.true_list = []
        self.false_list = []
        self.m = None
        self.quad = 100000000000
        self.next_list = []
        self.address = 0
        self.pure_code_list = []
        self.list = []
        self.ifexp = None
        self.args = []
        self.vars = []
        self.func = 0
        self.func_name = ""
        self.sym_var = []
        self.sym_rtype = ""



    def get_value(self):
        if self.place == "EMPTY":
            return str(self.value)
        return str(self.place)

    #Object in python
