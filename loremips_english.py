import random, webbrowser

def words_list(w_r,wr_value="Fnew2/d8w2-8ed.",file_n="words_english.txt"):
    with open(file_n, w_r) as soubor:
        if (w_r == "w" or w_r == "a") and not wr_value == "Fnew2/d8w2-8ed.":
            soubor.writelines(wr_value)
        elif w_r == "r":
            wr_value = soubor.readlines()
            soubor.close()
            return wr_value
        else:
            raise ValueError()
    soubor.close()
########################################
mode = input("Vyber, co chceš dělat: x-konec, 0-přidávat slova, 1-tvořit nové větné skladby, 2-generovat ")
## Definice větné skladby
words_order = [(0,1,0),(4,1,0),(6,0,1,0),(4,5,1),(4,1,2),(6,0,5,1,2)]
# 0 - noun, 1 - verb, 2 - adverb, 3 - adjective, 4 - pronoun, 5 - verbs with preposition, 6 - possesive pronoun
words_num = (1,1,1,1,2,1,2)
# this also an order of lines in the file 'words_english.txt'
while not mode == "x":

    # 0-přidávat slova
    if mode == "0":
        order_pattern = words_order[int(input(f"\nVyberte typ větné skladby, ve které budete psát věty.\n{words_order}\nLegenda: 0 - noun, 1 - verb, 3 - proverb, 4 - adjective, 5 - to be + noun/adjective/possesive pronoun, 6 - pronoun, 7 - způsobová slovesa\n"))]
        print("\n",order_pattern)
        new_sentence = input("Napište větu ve tvaru: "+str(order_pattern)+": ").lower().replace(".","").split()
        print(new_sentence)
        for article in ("an","a","the"):
            if article in new_sentence:
                new_sentence.remove(article)
        print(words_order)
        print(new_sentence)

        file_content = words_list("r")
        print(file_content)
        for ind in range(len(order_pattern)):
            file_content[order_pattern[ind]] = new_sentence[ind] +" "+ file_content[order_pattern[ind]]
        print(file_content)
        
        words_list("w",file_content)
    elif mode == "2":
        file_content = words_list("r")
        for type in range(len(file_content)):
            if not type == 5:
                file_content[type] = file_content[type].split()
            else:
                file_content[type] = file_content[type].split(", ")
        # print(file_content)
        output = ""
        for _ in range(int(input("Napiš počet vět, který chceš napsat."))):
            sentence = ""
            person_3rd = False
            for type in random.choice(words_order):
                if person_3rd and type == 1:
                    sentence += random.choice(file_content[type]) + "s"
                    person_3rd = False
                else:
                    sentence += random.choice(file_content[type]) + ""
                if type == 0 or type == 4:
                    person_3rd = True
                    if sentence[sentence.rfind(" ")+1:].lower() in {"i","you","these","those","they","we"}:
                        person_3rd = False
                elif person_3rd and not type == 1:
                    person_3rd = False
                sentence += " "
            sentence = sentence.capitalize().removesuffix(" ")+". "
            print(sentence)
            output += sentence
        words_list("w","<style>p{width: 750px;}</style>\n"+"<h2>Výsledek:</h2>\n<p>"+output.removesuffix(" ")+"</p>","output.html")
        webbrowser.open(r".\output.html")
        break
    mode = input("Vyber, co chceš dělat: x-konec, 0-přidávat slova, 1-tvořit nové větné skladby, 2-generovat ")
