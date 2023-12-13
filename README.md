# Generátor Lorem Ipsum
## Latinská verze
Tato verze generuje text složený z náhodně uspořádaných latinských slov. Uživatel má možnost si zvolit rozmezí, v jakém má být počet slov ve větě, a také zvolit počet vět. Výstup se zapíše do souboru output.txt, který se okamžitě otevře v Poznámkovém bloku.   
Uživatel může přidávat další slova, ze kterých bude vybíráno. Slova se ukládají do souboru words.txt na jediný řádek oddělena mezerou. Slova mohou být uspořádaná v libovolně dlouhém textu, ve kterém nejsou odstavce ani interpunkční známénka s výjimkou čárky a tečky.  
<br>
Do Latinské verze patří tyto soubory:   
- lorem_ipsum.py
- words.txt (slouží k ukládání slovíček)
- output.txt (soubor, do kterého se zapíše výstup kódu)   
<br>
## Anglická verze
Tato verze generuje náhodný text v angličtině z existujících slov uložených v souboru words.txt. V rámci něj jsou uspořádány dle druhu, jak je popsáno v komentáři u .py souboru. Kód skládá věty dle předdefinovaných variant skladby vět. Některé věty mohou být takto správně, byť s nesmyslným významem.   
Uživatel má možnost přidávat další slovíčka. Musí dodržovat zvolený styl věty, kterou bude zapisovat, aby generátor správně slovíčka rozřadil podle typu. <b>Přidávejte pouze podstatná jména, přídavná jména, příslovce a slovesa.</b>   
Generátor je schopný ve velké části případů rozlišit, zdali má použít tvar slovesa pro třetí osobu.  
Nakonec kód výsledek zapíše do souboru .html, který otevře v prohlížeči. Text je v něm uspořádaný do sloupce o šířce 750px.   
<br>
Do Anglické verze patří tyto soubory:
- loremips_english.py
- words_english.txt (slouží k ukládání slovíček, rozdělena do řádků dle typu slova)
- output.html (HTML soubor, do kterého se zapíše výstup generátoru)
