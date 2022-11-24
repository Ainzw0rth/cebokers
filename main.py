# The entry point for javascript parsing
import argparse as ag
import os
from cyk import CYK

def parseFile(filename):
    file = open(filename, 'r')
    input_string = file.read()

    file.close()

    # # TODO: Get The CNF
    # CNF = None

    # # TODO: Check the javascript syntax with CYK
    # CYK(CNF, input_string)

    # print(input_string) 

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
            