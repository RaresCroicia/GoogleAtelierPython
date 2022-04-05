cuvant = 'alfabet'
cuvant_ascuns = []

for i in cuvant:
    #print(cuvant[0], cuvant[-1])
    if cuvant[0] != i and cuvant[-1] != i:
        cuvant_ascuns.append('_')
    else:
        cuvant_ascuns.append(i)

print(" ".join(cuvant_ascuns))
set_litere_incercate = set()
set_litere_incercate.add(cuvant[0])
set_litere_incercate.add(cuvant[-1])

count_nr = 1
while count_nr <= len(cuvant):
    user_letter = input("Alege o litera: ")
    if user_letter in set_litere_incercate:
        print("Ai ales deja litera asta")
        continue
    if user_letter == "":
        print("Introdu o litera")
        continue
    if user_letter in cuvant:
        for iterator, value in enumerate(cuvant):
            if cuvant[iterator] == user_letter:
                cuvant_ascuns[iterator] = user_letter
        print(" ".join(cuvant_ascuns))
    else:
        count_nr += 1
    set_litere_incercate.add(user_letter)
    if '_' not in cuvant_ascuns:
        print("Bravo!")
        break
    elif count_nr > len(cuvant):
        print(f"Ai pierdut! Cuvantul era {cuvant}")
        break