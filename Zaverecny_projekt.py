import tkinter as tk
import random
import csv
import datetime

Okno = tk.Tk()
LNadpis = tk.Label()
LInstrukce1 = tk.Label()
LInstrukce2 = tk.Label()
LOdpocitavani = tk.Label()
LSlova = tk.Label()
LBody = tk.Label()
EVstup_odpoved = tk.Entry()
EVstup_jmeno = tk.Entry()
BNova_hra = tk.Button()
BKonec_hry = tk.Button()
LNejlepsi_vysledky = tk.Label()

Okno.title("VYZKOUŠEJ SVŮJ POSTŘEH!")
Okno.geometry("1400x700")
Okno.config(bg="lightgray")

LNadpis.config(bg="lightgray", text="Jakou barvu má...?", font=("Arial", 30, "bold"))
LNadpis.place(x=500, y=70)
LInstrukce1.config(bg="lightgray", text="V této hře bude prověřen váš zrak a postřeh!\nVaším úkolem je co nejrychleji vepsat do textového pole barvu zobrazeného textu (např, 'červenou' apod).\nOvšem pozor, pokud bude text zobrazen černě nebo bíle, musíte vepsat barvu, jakou má označovaný objekt ve skutečnosti!", font=("Arial", 18))
LInstrukce1.place(x=10, y=130)
LInstrukce2.config(bg="lightgray", text="Zadejte své jméno:", font=("Arial", 18))
LInstrukce2.place(x=20, y=20)

EVstup_jmeno.config(font=("Arial", 22))
EVstup_jmeno.place(x=20, y=55)
EVstup_jmeno.focus_set()

BNova_hra.place(x=100, y=570)
BNova_hra.place_forget()

BKonec_hry.config(text="Konec", command=Okno.destroy, font=("Arial", 20))
BKonec_hry.place(x=300, y=570)
BKonec_hry.place_forget()

LOdpocitavani.config(bg="lightgray", text="Zbývající čas: 40", font=("Arial", 16)) 
LOdpocitavani.place(x=100, y=300)
LSlova.config(bg="lightgray", font=("Arial", 52, "bold"))
LSlova.place(x=100, y=350)
LBody.config(bg="lightgray", text="Vaše skóre je: 0", font=("Arial", 16))
LBody.place(x=500, y=600)
EVstup_odpoved.config(font=("Arial", 42))
EVstup_odpoved.place(x=100, y=470)

LNejlepsi_vysledky.config(fg= "darkviolet", bg="lightgray", text="", font=("Arial", 16))
LNejlepsi_vysledky.place(x=900, y=470)

barva_slova_klic = ""
spravna_barva = ""
zbyvajici_cas = 40 
body = -1
jmeno_hrace = ""
datum = datetime.datetime.now().strftime("%Y-%m-%d")

slova = ["bělásek", "jahoda", "trávník", "citrón", "rubín", "slon", "pomeranč", "filmový panter", "lední medvěd", "havran", "kos", "trh, kde se obchoduje nelegálně", "zóna mezi zákonným a nezákonným", "rak", "žluťásek", "Shrek"]
barvy = {
    "red": "červenou", 
    "blue": "modrou", 
    "lime": "zelenou", 
    "hotpink": "růžovou", 
    "yellow": "žlutou", 
    "gray": "šedou", 
    "orange": "oranžovou", 
    "black": "černou", 
    "white": "bílou"}

barvy_s_cetnostmi = ["red", "lime", "blue", "hotpink", "yellow", "gray", "orange", "black", "black", "white", "white"]

def zacni_hru(event):
    global zbyvajici_cas, jmeno_hrace
    jmeno_hrace = EVstup_jmeno.get().strip()
    
    if jmeno_hrace:
        EVstup_odpoved.focus_set()
        if zbyvajici_cas == 40: 
            odpocitavej()
        zobraz_dalsi()

def odpocitavej():
    global zbyvajici_cas
    if zbyvajici_cas > 0:
        zbyvajici_cas -= 1
        LOdpocitavani.config(text="Zbývající čas: " + str(zbyvajici_cas))
        LOdpocitavani.after(1000, odpocitavej)
    else:
        zaznamenej_body()  

