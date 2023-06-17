import pyRekurzivneNizListe

class prosirenaPyRekirzivnaNizLista(pyRekurzivneNizListe.pyRekurzivneNizLista):
    def fakotorijelOdTekuceg(self, x): #Racuna faktorijel tekuceg elementa
        if x <= 1: #Ako je 1 vraca 1
            return 1 
        else: 
            return (x*self.fakotorijelOdTekuceg(x-1)) #Ako je razlicito od 1, onda poziva rekuzrivno funkciju, ali je element umanjen za 1
        
    def KubTekucegElementa(self, tek): #Prosljedjujemo uneseni element
        pom = self.fakotorijelOdTekuceg(tek) #U pom smjestamo fakotirjel od tog broja
        pom = pom*pom*pom #Kubiramo
        print("Kub fakotorijela od tekuceg elementa iznosi: " + str(pom)) #Ispisujemo vrijednost kubiranog elementa
    
    
    def sumaElemenata(self, niz,duzina):
        if(duzina==0):
            return 0
        else:
            return int(niz[duzina-1])+int(self.sumaElemenata(niz,duzina-1))
    
    def proizvodElemenata(self,niz,duzina):
        if(duzina==0):
            return 1
        else: 
            return int(niz[duzina-1])*int(self.proizvodElemenata(niz,duzina-1))
