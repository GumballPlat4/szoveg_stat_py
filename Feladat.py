
def beolvasas(szoveg):
    
    with open("info.txt", "r", encoding="utf-8") as fm:
        szoveg = fm.read()


def megszamolas(szoveg,szavak_lista):
    szavak_lista=[]
    for szo in szoveg.split():
            szavak_lista.append(szo)
    return szavak_lista

def megforditas():
    info="info.txt"[::-1]

def listaba_olv(l):
    l=[]
    l = szoveg.split()
    
def kivalasztas(szavak):    
    leghosszabb = szavak[0]
    
    for szo in szavak[1:]:
       
        if len(szo) > len(leghosszabb):
           
            leghosszabb = szo
    
    return leghosszabb

def maganhangzo_szama():
    maganhangzok = "a","e","i","o","u","á","é","í","ó","ö","ő","ú","ü","ű"
    szoveg = szoveg.lower()
    maganhangzok_szama = sum(szoveg.count(mh) for mh in maganhangzok)
    return maganhangzok_szama

def masalhangzok_szama(szoveg):
    maganhangzok = "a","e","i","o","u","á","é","í","ó","ö","ő","ú","ü","ű"
    szoveg = szoveg.lower()
    masalhangzok_szama = sum(1 for betu in szoveg if betu.isalpha() and betu not in maganhangzok)
    return masalhangzok_szama



def kiir(szvg,sz_sz_szama,m_megforditasa,listaba_ol,legh_szo,mag_hangzo,mas_hangzo):
    print(szvg)
    print(f"A szöveg {sz_sz_szama} szóból áll.")
    print(f"A szöveg visszafelé{m_megforditasa}")
    print(listaba_ol)
    print(f"A leghosszabb szó a(z) {legh_szo}")
    print(mag_hangzo)
    print(mas_hangzo)
    


szoveg=beolvasas
sz_szavak_szama=megszamolas
visszafele=megforditas
listaba_olvasas=listaba_olv
leghosszabb_szo=kivalasztas
maganhangzo=maganhangzo_szama
masalhangzok=masalhangzok_szama
szavak="info.txt"

maganhangzok_szama_teljes=(szavak)
masalhangzok_szama_teljes=(szavak)

kiir(szoveg,sz_szavak_szama,visszafele,listaba_olvasas,leghosszabb_szo,maganhangzo,masalhangzok)