def zobraz_dalsi():
    global body, zbyvajici_cas, barva_slova_klic, spravna_barva
    LSlova.place(x=100, y=350)
    if zbyvajici_cas > 0:
        if EVstup_odpoved.get().lower() == spravna_barva.lower():
            body += 1
        elif EVstup_odpoved.get().lower() == "":
            pass
        else:
            body -= 1

        barva_slova_klic = random.choice(barvy_s_cetnostmi)
        slovo = random.choice(slova)
        if barva_slova_klic.lower() == "black" or barva_slova_klic.lower() == "white":
            if slovo == "bělásek": spravna_barva = "bílou"
            elif slovo == "jahoda": spravna_barva = "červenou"
            elif slovo == "trávník": spravna_barva = "zelenou"
            elif slovo == "citrón": spravna_barva = "žlutou"
            elif slovo == "rubín": spravna_barva = "červenou"
            elif slovo == "slon": spravna_barva = "šedou"
            elif slovo == "pomeranč": spravna_barva = "oranžovou"
            elif slovo == "filmový panter": spravna_barva = "růžovou"
            elif slovo == "lední medvěd": spravna_barva = "bílou"
            elif slovo == "havran": spravna_barva = "černou"
            elif slovo == "kos": spravna_barva = "černou"
            elif slovo == "trh, kde se obchoduje nelegálně": spravna_barva = "černou"
            elif slovo == "zóna mezi zákonným a nezákonným": spravna_barva = "šedou"
            elif slovo == "rak": spravna_barva = "červenou"
            elif slovo == "žluťásek": spravna_barva = "žlutou"
            elif slovo == "Shrek": spravna_barva = "zelenou"
        
        else:
            spravna_barva = barvy[barva_slova_klic]

        LSlova.config(fg=barva_slova_klic, text=slovo)
        LBody.config(text="Vaše skóre je: " + str(body))

    EVstup_odpoved.delete(0, tk.END)
        
def zaznamenej_body():
    global body, jmeno_hrace
    with open("vysledky.csv", "a", newline="", encoding="ansi") as vysledky_otevrene:
        zapis_vysledku_do_csv = csv.writer(vysledky_otevrene)
        zapis_vysledku_do_csv.writerow([jmeno_hrace, body, datum])
    LBody.config(fg= "darkviolet", text=f"Čas vypršel!\nVaše skóre je: {body}\nVýsledky byly uloženy!")
    zobraz_Nejlepsi_vysledky()
    BNova_hra.place(x=100, y=600)
    BKonec_hry.place(x=300, y=600)

def zobraz_Nejlepsi_vysledky():
    try:
        with open("vysledky.csv", "r", encoding="ansi") as vysledky_otevrene:
            nacteni_vysledku_z_csv = csv.reader(vysledky_otevrene)
            top3_vysledky = sorted(nacteni_vysledku_z_csv, key=lambda x: int(x[1]), reverse=True)[:3]
            text = "Nejlepší výsledky:\n"
            for index, (jmeno, body, _) in enumerate(top3_vysledky):
                text += f"{index + 1}. {jmeno}, počet bodů: {body}\n"
            LNejlepsi_vysledky.config(text=text)
    except FileNotFoundError:
        LNejlepsi_vysledky.config(text="Žádné výsledky zatím nejsou.")

EVstup_odpoved.delete(0, tk.END)        

Okno.bind("<Return>", zacni_hru)

def resetuj_hru():
    global body, zbyvajici_cas, jmeno_hrace
    LSlova.place_forget()
    body = 0
    zbyvajici_cas = 40
    jmeno_hrace = ""
    EVstup_jmeno.focus_set()
    EVstup_jmeno.delete(0, tk.END)
    EVstup_odpoved.delete(0, tk.END)
    LOdpocitavani.config(text="Zbývající čas: 40")
    LBody.config(text="Vaše skóre je: 0")
    BNova_hra.place_forget()
    BKonec_hry.place_forget()
    zacni_hru(None)

BNova_hra.config(text="Nová hra", command=resetuj_hru, font=("Arial", 20))

Okno.mainloop()
