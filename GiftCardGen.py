import random
from random import randint
from statistics import mode
import time
from pystyle import *
import os
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear"); os.system("title GiftCard Gen" if os.name == "nt" else "")
    txt = """                                                        
  /$$$$$$  /$$  /$$$$$$   /$$      /$$$$$$                            /$$        /$$$$$$                     
 /$$__  $$|__/ /$$__  $$ | $$     /$$__  $$                          | $$       /$$__  $$                    
| $$  \__/ /$$| $$  \__//$$$$$$  | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$      | $$  \__/  /$$$$$$  /$$$$$$$ 
| $$ /$$$$| $$| $$$$   |_  $$_/  | $$       |____  $$ /$$__  $$ /$$__  $$      | $$ /$$$$ /$$__  $$| $$__  $$
| $$|_  $$| $$| $$_/     | $$    | $$        /$$$$$$$| $$  \__/| $$  | $$      | $$|_  $$| $$$$$$$$| $$  \ $$
| $$  \ $$| $$| $$       | $$ /$$| $$    $$ /$$__  $$| $$      | $$  | $$      | $$  \ $$| $$_____/| $$  | $$
|  $$$$$$/| $$| $$       |  $$$$/|  $$$$$$/|  $$$$$$$| $$      |  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$
 \______/ |__/|__/        \___/   \______/  \_______/|__/       \_______/       \______/  \_______/|__/  |__/
                                                                                                             
                                                                                                             
                                                                                                             
    """
print(
    Colorate.Vertical(
        Colors.DynamicMIX((Col.light_blue, Col.purple)), Center.XCenter(txt)
    )
)       

gifttype = str(Write.Print("\nAmazon\nRoblox\nWebkinz\nFortnite\nIMVU\nEbay\nNetflix\niTunes\nPaypal\nVisa\nPokemonTGC\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n", Colors.blue_to_purple, interval=0.0001))


mode = str(Write.Input("\n\n           Giftcard type > ", Colors.yellow_to_red, interval=0.0001))

total = str(Write.Input("\n\n          Number of giftcard code  > ", Colors.yellow_to_red, interval=0.0001))

number = int(total)
file = (total + " GiftCards.txt")
file2 = 'GiftCardsCodes.txt'
#Minecraft
if(mode == "Minecraft"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
          out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Amazon
if(mode == "Amazon"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#iTunes
if(mode == "iTunes"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)

#Paypal
if(mode == "Paypal"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
#Playstation
if(mode == "Playstation"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)

#Steam
if(mode == "Steam"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+newline)

#Visa
if(mode == "Visa"):
    types = input("Card Or Prepaid Code? ")
    if(types == "Prepaid Code"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            generate16 = random.choice(gentype)
            newline = "\n"
            space = " "
            gen1 = random.choice(gentype)
            gen2 = random.choice(gentype)
            gen3 = random.choice(gentype)
            gen4 = random.choice(gentype)
            gen5 = random.choice(gentype)
            gen6 = random.choice(gentype)
        
        
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)
            with open(file2, 'a') as out2:
                out2.write(gen1+gen2+gen3+gen4+gen5+gen6+newline)
    elif(types == "Card"):
        gentype = '0123456789'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            generate16 = random.choice(gentype)
            newline = "\n"
            space = "|"
            month = "{:02d}".format(randint(1, 12))
            year = str(randint(2024,2027))
            slash = "|"
            space5 = "|"
            generate26 = random.choice(gentype)
            generate27 = random.choice(gentype)
            generate28 = random.choice(gentype)
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+space+month+slash+year+space5+generate26+generate27+generate27+newline)
    
#Xbox
if(mode == "Xbox"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        space3 = "-"
        generate16 = random.choice(gentype)
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        space4 = "-"
        generate21 = random.choice(gentype)
        generate22 = random.choice(gentype)
        generate23 = random.choice(gentype)
        generate24 = random.choice(gentype)
        generate25 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+generate15+space3+generate16+generate17+generate18+generate19+generate20+space4+generate21+generate22+generate23+generate24+generate25+newline)
#PlayStore
if(mode == "PlayStore"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        space3 = "-"
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space4 = "-"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+space3+generate13+generate14+generate15+generate16+space4+generate17+generate18+generate19+generate20+newline)
#PokemonTGC
if (mode == "PokemonTGC"):
    gentype = 'ABCDEFGHJHIKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        space2 = "-"
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space3 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+generate6+generate7+space2+generate8+generate9+generate10+space3+generate11+generate12+generate13+newline)
#Netflix
if(mode == "Netflix"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
#Ebay
if(mode == "Ebay"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
#Fortnite
if(mode == "Fortnite"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        space1 = "-"
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        space2 = "-"
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+space1+generate6+generate7+generate8+generate9+space2+generate10+generate11+generate12+generate13+newline)
#Roblox
if(mode == "Roblox"):
    gentype = '0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)

        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10+newline)
#Webkinz
if(mode == "Webkinz"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+newline)
#IMVU
if(mode == "IMVU"):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
print("Done ! all code are generated ;)")
time.sleep(5)
