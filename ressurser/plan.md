# timeliste:
04.11 16:00 - 17:00 # 1t
11.11 11:45 - 13:30 # 1t 45m
12.11 11:30 - 17:00 # 5t 30m
13:11 10:00 - 14:00 # 4t
14:11 15:00 - 18:30 # 3t 30m
15:11 10:00 - 14:30 # 4t 30m
16:11 12:00 - 13:30 # 1t 30m
17:11 14:30 - 18:30 # 4t

* memes
* oppgaver til salen
    * små oppgaver for å øke engesjemtn + variere undervisningen
        * Think, pair, share 1-5 min
        * Eks: hva skjer når vi kjører denne koden? hva er galt her?
* meningsmålinger?
* kode uten hjelpemiddler
    * tips/triks/strategi
* hvordan øve til eksamen
* strategi på ekseamen
* masse eksempler
* spørsmål fra salen, mulighet for å stille på nett? (må finne løsning)
* oppfordre til dialog ikke monolog
* hente innhold fra youtube, fagsiden, prøveeksamen, ppt fra ifjor, innleveringene
* vurdere om eksemplene bør gjøres i plaintext eller .py (siden eksamen er uten IDE)
* øving gjør mester
* Make it work, make it right
* Stegvis prosess, bryte store problemer ned i mindre biter
* Holding/instilling: dette får jeg til
* syklus:
    * teori (memes der det passer)
    * eksempel
    * praktisk oppgave til salen
    - rinse and repeat
* huske å gjennta høyt spørsmål som stilles fra salen

## Innhold


Grunnleggende datatyper
Heltall (`int`)
Desimaltall (`float`)
Tekststrenger (`str`)
Boolske verdier (`bool`)
Samlinger
Lister (`list`)
Tuppler (`tuple`)
Sett (`set`)
Oppslagsverk/ordbok (`dict`)
Spesialtyper
"Ingenting"/"ingen verdi" (`None`)


Listemetoder

`append(element)`
    Legger til et element på slutten av listen
`extend(list2)`
    Utvider listen med flere elementer
`insert(index, element)`
    Setter inn et element på spesifisert indeks
`remove(element)`
    Fjerner første forekomst av et element
`pop(index)`
    Fjerner og returnerer element på indeks
`sort()`
    Sorterer listen på stedet
`reverse()`
    Reverserer listen


`liste[start:slutt:steg]`
    Henter en del av listen fra start til slutt, med gitt stegstørrelse
`streng[start:slutt]` 
    Henter en del av strengen fra start til slutt


Strengmetoder

`upper()` / `lower()`
    Gjør om strengen til store/små bokstaver
`strip()`
    Fjerner whitespace fra begynnelsen og slutten av strengen
`.split(separator)`
    Deler opp strengen i en liste basert på separator
`join(liste)`
    Sammenslår elementer i en liste til en streng med gitt separator


Konkatenering
`print("Hei, " + navn + "!")`
Elementutlisting
`print("Hei,", navn, "!")`
Formatert Strenger (f-streng)
`print(f"Hei, {navn}!")`
String Formatting (.format()-metoden)

Flere finnes, men brukes lite

Iterative for-løkker
    `for element in liste:`
        Iterasjon direkte over elementer i en liste.
Indekserte for-løkker
    `for i in range(len(liste)):`
        Bruk indeks for å manipulere elementer.
While-løkker
    `i = 0`
    `while i < len(liste)`
        Basert på en betingelse, kan bruke indeks.

Løkke over ordbok:
    `for key, value in dict.items():`
        Itererer over nøkkel-verdi par.

Nyttige Funksjoner og Metoder
`range(start, stop)`
    For numeriske løkker.
`enumerate(iterable)`
    For indeks og verdi samtidig.
`len(iterable)`
    For å vite antall elementer.

"Løkkeflyt"
`break`
    For avslutte en løkke.
`return`
    Brukes for å avslutte løkker innenfor funksjoner.
`continue`
    Hopp til neste iterasjon.
`pass` og `...` Ingen operasjon, placeholder.

Kan du lage en lignende oppgave?:

Hva skriver dette programmet ut? (hvis programmet krasjer, skriv kun ‘Error’)

```py
b = 3
a = a * b
b = a + b
a -= 1
print(b - a)
```

Oppgaven er ment til å teste "kodesporingsevnen" hos stuendene. Altså at de klarer å forstå hva som skjer steg for steg i programmet.

## (b) Destruktive og ikke-destrukive funksjoner i snake (10 poeng)

### Forklar forskjellen på en destruktiv og en ikke-destruktiv funksjon. Vis til eksempler på begge deler i det vedlagte løsningsforslaget til lab6.