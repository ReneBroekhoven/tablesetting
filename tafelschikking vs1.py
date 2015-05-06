import random

aantalPerTafel = 4
aantalGangen = 4
aantalVrouwen = 8
aantalMannen = 8
personen=[]
i=1
while i< aantalMannen+1 :
     personen.append('m'+str(i))
     i=i+1
i=1
while i< aantalVrouwen+1 :
     personen.append('v'+str(i))
     i=i+1

persoonPersoon = {}
tafelSchikking = []
tafelSchikkingRonde = []
aantalTafels = len(personen)/aantalPerTafel

#=====================================================================================================
#stelt het aatal dubbelen zittingen vast
def dubbelen() :
    if persoonPersoon :
        dubbelTeller = 0
        for n in persoonPersoon :
            #print n, sorted(persoonPersoon[n])
            i = 0
            while i < len(persoonPersoon[n])-1 :
                if sorted(persoonPersoon[n])[i] == sorted(persoonPersoon[n])[i+1] :
                    #print "EEN DUBBELE : ", sorted(persoonPersoon[n])[i]
                    dubbelTeller = dubbelTeller + 1
                i = i + 1
        return dubbelTeller

#===================================================================================================
#willekeurige toedeling aan de tafels ronde 1

personenNog = personen[:] # copietje alle personen
j = 0
while j < aantalTafels :
    i = 0 
    tafelTemp = []
    while i < aantalPerTafel :
        persoonKeuze = random.randrange(len(personenNog))
        tafelTemp.append(personenNog[persoonKeuze])
        personenNog[persoonKeuze:persoonKeuze+1] = [] 
        i = i + 1
    tafelSchikking.append(tafelTemp)
    j = j +1
tafelSchikkingRonde.append(tafelSchikking)
       
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
print "In de 1e gang is het aantal dubbelen: ",dubbelen()

#===================================================================================================
# random toedeling aan de tafels na 1e ronde
gangenTeller = 1
while gangenTeller < aantalGangen :

    personenNog = personen[:]
    tafelSchikking = []
    j = 0
    while j < aantalTafels :
        tafelTemp = []
        persoonKeuze = random.choice(personenNog)
        tafelTemp.append(persoonKeuze) # de eerste persoon van de nieuwe tafel
        personenNog.remove(persoonKeuze) # verwijder persoon uit nog beschikbare personen
        teZoeken = persoonPersoon[persoonKeuze]
        #print "1e persoon is : ", persoonKeuze
        #print "te zoeken bij de eerste van de tafel: ", teZoeken
        i = 0
        while len(tafelTemp) < aantalPerTafel : # zolang de tafel nog niet is gevuld
            for persoonKeuze in personenNog :
                if not persoonKeuze in teZoeken :
                    tafelTemp.append(persoonKeuze)
                    personenNog.remove(persoonKeuze)
                    teZoeken = teZoeken + persoonPersoon[persoonKeuze]
                    i = i + 1
                if len(tafelTemp)== aantalPerTafel :
                    break
            #print "teZoeken :",teZoeken
            if len(tafelTemp) < aantalPerTafel : # is de tafel dus nog steeds niet gevuld dan iemand kiezen die al bij de anderen heeft gezeten
                for persoonKeuze in personenNog :
                    var1 = teZoeken.count(persoonKeuze)
                    #print "var1: ", var1
                    if var1 == 0 :
                         tafelTemp.append(persoonKeuze)
                         personenNog.remove(persoonKeuze)
                    if var1 == 1 :
                         tafelTemp.append(persoonKeuze)
                         personenNog.remove(persoonKeuze)
                    if var1 == 2 :
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
i=1
for n in tafelSchikkingRonde :
    print "tafel schikking ronde ",i,"\n",tafelSchikkingRonde[0]
    i=i+1 



                  


    


