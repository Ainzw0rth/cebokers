from FA import isVariable
from yangngecekterminal import is_terminal

# referensi : https://www.youtube.com/watch?v=7G0PwGrdlH8&ab_channel=Education4u

def CFG_to_CNF(CFG):
    # STEP 1 : BUAT STARTSTATE YANG BARU
    listKey = list(CFG.keys())
    # asumsi start state awal dituliskan paling awal di grammar
    startStateAwal = listKey[0]
    
    # tambahkan STARTSTATE ke CFG
    startStateBaru = {"STARTSTATE" : [[startStateAwal]]}
    startStateBaru.update(CFG)
    CFG = startStateBaru

    # STEP 2 : JADIKAN SEBAGAI NORMAL FORM
    ada = True

    # looping untuk menyederhanakan grammar
    while ada:
        satuElemen = {}
        ada = False                    # boolean sebagai penanda bahwa ada minimal satu rule pada grammar yang valuenya dikanan terdiri dari satu elemen saja
        
        # sederhanakan jika grammar hanya terdiri dari satu elemen
        for key, value in CFG.items():
            for rule in value:
                if len(rule) == 1 and isVariable(rule[0]):
                    ada = True
                    if key not in satuElemen.keys():
                        satuElemen[key] = [[rule[0]]]
                    else:
                        satuElemen[key].append([rule[0]])

        # substitusikan grammar yang singular ke rules lain yang memiliki rules singular tersebut
        for key, value in CFG.items():
            for keySatuElemen, valueSatuElemen in satuElemen.items():
                for ruleSatuElemen in valueSatuElemen:
                    # substitusikan
                    if len(ruleSatuElemen) == 1 and key == ruleSatuElemen[0]:
                        if keySatuElemen not in CFG.keys():
                            CFG[keySatuElemen] = value
                        else:
                            for rule in value:
                                if rule not in CFG[keySatuElemen]:
                                    CFG[keySatuElemen].append(rule)

        # hapus grammar yang hanya terdiri dari satu elemen
        for keySatuElemen, valueSatuElemen in satuElemen.items():
            for ruleSatuElemen in valueSatuElemen:
                CFG[keySatuElemen].remove(ruleSatuElemen)


    # STEP 3 : SEDERHANAKAN RULES YANG PRODUKNYA TERDIRI DARI MINIMAL SATU TERMINAL DAN SISANYA ADALAH BUKAN TERMINAL
    RulesBaru = {}
    RulesLama = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            temp = []
            ada = False
            for r in rule:
                temp.append(r)

            for x in range(len(rule)):
                if is_terminal(rule[x]):
                    ada = True
                    simbolbaruX = f"X{i}"
                    i += 1
                    RulesBaru[simbolbaruX] = [[rule[x]]]
                    temp[x] = simbolbaruX

            if ada:
                if head not in RulesBaru.keys():
                    RulesBaru[head] = [temp]
                else:
                    RulesBaru[head].append(temp)
            else:
                pass

    for new_head, new_body in RulesBaru.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in RulesLama.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)
            
    # substitusi grammar yang memiliki lebih dari 2 elemen pada produk
    i = 0
    RulesBaru = {}
    RulesLama = {}

    for key, value in CFG.items():
        for rule in value:
            temp_rule = []
            for r in rule:
                temp_rule.append(r)

            # looping hingga rulenya pada bagian produk tidak lebih dari 2
            while len(temp_rule) > 2:
                # misalkan rule baru tersebut simbolnya Yi
                ruleTambahan = f"Y{i}"
                i += 1
                # simpan rules-rules baru agar nanti bisa ditambahkan
                if key not in RulesBaru.keys():
                    RulesBaru[key] = [[temp_rule[0], ruleTambahan]]
                else:
                    RulesBaru[key].append([temp_rule[0], ruleTambahan])
                temp_rule.remove(temp_rule[0])

            if ruleTambahan not in RulesBaru.keys():
                RulesBaru[ruleTambahan] = [temp_rule]
            else:
                RulesBaru[ruleTambahan].append(temp_rule)
            
            if ruleTambahan not in RulesLama.keys():
                RulesLama[ruleTambahan] = [rule]
            else:
                RulesLama[ruleTambahan].append(rule)

    # tambahkan rules baru ke CFG sesuai keynya
    for new_key, new_value in RulesBaru.items():
        if new_key not in CFG.keys():
            CFG[new_key] = new_value
        else:
            CFG[new_key].extend(new_value)

    # hapus dari CFG
    for del_key, del_value in RulesLama.items():
        for del_rule in del_value:
            CFG[del_key].remove(del_rule)

    return CFG