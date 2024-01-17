# Datatyper

heltall = 21
desimaltall = 3.14
tekststreng = "Hello world!"
bool = True or False
liste = [1, 2, 2.77, "pi", True, [1]]
tupple = (3, 4)
sett = {"eple", "banan", "drue"}
oppslagsverk = {"merke": "Apple", "modell": "MacBook"}
ingenting = None

# Eksempel

# print("Hva er din alder?")

# alder = input()

# ny_alder = alder + 10

# print("Om 10 år er du "+ny_alder+" år gammel!")

# Eksempel listemetoder

liste = [1, 2]
print(liste[1])  # 2
liste.append(2.77)
print(liste)  # [1, 2, 2.77]
liste2 = ["pi", True]
liste.extend(liste2)
print(liste)  # [1, 2, 2.77, "pi", True]
liste.insert(2, 25)
print(liste)  # [1, 2, 25, 2.77, 'pi', True]
liste.remove("pi")
print(liste)  # [1, 2, 25, 2.77, True]
liste.sort()
print(liste)  # [1, True, 2, 2.77, 25]
liste.reverse()
print(liste)  # [25, 2.77, 2, True, 1]

# Eksempel slicing

liste = list(range(0, 20))  # 0 t.o.m 19
streng = "Hello world!"

første_halvdel = liste[0:10]
print(første_halvdel)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bare_partall = liste[:10:2]
print(bare_partall)  # [0, 2, 4, 6, 8]
fem_til_15 = liste[5:15]
print(fem_til_15)  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

hello = streng[:5]
print(hello)  # "Hello"
world = streng[6:]
print(world)  # "world!"

# Strengmetoder

print("Tekst meD sMå Og STOre BoksTaver".lower())
# "tekst med små og store bokstaver"

print(" \n    Litt vel mye mellomrom her      \n".strip())
# "Litt vel mye mellomrom her"

print("Litt vel mye mellomrom fortsatt".replace(" ", ""))
# "Littvelmyemellomromfortsatt"

print("".join(["liste", "av", "strings", "til", "en", "string"]))
# "listeavstringstilenstring"

print("tilbake til en liste av strings".split())
# ['tilbake', 'til', 'en', 'liste', 'av', 'strings']

# Oppgave slicing
# Fullfør programmet

streng = "abcd"
ekstra = "XY"
ønsket_streng = "abXYcd"

... == ønsket_streng


# Oppgave lister
frukter = ["eple", "banan"]
flere_frukter = ["appelsin", "druer"]
alle_frukter = ["eple", "banan", "appelsin", "druer"]

frukter.append(flere_frukter)
print(frukter == alle_frukter)

# Oppgave strenger

streng = "   abXYcd   \n"
ønsket_streng = "abxycd"

streng.lower().strip()

print(streng == ønsket_streng)

# Eksempel f-strenger

pris_per_enhet = 5.98765
antall_enheter = 8

print(f"Totalpris: {pris_per_enhet * antall_enheter:.2f} kr")
# Totalpris: 47.90 kr

# Vanlig feil: Glemmer å avslutte uttrykket før formattering
# print(f"Totalpris: {pris_per_enhet * antall_enheter.2f} kr")
# Dette vil gi en syntax error

# Oppgave f-streger

# Avrund pi til to desimaler
pi = 3.14159265

print(...)

# Ønsket output: "pi = 3.14"

# Eksempel løkker

frukter = ["eple", "banan", "kiwi"]
frukt_farge = {
    "eple": "rødt",
    "banan": "gul",
    "kiwi": "grønn"
    }

for frukt in frukter:
    print(f"Frukt: {frukt}")
for i in range(len(frukter)):
    frukter[i] = frukter[i].upper()
    print(f"Frukt: {frukter[i]}")

i = 0
while i < len(frukter):
    print(f"Frukt: {frukter[i]}")
    i += 1

for frukt, farge in frukt_farge.items():
    print(f"Frukten {frukt} er {farge}.")

# Eksempel løkker

# frukter = ["eple", "banan", "kiwi"]

# for i in range(frukt):
#     frukter[i] = frukter[i].upper()
#     print(f"Frukt: {frukter[i]}")
#     i = i + 1

# for nummer in range(10):
#     if nummer == 5:
#         break
#     print(nummer)
# # Printer tall fra 0 til 4 og stopper ved 5

