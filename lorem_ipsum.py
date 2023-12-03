import os
import random

def words_list(w_r,wr_value="Fnew2/d8w2-8ed.",file_n="words.txt"):
    with open(file_n, w_r) as soubor:
        if (w_r == "w" or w_r == "a") and not wr_value == "Fnew2/d8w2-8ed.":
            soubor.write(wr_value)
        elif w_r == "r":
            wr_value = soubor.readline()
            soubor.close()
            return wr_value
        else:
            raise ValueError()
    soubor.close()
###################################
action = input("\nPřidat text do seznamu: přidat\nVygenerovat Lorem Ipsum text: generovat\n")

## texts adding
if action == "přidat":
    new_text = " "+input("Sem vložte nový text:\n")
    new_text = new_text.lower().replace(".","").replace(",","").replace("\n","")
    words_list("a",new_text)
    print("Přidali jste do seznamu slov tento text:",new_text)
elif action == "generovat":
    ## texts generating
    words = list(set(words_list("r").split()))
    output = ""
    sentence = "Lorem ipsum"
    words_range = input("Napište rozsah počtu slov v jedné větě. Např. '2-5' : ").replace("-"," ").split()
    words_range[0] = int(words_range[0])
    words_range[1] = int(words_range[1])
    if words_range[0]>words_range[1]:
        words_range.reverse()
    for _ in range(int(input("Kolik vět chceš napsat: "))):
        for word_index in range(random.randint(words_range[0],words_range[1])):
            if word_index == 0 and not sentence:
                sentence += " "+words[random.randint(0,len(words)-1)].capitalize()
            else:
                sentence += " "+words[random.randint(0,len(words)-1)]
        output += sentence + "."
        sentence = ""
    print("\n"+output+"\n")
    words_list("w",output,"output.txt")
    osCommandString = "notepad.exe output.txt"
    os.system(osCommandString)
    