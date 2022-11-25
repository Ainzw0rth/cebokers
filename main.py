# The entry point for javascript parsing
import argparse as ag
import os
from CYK import CYK
from language import string_to_grammar
from FA import isOperasiValid, isVariable, isStringValid
from grammar_reader import cfg_from_file
from CFGtoCNF import CFG_to_CNF


def parseFile(filename):
    file = open(filename, 'r')
    input_string = file.read()

    file.close()

    input_string, expressions, variables = string_to_grammar(input_string)
    # print(expressions)
    # print(variables)
    
    # # CEK ALL EXPRESSIONS VALIDITY
    # expressionValid = True
    # i = 0
    # while expressionValid and i < len(expressions):
    #     expressionValid = isOperasiValid(expressions[i])
    #     i += 1

    # print(expressionValid)

    # # CEK ALL VARIABLES VALIDITY
    # variableValid = True
    # i = 0
    # while variableValid and i < len(variables):
    #     variableValid = isVariable(variables[i])
    #     i += 1

    # # Get The CNF
    CFG = cfg_from_file("grammar.txt")
    CNF =  CFG_to_CNF(CFG)
    print(CNF)
    # CNF = (CFG[0], CFG[1], V, CFG[3])
    
    # isAccepted = CYK(input_string, CNF)
    # print(isAccepted)

    return

parser = ag.ArgumentParser(description='Parsing file javascript yang akan dicek syntaxnya.')
parser.add_argument(
    'file', help = 'File yang akan dicek syntaxnya', type = str)

args = parser.parse_args()
if (not args.file):
    print('File tidak ditemukan')
else:
    if (not os.path.exists(args.file)):
        print('File tidak ditemukan')
    else:
        if (not args.file.endswith('.js')):
            print('File yang di-parse bukan file javascript')
        else:
            parseFile(args.file)
            