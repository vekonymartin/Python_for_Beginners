# region Boolean values
inGame   = True # Benne vagyunk vagy nem
lion_eat = False
win      = False
# endregion

# region Lists
rooms  = []
items = []
# endregion

# region Values
switches_value = "0000000"
code_solution  = "4686"
code_tip       = ""
chances        = 3
# endregion

print("""Üdvözöljük a menekülési szobám játékában. Egy szobában vagy, és 14 ajtó van körülötted.
Az egyik a szabadságod ajtaja. Keresse meg a megfelelőt, és írja be a négyjegyű jelszót.
A számjegyek a többi 13 ajtó mögött találhatók. Keresse meg a számjegyeket, és szabadítsa fel magát.""")

# ==================================================================
# region Game
while inGame:
    room_number = input("Melyik szobába akarsz bemenni (0-13)?\n")

    if room_number == "-1":
        print("Játékmeneted állapota:")
        for i in range(len(items)):
            print("Szobák: ", rooms[i], ": ",items[i])

    if room_number == "0":
        if "key" not in items:
            print("""Sötét szobát találtál. A fal mellett haladva kapcsolót keresel....
            Végül megtalálod és felkapcsolod a villanyt, majd rájössz, hogy a szoba üres.
            Észreveszel valamit a szoba közepén. Odamész és megnézed, majd rájössz, hogy egy kulcs az.
            Gyorsan zsebrevágod és elhagyod szobát.""")
            items.append("key")
            rooms.append(room_number)
            if "locked box" in items:
                print("Wait a minute. Már van lootbox-od!")
                print("Kinyitod a box-ot és látod, hogy van benne egy darab hús és ezért ezt azonnal\n"
                      "zsebrevágod.")
                items.append("raw meat")
                rooms.append(room_number)
        else:
            print("Már megtaláltad a kulcsot! :D")
    if room_number == "1":
        print("Látunk egy vreepy festmény, ezért jó gyerek módjára odamegyek és megnézem mi van mögötte,\n"
              "mert a horror filmekben ezt láttam.\n"
              "Észreveszem, hogy egy számkódot rejt a festmény hátulja.\n"
              "A kód: 00000100")
        items.append("00000100")
        rooms.append(room_number)
    else:
        print("Ezt a kódot már megtaláltuk!")
    if room_number == "2":
        if room_number not in rooms:
            print("Holy Shit! Ez egy nagy szisza! Körülnézek és nem tudok semmere se menni, pedig a \n"
                  "szisza mögött van a következő rejtvény!")
            items.append("Cuki oroszlán")
            rooms.append(room_number)
            lion = input("Mégis mi a tőcsömet akarsz most csinálni?!?!?! (kemény leszek/megsimogatom/itt hagyom a ...)")
            if lion == "kemény leszek":
                if "raw meat" not in items:
                    print("Hát megpróbáltam Chuck Norris lenni, de nem gyütt össze :(")
                    print("YOU DIED")
                    inGame = False
                    lion_eat = True
                else:
                    print("Hozzá vágtam a husimusit, szóval szabad az utam a kód felé! :D")
                    items.append("8")
                    rooms.append(room_number)
        else:
            print("Talán legközelebb! :(")
# endregion
# ==================================================================


