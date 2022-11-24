import argparse as ag

parser = ag.ArgumentParser(description='Parsing file js yang akan dicek syntaxnya.')
parser.add_argument(
    'file', help = 'File yang akan dicek syntaxnya', type = str)

args = parser.parse_args()
if (not args.file):
    print('File tidak ditemukan')
else:
    print(args.file)