# for nummer in range(10):
#     if nummer % 2 == 0:  # Hopper over partall
#         continue
#     print(nummer)  # Printer kun oddetall

# for nummer in range(10):
#     if nummer % 2 == 0:
#         pass  # Gjør ingenting for partall
#     else:
#         print(f"Oddetall: {nummer}")

# # Eksempler funksjoner

# def addere(x, y):
#     return x + y

# print(addere(2,5))
# # 7
# print(addere("femti","to"))
# # "femtito"

# def dividere(x, y):
#     return x / y

# print(addere(10, dividere(10, 2)))
# # 15.0

# # Flere eksempler funksjoner

# # Eks 1
# def dividere(x, y):
#     x / y

# print(dividere(20,2))

# # Eks 2
# def dividere(x, y):
#     print(x / y)

# print(dividere(20,2))

# # Eks 3
# def dividere(x, y):
#     return x / y

# print(dividere(20,2))

# # Eks 4
# def alle_oddetall(numre):
#     for tall in numre:
#         if tall % 2:
#             return tall
        
# numre = list(range(10))
# print(alle_oddetall(numre))

# # Fasit:
# # Eks 1
# def dividere(x, y):
#     x / y

# print(dividere(20,2)) # None

# # Eks 2
# def dividere(x, y):
#     print(x / y)

# print(dividere(20,2))
# # 10.0
# # None

# # Eks 3
# def dividere(x, y):
#     return x / y

# print(dividere(20,2)) # 10.0

# # Eks 4
# def alle_oddetall(numre):
#     for tall in numre:
#         if tall % 2:
#             return tall
        
# numre = list(range(10))
# print(alle_oddetall(numre)) # 1


# Nøstete løkker:

grid = [
    [2, 3, 5],
    [1, 4, 7],
]

rows = len(grid) # 2
cols = len(grid[0]) # 3

grid2 = []

for row in range(rows):
    row2 = []
    for col in range(cols):
        celle = grid[row][col]
        row2.append(celle*2)
    grid2.append(row2)

print(f"{grid2 = }")
# grid2 = [[4, 6, 10], [2, 8, 14]]

# Feilhåndering eksempel

# try:
#     tall = int(input("Skriv inn et tall: "))
#     resultat = 10 / tall
# except:
#     print("Det har skjedd en feil")

# try:
#     tall = int(input("Skriv inn et tall: "))
#     resultat = 10 / tall
# except ZeroDivisionError:
#     print(f"Kan ikke dele med null.")
# except ValueError:
#     print(f"Vennligst skriv inn et gyldig tall.")
# except Exception as e:
#     print(f"En uventet feil oppstått: {e}")


# relativ_filsti = './prosjekt/data.txt'
# absolutt_filsti = '/home/brukernavn/dokumenter/prosjekt/data.txt'

# # Skrive til en fil
# with open(relativ_filsti, 'w') as fil:
#     fil.write('Tekst i fil')
    
# # Lese fra en fil
# with open(relativ_filsti, 'r') as fil:
#     innhold = fil.read()
#     print(innhold)
# # Skriver ut 'Tekst i fil'

# Eksempel betingelser

temperatur = 25

if temperatur > 25:
    print("Det er varmt")
elif temperatur >= 10:
    print("Husk jakke")
    # printes
else:
    print("Huff, så kaldt!")

vær = "regn"

if temperatur > 25 and vær == "sol":
    print("Husk solkrem")
elif temperatur >= 10 or vær != "regn":
    print("Norsk sommer :-)")
    # printes
elif temperatur is None or not vær:
    print("Ingen data")

# Kodesporing 1

x = 5
y = 2
x += y
y = x - y
x *= 2
print(x // y)


pi = 3.1415546789

print(f"{pi = :.2f}")


a = [1,2]

print(a in a)


# a =  [1, 2.2, "3", "a"]


# print(a[0:1])

# pi = 3.14159265

# print(f"{pi = :.2f}")

# frukter = ["eple", "banan", "kiwi"]

# for i in range(len(frukter)):
#     frukter[i] = frukter[i].upper()
#     print(f"Frukt: {frukter[i]}")
#     i = i + 1

# streng = "abcd"
# ekstra = "XY"
# ønsket_streng = "abXYcd"

# ny_streng = streng[:2]+ekstra+streng[2:]

# print(ny_streng)

x = 5
y = 2
x += y # x = 7
y = x - y # y = 5
x *= 2 # x = 14
print(x // y) # 2