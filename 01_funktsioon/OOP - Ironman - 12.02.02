# Ajalimiidid minutites
ujumise_limiit = 140
ratta_limiit = 490
jooksu_limiit = 390

#UJUMINE
ujumine_input = input("Sisesta oma ujumise aeg minutites: ")
while not ujumine_input.isdigit():
    print("Vale sisestus! Palun sisesta aeg minutites.")
    ujumine_input = input("Sisesta oma ujumise aeg minutites: ")
ujumine = int(ujumine_input)

if ujumine <= ujumise_limiit:

    #RATTASÕIT
    ratas_input = input("Sisesta oma rattasõidu aeg minutites: ")
    while not ratas_input.isdigit():
        print("Vale sisestus! Palun sisesta aeg minutites.")
        ratas_input = input("Sisesta oma rattasõidu aeg minutites: ")
    ratas = int(ratas_input)

    if ratas <= ratta_limiit:

        #JOOKS
        jooks_input = input("Sisesta oma jooksu aeg minutites: ")
        while not jooks_input.isdigit():
            print("Vale sisestus! Palun sisesta aeg minutites.")
            jooks_input = input("Sisesta oma jooksu aeg minutites: ")
        jooks = int(jooks_input)

        if jooks <= jooksu_limiit:

            #KOGU AEG
            kogu_aeg = ujumine + ratas + jooks
            tunnid = kogu_aeg // 60
            minutid = kogu_aeg % 60

            print("Jäid ilusti aja sisse!")
            print("Sinu kogu aeg oli", tunnid, "tundi ja", minutid, "minutit.")
            print("Palju õnne! Oled Ironman!")

        else:
            print("Seekord jooksu ajalimiiti ei jõudnud. Järgmine aasta jõuad kindlasti!")

    else:
        print("Seekord ratta ajalimiiti ei jõudnud. Järgmine aasta jõuad kindlasti!")

else:
    print("Seekord ujumise ajalimiiti ei jõudnud. Järgmine aasta jõuad kindlasti!")
