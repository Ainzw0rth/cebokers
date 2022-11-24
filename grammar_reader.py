TERMINAL_SYMBOLS = [
    # Will be added later
]

VARIABLES = [
    # Will be added more later

]

START_SYMBOL = "START"


def cfg_from_file(filepath):
    # I.S. filepath adalah path ke file txt yang berisi CFG
    # F.S. Mengembalikan CFG dalam G = (V, X, R, S)
    #      V adalah set of variables/non-terminal symbols
    #      X adalah set of terminal symbols
    #      R adalah set of production rules
    #      S adalah start symbol
    
    # Persiapkan variabel yang akan digunakan
    V = VARIABLES
    X = TERMINAL_SYMBOLS
    R = {}
    S = START_SYMBOL 

    file = open(filepath, 'r')
    line = file.readline()
    while line != "@":
        if (line[0] != "#" and line != ""):
            production, rules = line.split(" -> ")
            rules = rules.replace("\n", "")
            if production not in R.keys():
                R[production] = [rules.split(" | ")]
            else:
                R[production].append(rules.split(" | "))
            
        line = file.readline()
    
    file.close()

    print("V = ", V)
    print("X = ", X)
    print("R = ", R)
    print("S = ", S)

    return (V, X, R, S)

cfg_from_file("grammar.txt")