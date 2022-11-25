# This is the example of input CNF
NULL = None

V = ('S', 'X', 'Y')
X = ('a', 'b')
R = {
    'S': [['A','B'], ['B', 'C']],
    'A': [['B','A'], ['a']],
    'B': [['b'], ['C','C']],
    'C': [['a'], ['A','B']]
}
S = "S"

CNF_example = (V, X, R, S)

def print_table(table):
    # I.S. table adalah tabel CYK
    # F.S. Menampilkan tabel CYK
    i = len(table) - 1
    for row in table[::-1]:
        print(row[:len(row)-i])
        i -= 1

def CYK(CNF, input):
    # I.S. CNF adalah CFG dalam bentuk CNF
    #      input adalah string yang akan diuji
    # F.S. Mengembalikan True jika input dapat dihasilkan oleh CNF
    #      Mengembalikan False jika input tidak dapat dihasilkan oleh CNF

    # Main Reference: https://www.youtube.com/watch?v=VTH1k-xiswM
    
    w_length = len(input)
    R = CNF[2]
    # Inisialisasi tabel CYK
    table = [[[] for j in range(w_length)] for i in range(w_length)]

    # Isi tabel CYK
    for i in range(1, w_length + 1):  # Iterasi untuk length 1 sampai (w_length)
        # Proses untuk baris pertama, yaitu baris yang memiliki length 1
        if i == 1:
            for j in range(w_length):
                # Cari production rule yang memiliki terminal symbol yang sama dengan input
                for prod, rules in R.items():
                    for rule in rules:
                        # Jika terminal symbol sama, masukkan prod ke tabel
                        if rule[0] == input[j]:
                            table[i - 1][j].append(prod)

        # Untuk baris selanjutnya, proses dapat dilakukan dengan mengambil kombinasi dari baris sebelumnya
        else:
            # Cari semua kombinasi (m, n) dari yang mungkin untuk string dengan length i 
            combination = decompose_combination(i)
            for j in range(w_length - i + 1):
                for m, n in combination:
                    # Cari semua kombinasi dari baris sebelumnya dengan cartesian product
                    possible_constructor = cartesian_product(table[m - 1][j], table[n - 1][j + m])
                    # Cari production rule yang memiliki kombinasi yang sama dengan cartesian product
                    for prod, rules in R.items():
                        for rule in rules:
                            # Jika kombinasi sama, masukkan prod ke tabel
                            if rule in possible_constructor and prod not in table[i - 1][j]:
                                table[i - 1][j].append(prod)
    
    # Cek apakah Start Symbol ada di tabel CYK paling atas
    if CNF[3] in table[w_length - 1][0]:
        return True
    else:
        return False

def decompose_combination(i):
    # I.S. i adalah integer
    # F.S. Mengembalikan list of tuple yang merupakan kombinasi dari i
    #      Contoh: i = 3
    #              return [(1, 2), (2, 1)]

    # Inisialisasi list of tuple
    combinations = []
    for j in range(1, i):
        combinations.append((j, i - j))
    return combinations

def cartesian_product(l1, l2):
    # I.S. l1 dan l2 adalah list
    # F.S. Mengembalikan hasil perkalian kartesius dari l1 dan l2

    # Inisialisasi hasil
    result = []
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    for e1 in l1:
        for e2 in l2:
            result.append([e1, e2])
    return result

# print(cartesian_product(['A','C'], []))
print(CYK(CNF_example, "baaba"))