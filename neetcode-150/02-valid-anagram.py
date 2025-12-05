s = "ab"
t = "a"

def isAnagram(s: str, t: str) -> bool:
    listS = list(s) # ["r","a","c","e","c","a","r"]
    listT = list(t)
    # hashS = [{'char': 'r', 'count': 1}, {'char': 'a', 'count': 1}]
    hashS = [] # {r},{a},{c},{e}
    hashT = [] # {c},{a},{r},{e},
    equal = False

    for char in listS:
        match = False
        # print(f'Char {char}')
        if hashS != []:
            # print(f'   {hashS}')
            for hash in hashS:
                # for key, val in hash.items():
                # print(f'   checking {char} with {hash["char"]}')
                if hash["char"] == char:
                    match = True
                    hash["count"] += 1
                    # print(f'  > hash char {hash["char"]} is equal with {char}, count + 1')
                    # print(f'   {match}')
                    break
            if match == False:
                # print('  > buat baru')
                new = {'char': char, 'count': 1}
                hashS.append(new)
        else:
            # print('   Hash kosong, mari kita isi')
            new = {'char': char, 'count': 1}
            hashS.append(new)
            # print(f'   {hashS}')

    for char in listT:
        match = False
        # print(f'Char {char}')
        if hashT != []:
            # print(f'   {hashT}')
            for hash in hashT:
                # for key, val in hash.items():
                # print(f'   checking {char} with {hash["char"]}')
                if hash["char"] == char:
                    match = True
                    hash["count"] += 1
                    # print(f'  > hash char {hash["char"]} is equal with {char}, count + 1')
                    # print(f'   {match}')
                    break
            if match == False:
                # print('  > buat baru')
                new = {'char': char, 'count': 1}
                hashT.append(new)
        else:
            # print('   Hash kosong, mari kita isi')
            new = {'char': char, 'count': 1}
            hashT.append(new)
            # print(f'   {hashT}')

    if hashS != []:
        if hashT != []:
            # {r},{a},{c},{e}
            eq = False
            for dictS in hashS:
                # {c},{a},{r},{e},
                for dictT in hashT:
                    print(f'checking {dictS["char"]} with {dictT["char"]}')
                    if dictS["char"] == dictT["char"]:
                        # founded the same char
                        if dictS["count"] == dictT["count"]:
                            eq = True
                            # has the same value
                            print(f'equal {eq}')
                            break # stop the 2nd list loop
                        else:
                            eq = False
                            print(f'equal {eq}')
                            # print("diff val")
                            # different value
                            # equal = False
                            break
                    else:
                        eq = False
                if eq == False:
                    print("Found false stop!!")
                    break
            equal = eq
        
        if equal != False: # True
            if hashT != []:
                if hashS != []:
                    # {r},{a},{c},{e}
                    eq = False
                    for dictT in hashT:
                        # {c},{a},{r},{e},
                        for dictS in hashS:
                            # print(f'checking {dictS["char"]} with {dictT["char"]}')
                            if dictS["char"] == dictT["char"]:
                                # founded the same char
                                if dictS["count"] == dictT["count"]:
                                    eq = True
                                    # has the same value
                                    # print(f'equal {eq}')
                                    break # stop the 2nd list loop
                                else:
                                    eq = False
                                    # print(f'equal {eq}')
                                    print("diff val")
                                    # different value
                                    # equal = False
                                    break
                            else:
                                eq = False
                        if eq == False:
                            # print("Found false stop!!")
                            break
                    equal = eq

    return equal

print(isAnagram(s,t))

# test = [{"char": "r","count": 1},{"char": "r","count": 1}]
# print(type(test[0]))