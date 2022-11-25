from FA import isVariable
from grammar_processing import is_terminal

def CFG_to_CNF(CFG):
    # buat start state yang baru
    listKey = list(CFG.keys())
    listvalue = list(CFG.values())
    # asumsi start state dituliskan paling awal di grammar
    startStateAwal = listKey[0]
    adaStartStateAwal = False

    for rules in listvalue:
        for rule in rules:
            if startStateAwal in rule:
                adaStartStateAwal = True
    
    # tambahkan start state baru jika terdapat pengulangan state awal
    if adaStartStateAwal:
        startStateBaru = {"STARTSTATE" : [[startStateAwal]]}
        startStateBaru.update(CFG)
        CFG = startStateBaru

    # hapus unit production
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
                if len(ruleSatuElemen) == 1:
                    CFG[keySatuElemen].remove(ruleSatuElemen)

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
                # misalkan rule baru tersebut simbolnya Zi
                ruleTambahan = f"Z{i}"
                #
                if key not in RulesBaru.keys():
                    RulesBaru[key] = [[temp_rule[0], ruleTambahan]]
                else:
                    RulesBaru[key].append([temp_rule[0], ruleTambahan])
                temp_rule.remove(temp_rule[0])
                i += 1

            if ruleTambahan not in RulesBaru.keys():
                RulesBaru[ruleTambahan] = [temp_rule]
            else:
                RulesBaru[ruleTambahan].append(temp_rule)
            
            if ruleTambahan not in RulesLama.keys():
                RulesLama[ruleTambahan] = [rule]
            else:
                RulesLama[ruleTambahan].append(rule)

    for new_key, new_value in RulesBaru.items():
        if new_key not in CFG.keys():
            CFG[new_key] = new_value
        else:
            CFG[new_key].extend(new_value)

    for del_key, del_value in RulesLama.items():
        for del_rule in del_value:
            CFG[del_key].remove(del_rule)

    # STEP 4: Replace Terminal adjacent to a Variables
    RulesBaru = {}
    RulesLama = {}

    j = 0
    k = 0
    for key, value in CFG.items():
        for rule in value:
            if len(rule) == 2 and is_terminal(rule[0]) and is_terminal(rule[1]):
                ruleTambahanY = f"X{j}"
                ruleTambahanZ = f"Y{k}"

                if key not in RulesBaru.keys():
                    RulesBaru[key] = [[ruleTambahanY, ruleTambahanZ]]
                else:
                    RulesBaru[key].append([ruleTambahanY, ruleTambahanZ])
                    
                RulesBaru[ruleTambahanY] = [[rule[0]]]
                RulesBaru[ruleTambahanZ] = [[rule[1]]]

                if key not in RulesLama.keys():
                    RulesLama[key] = [rule]
                else:
                    RulesLama[key].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and is_terminal(rule[0]):
                ruleTambahanY = f"X{j}"

                if key not in RulesBaru.keys():
                    RulesBaru[key] = [[ruleTambahanY, rule[1]]]
                else:
                    RulesBaru[key].append([ruleTambahanY, rule[1]])

                RulesBaru[ruleTambahanY] = [[rule[0]]]

                if key not in RulesLama.keys():
                    RulesLama[key] = [rule]
                else:
                    RulesLama[key].append(rule)

                j += 1

            elif len(rule) == 2 and is_terminal(rule[1]):
                ruleTambahanZ = f"Y{k}"

                if key not in RulesBaru.keys():
                    RulesBaru[key] = [[rule[0], ruleTambahanZ]]
                else:
                    RulesBaru[key].append([rule[0], ruleTambahanZ])

                RulesBaru[ruleTambahanZ] = [[rule[1]]]

                if key not in RulesLama.keys():
                    RulesLama[key] = [rule]
                else:
                    RulesLama[key].append(rule)

                k += 1

            else:
                pass

    for new_key, new_value in RulesBaru.items():
        if new_key not in CFG.keys():
            CFG[new_key] = new_value
        else:
            CFG[new_key].extend(new_value)

    for del_key, del_value in RulesLama.items():
        for del_rule in del_value:
            CFG[del_key].remove(del_rule)

    return CFG