# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#
#
#
import sys
import psutil

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Viktor Setervang', \
			'student2': 'Ola Mathiesen', \
            'student3': 'Tord Resch Lindaas', \
            'student4': 'Michael Matthew Desmond', \
}

#
#  Oppgave 1
#    Leke med utskrift
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '`
def ascii_bird():
	ws = " "
	print(ws*5+"\\/_\n\\,"+ws*3+"/("+ws+",/\n"+ws+"\\\\\\'"+ws+"///\n"+ws*2+"\\_ /_/\n"+ws*2+"(./\n"+ws*3+"'`")


#
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og
#					den mest signifikante bit-en er lengst til venstre
def bitAnd(x, y):
	return int(bin(x&y), 2)
#
#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
    return int(bin(x^y), 2)
#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
	return int(bin(x|y), 2)
#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#
#  Besvarelse:
#   Begrensningene til ord():
#    Hvis man skriver ord('Å') så får man feilmeldingen: "TypeError: ord() expected a character,
#    but string of length 2 found" Hvis vi skriver len('Å') så får vi length 2.
#    Grunnen til dette er at python2 er basert på encodinga ASCII (American Standard Code for Information Interchange),
#    og her inngår blant annet ikke ØÆÅ. For å kunne skrive disse bokstavene må man endre encoding til et tegnsystem
#	 hvor disse inngår, som f.eks latin-1 eller utf-8. Dette vil derimot ikke få denne koden til å
#    fungere.
#
#    Hvis vi i python terminalen skriver ord(u'Å') så vil man få desimalene til Å(197), hvis vi da bruker bruker
#    "motstykket" unichr(197), så får vi '\xc5' istenfor u'Å', hvor \x henviser til hexadecimal c5.
#
def ascii8Bin(letter):
	char = ord(letter)
	ascii8Bin = '{0:08b}'.format(char)
	return ascii8Bin
#
#
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut:
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut:
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
#   Kommentar til koden:
#   l referer til en liste med samme elementer som string.
#   test blir deklarert som en liste.
#   En for loop som går gjennom alle elementene i listen, dvs alle bokstavene i ordet.
#   I loopen skrives det ut den binære representasjon av hvert tegn (bruker ascii8Bin funksjonen)
#   %s henviser til stringen c som her en bokstav.
#   Den binære representasjonen av hver bokstav blir satt inn i listen test.
#   Returner listen slik at den kan testes av funksjonen test().
#
def transferBin(string):
	l = list(string)
	test = []
	for c in l:
		print "Den binære representasjonen for %s" % c
		print ascii8Bin(c)
		test.append(ascii8Bin(c))
	return test
#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def ascii2Hex(letter):
	char = ord(letter)
	ascii2Hex = '{0:02x}'.format(char)
	return ascii2Hex

def transferHex(string):
	l = list(string)
	test = []
	for c in l:
		print "Den heksadesimale representasjonen for %s" % c
		print ascii2Hex(c)
		test.append(ascii2Hex(c))
	return test
#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	char = character.decode("utf-8")
	char = ord(char)
	unicodeBin = '{0:08b}'.format(char)
	return unicodeBin

# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
#Besvarelse:
#   Ut i fra det jeg fant, så hadde psutil IKKE støtte til å finne følgende punkter:
# 	1.		Brand and model
# 	2.		Display resolution and size
# 	3.		Operating system
#   På psutil sin hjemmeside skriver de at psutil er hovedsakelig for å hente ut informasjon om kjørende prosesser, og for å sjekke system ytelse.
#   Siden ingen av disse 3 punktene går under hovedbruksområdene til psutil så er det kanskje ikke så rart at det ikke ligger støtte for det.
#
#   Terminalen i linux tilbyr flere commands for å finne informasjon om hardware.
#	En veldig generel command er lshw, lshw lister opp en kort detaljert beskrivelse av det meste av hw, den henter
#   ut informasjonen fra forskjellige /proc filer.
#   For å få informasjon om display kan vi terminalen skrive: xrandr | grep '*'
#	For å få info om operativ systemet kan vi i terminalen skrive: cat /etc/issue
#
#   De forskjellige partisjonene
#
#	ln:211 Bruk mountpoint som parameter i ln:213
#   ln:213 Parameteren er(mountpoint) total == capicity
#   Virtuelt minne
#   Swap minne
#   CPU hastighet.
#
def printSysInfo():
	n = "\n"
	print "Hard drive partitions:"
	print str(psutil.disk_partitions())+n
	print "Hard drive capacity == total:"
	print str(psutil.disk_usage('/'))+n
	print "Virtual memory:"
	print str(psutil.virtual_memory())+n
	print "Swap memory:"
	print str(psutil.swap_memory())+n
	print "CPU speed:"
	print str(psutil.cpu_times())+n

def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin("Hi") == ['01001000','01101001']
	assert transferHex("Ab") == ['41','62']
	assert unicodeBin('å') == '11100101'
	return "Testene er fullført uten feil."

print test()
