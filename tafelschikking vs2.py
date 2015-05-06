import random

aantalPerTafel = 2
aantalGangen = 3
aantalVrouwen = 3
aantalMannen = 3

personen=[]
for i in range(aantalMannen):
    personen.append('M'+str(i+1))
for i in range(aantalVrouwen):
    personen.append('V'+str(i+1))

persoonPersoon = {}
tafelSchikking = []
tafelSchikkingRonde = []
aantalTafels = len(personen)/aantalPerTafel
maxGangenZonderDubbel = (((aantalMannen+aantalVrouwen)-1)/aantalPerTafel)+1
print "max aantal gangen :", maxGangenZonderDubbel

#=====================================================================================================
#stelt het aantal dubbelen zittingen vast
def dubbelen() :
    if persoonPersoon :
        dubbelTeller = 0
        for n in persoonPersoon :
            i = 0
            while i < len(persoonPersoon[n])-1 :
                if sorted(persoonPersoon[n])[i] == sorted(persoonPersoon[n])[i+1] :
                    dubbelTeller = dubbelTeller + 1
                i = i + 1
        return dubbelTeller
    
#=====================================================================================================
#husselt een willekeurige lijst at random
def husselaar(lijst) :
    tempLijst=lijst[:]
    outputLijst=[]
    for n in range(len(lijst)) :
        keuze = random.randrange(len(tempLijst))
        outputLijst.append(tempLijst[keuze])
        tempLijst[keuze:keuze+1] = []
    return outputLijst        



#======================================================================================
# het feitelijk husselen van de personen obv de functie husselaar
#personen = husselaar(personen)
#print "46 personen : ", personen



#===================================================================================================
#Vaste toedeling op basis van de net gehusselde personen

personenNog = personen[:] # copietje alle personen
print "54 personenNog als copie van personen bij de start :", personenNog
j = 0
i = 0
k = 0
while j < aantalTafels :
    i = 0 
    tafelTemp = []
    while i < aantalPerTafel :
        persoonKeuze = personenNog[i+k]
        tafelTemp.append(persoonKeuze)
        #personenNog[i:i+1] = [] 
        i = i + 1
        print "tafelTemp :",tafelTemp
    tafelSchikking.append(tafelTemp)
    print "tafelScvhikking :", tafelSchikking
    k=k+aantalPerTafel # was 4 ??
    j = j +1
tafelSchikkingRonde.append(tafelSchikking)
print "71 tafelschikking : ", tafelSchikking

"""
#===================================================================================================
#toedeling aan de tafels ronde 1 gelijke verdeling mannen en vrouwen

personenNog = husselaar(personen)# copietje alle personen maar welke na de hussel ?
manvrouw=[]
for n in personenNog :
    manvrouw.append(n[0])
tafelTemp = []
print"personenNog :", personenNog
print "manvrouw :", manvrouw
i = 0
j = 0
while j < 4:
    i = 0
    while i < aantalPerTafel :
        if i%2 == 0 :
            mIndex = manvrouw.index("M")
            tafelTemp.append(personenNog[mIndex])
            print  "tafelTemp :", tafelTemp
            del manvrouw[mIndex]
            del personenNog[mIndex]
            print "manvrouw :", manvrouw
            print "personenNog :", personenNog
        else :
            mIndex = manvrouw.index("V")   
            tafelTemp.append(personenNog[mIndex])
            print  "tafelTemp :", tafelTemp
            del manvrouw[mIndex]
            del personenNog[mIndex]
            print "manvrouw :", manvrouw
            print "personenNog :", personenNog
        i=i+1
    tafelSchikking.append(tafelTemp)
    print "tafelSchikking :", tafelSchikking
    tafelTemp =[]
    j = j + 1
tafelSchikkingRonde.append(tafelSchikking)
print "tafelschikking test :",tafelSchikking

"""      
#===================================================================================================
# toevoegen aan PersoonPersonen na ronde 1

j = 0
while j < len(tafelSchikking) :
    i = 0
    while i < len(tafelSchikking[j]) :
        varTemp = tafelSchikking[j][:]
        varTemp[i:i+1] = []
        persoonPersoon[tafelSchikking[j][i]] = varTemp
        i = i + 1
    j = j + 1    
print "128 In de 1e gang is het aantal dubbelen: ",dubbelen()
print "129 persoonPersoon :", persoonPersoon

#===================================================================================================
# random toedeling aan de tafels na 1e ronde


gangenTeller = 1
while gangenTeller < aantalGangen :

    personenNog = personen[:]
    tafelSchikking = []
    j = 0
    k = 0 
    while j < aantalTafels :
        tafelTemp = []
        persoonKeuze = personenNog[k]
        tafelTemp.append(persoonKeuze) # de eerste persoon van de nieuwe tafel
        personenNog.remove(persoonKeuze) # verwijder persoon uit nog beschikbare personen
        teZoeken = persoonPersoon[persoonKeuze]
        personenNogNaEerste = personenNog[:]
        i = 0
        while len(tafelTemp) < aantalPerTafel : # zolang de tafel nog niet is gevuld
            for persoonKeuze in personenNogNaEerste :
                if not persoonKeuze in teZoeken :
                    tafelTemp.append(persoonKeuze)
                    personenNog.remove(persoonKeuze)
                    teZoeken = teZoeken + persoonPersoon[persoonKeuze]
                    i = i + 1
                if len(tafelTemp)== aantalPerTafel :
                    break
            #print "159 j is :", j
            #print "160 gangenTeller :", gangenTeller
            #print "161tafelTemp :", tafelTemp    
            if len(tafelTemp) < aantalPerTafel : # is de tafel dus nog steeds niet gevuld dan iemand kiezen die al bij de anderen heeft gezeten
                for persoonKeuze in personenNog :
                    var1 = teZoeken.count(persoonKeuze)
                    print "165 var1: ", var1
                    if var1 == 0 :
                        print "167 var0 is geraakt"
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if var1 == 1 :
                        print "var1 is geraakt"
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if var1 == 2 :
                        print "var 2 is geraakt"
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if var1 == 3 :
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if var1 == 4 :
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if var1 > 4 :
                        tafelTemp.append(persoonKeuze)
                        personenNog.remove(persoonKeuze)
                    if len(tafelTemp)== aantalPerTafel :
                        break
        tafelSchikking.append(tafelTemp)
        j = j +1
    tafelSchikkingRonde.append(tafelSchikking)
    
    #===================================================================================================
    # toevoegen aan PersoonPersonen na elke ronde
    j= 0
    while j < len(tafelSchikking) :
        i = 0
        while i < len (tafelSchikking[j]) :
            varTemp = tafelSchikking[j][:] 
            varTemp[i:i+1] = []
            for p in varTemp :
                persoonPersoon[tafelSchikking[j][i]].append(p) 
            i = i + 1
        j = j + 1
        
    gangenTeller = gangenTeller+1
    print "In de",gangenTeller,"de gang is het aantal dubbelen: ",dubbelen()
    
# printjes maken
#===================================================================================================
print ""
i=0
for n in tafelSchikkingRonde :
    print "tafel schikking ronde :",i+1,"\n",tafelSchikkingRonde[i]
    i=i+1

print ""  
#print "PersoonPersoon :\n", persoonPersoon
print ""
#print "Persoonpersoon even gesorteerd :\n"
#for n in persoonPersoon :
#    print n, ":", sorted(persoonPersoon[n])





                  


    


