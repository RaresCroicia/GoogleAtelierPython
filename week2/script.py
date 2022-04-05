# print("mesaj")
# numar_mere = 2
# variabila_goala = None # None == NULL din c (kind of) - gen ii zic "ba, existi, dar esti degeaba"
#
# #integrarea variabilelor in string
#
# #varianta 1
# mesaj = f"Ana are {numar_mere} mere" #f inainte de string si variabila intre {}
# print(mesaj)
#
# #varianta 2
#
# mesaj = "Ana are {} mere".format(numar_mere) #practic va inlocui IN ORDINE variabilele in locul {}
# print(mesaj)
#
# #varianta 2.5
#
# mesaj = "Ana are {0} mere si {0} pere".format(numar_mere) #inlocuieste in {index} cu al index-lea din format
# print(mesaj)
#

# #liste
# lista = [] # lista vida
# lista.append('2')
# lista.append(3) #functie de append
# lista.append(4)
# lista.append('text')
#
# print(len(lista)) #len(lista) = lungime lista
# print(lista)
#
# print(lista[2:3]) #afiseaza incepand cu index = 2 si < 3
# print(lista[:3]) #afiseaza incepand cu index = 0 si < 3
# print(lista[:5]) #in sliclind "over bounding-ul" e rezolvat de python (nu afiseaza)
# #print(lista[5]) #out of bounds si eroare
#
# lista[0] = 'altceva' #da replace pe index 0
#
# #tupluri
#
# tuplu = (1, 7, -3, 'a') #se baga intre ()
#
# #dictionare
#
# dictionar = {"cheie1": 1, "cheie2": 2}
# print(dictionar["cheie1"]) #da eroare daca nu exista cheia in dictionar
# print(dictionar.get("cheie1")) #daca nu exista cheia, va arata None
#
# #ca sa adaugi alte elemente in dictionar / updatezi chestii
# dictionar["cheienoua"] = 'ceva'
# #sau
# dictionar.update({"cheie3": "3"})
# print(dictionar)

#seturi

# my_set = {"item1", 1, 2, 3} #imutabila si neaccesibila in index
# print(my_set)
# my_set1 = {"item2", 2, 3}
# my_final_set = my_set.union(my_set1)
# print(my_final_set)
#
#
# #if
#
# my_var = 5
# if my_var < 5:
#     print("mic")
# elif my_var > 5:
#     print("mare")
# else:
#     print("fix 5")
#
# # de mentionat, la quality testing else nu e placut, asa ca scapam de el
#
# mesaj = "fix 5"
# if my_var < 5:
#     mesaj = "mic"
# elif my_var > 5:
#     mesaj = "mare"
#
# print(mesaj)
#
# #while - cam clasic
#
# variabila_1 = 1
# while variabila_1 < 3:
#     print("ceva")
#     variabila_1 += 1


#for

#pentru stringuri
cuvant = "Ana are mere"
# for i in cuvant:
#     print(i)

# for i, value in enumerate(cuvant):
#     print(i, value)

for i in range(0, 10):
    print(i)
