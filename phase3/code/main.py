from classes.lexer import Lexer
from classes.parser_test import Parser

filer = open("zosoist", "r")                      #15,3,35

text_input = filer.read()
filer.close()

lexer = Lexer().build()
parser = Parser()
parser.build().parse(text_input, lexer, False)
