import pyNizListe
import random
import time


class pySortiranjeNizListe(pyNizListe.NizLista):


    def insertionSort(self):
        start_time = time.time()
        
        for i in range (1, self.duzina):
            privremeni = self.Niz[i]
            j = i -1
            while ((j>= 0) and (self.Niz[j]>privremeni)):  
                self.Niz[j+1] = self.Niz[j]
                j = j-1
            self.Niz[j+1]=privremeni
        
        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")



    def bubbleSort(self):
        start_time = time.time()
        
        for i in range(self.duzina-1,0,-1):
            for j in range(1,i+1):
                if(self.Niz[j-1] > self.Niz[j]):
                    privremeni = self.Niz[j-1]
                    self.Niz[j-1]=self.Niz[j]
                    self.Niz[j] = privremeni

        print("Lista sortirana za " + str(time.time() - start_time) + " sekundi")




    def Merge(self, l, p , q, u):        
 
        l = int(l)
        p = int(p)
        q = int(q)
        u = int(u)
        
        i = 0
        j = q-l
        k = l
        
        B = self.kreiraj_niz(u-l+1)
        for m in range(0,u-l+1):
            B[m] = self.Niz[l+m]
        
        while ((i <= p-l) and (j <= u-l)):
            if(B[i] < B[j]):
                self.Niz[k] = B[i]
                i+=1                
            else:
                self.Niz[k] = B[j]
                j+=1                
            k+=1

        while(i <= p-l):            
            self.Niz[k] = B[i]
            k+=1
            i+=1

        while(j <= u-l):           
            self.Niz[k] = B[j]
            k+=1
            j+=1

        del B

    def MergeSort(self,l,u):
 
        l = int(l)
        u = int(u)

        if (u > l):
            p = (l+u-1)/2
            q = p + 1
            self.MergeSort(l,p)
            self.MergeSort(q,u)
            self.Merge(l,p,q,u)


    def popuniListuRand(self): 
        for i in range(1,self.kapacitet):        
            self.dodaj(random.randint(1,1000))
