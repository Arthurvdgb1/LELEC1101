from numpy import *

#Calcul des capacités (resp. résistances) équivalentes possible avec deux capacités (resp. résistances)
listCapaPossible=[]
for C1 in [10e-9,15e-9,22e-9,100e-9]:
    for C2 in [0,10e-9,15e-9,22e-9,100e-9]:
        Cpara=C1+C2
        if Cpara not in listCapaPossible:
            listCapaPossible.append(Cpara)
        if C2!=0:
            Cser=1/(1/C1+1/C2)
        else :
            Cser=C1
        if Cser not in listCapaPossible:
            listCapaPossible.append(Cser)
            
listResiPossible=[]
for R1 in [100,1000,2200,8200,10000,22000,100000]:
    for R2 in [100,1000,2200,8200,10000,22000,100000]:
        Rser=R1+R2
        if Rser not in listResiPossible:
            listResiPossible.append(Rser)
        Rpara=1/(1/R1+1/R2)
        if Rpara not in listResiPossible:
            listResiPossible.append(Rpara)


#Calcul des résistance théoriques en fonction des conditions imposées et des capacités équivalentes possibles
#On met un tuple pour garder le couple R-C en mémoire
#Retirer une condition en commentaire pour voir valeurs des composants respectant la condition choisie
listResiTheorique=[]
for C in listCapaPossible:
    R=1/(2*pi*C*3000) #Condition Déphasage
    #R=...  #Condition ...
    listResiTheorique.append((R,C))


#On trouve la meilleure combinaison et on la print
best=(1,0,0,0)
for R_theorique,C in listResiTheorique:
    for R_possible in listResiPossible:
        if best[0]<abs((R_possible-R_theorique)/R_theorique):
            pass
        else :
            best=(abs((R_possible-R_theorique)/R_theorique),R_theorique,R_possible,C)
print("La meilleur combinaison R-C que l'on peut obtenir est R={0:.4g}k et C={1:.4g}nF".format(best[2]/1000,best[3]*10**9))
print("Pour remplir parfaitement la condition R devrait être égal à {0:.4g}k soit une erreur de {1:.3g}%".format(best[1]/1000,best[0]*100))


#On cherche comment obtenir la capacité et la résistance équivalente trouvée
comp=0.01
for C1 in [10e-9,15e-9,22e-9,100e-9]:
    for C2 in [0,10e-9,15e-9,22e-9,100e-9]:
        Cpara=C1+C2
        if abs(Cpara-best[3])/best[3]<comp:
            print("On obtient la capacité équivalente en mettant 2 capacités en parallèle : C1={0:.2g}nF et C2={1:.2g}nF".format(C1*10**9,C2*10**9))
            comp=-1 #pas print 2 fois le même couple de capacité
        if C2!=0:
            Cser=1/(1/C1+1/C2)
        else :
            Cser=C1
        if abs(Cser-best[3])/best[3]<comp:
            print("On obtient la capacité équivalente en mettant 2 capacités en série : C1={0:.2g}nF et C2={1:.2g}nF".format(C1*10**9,C2*10**9))
            comp=-1 #pas print 2 fois le même couple de capacité
comp=0.01            
for R1 in [100,1000,2200,8200,10000,22000,100000]:
    for R2 in [100,1000,2200,8200,10000,22000,100000]:
        Rser=R1+R2
        if Rser not in listResiPossible:
            listResiPossible.append(Rser)
        if abs(Rser-best[2])/best[2]<comp:
            print("On obtient la résistance équivalente en mettant 2 résistances en série : R1={0:.2g}k et R2={1:.2g}k".format(R1/1000,R2/1000))
            comp=-1 #pas print 2 fois le même couple de résistance
        Rpara=1/(1/R1+1/R2)
        if abs(Rpara-best[2])/best[2]<comp:
            print("On obtient la résistance équivalente en mettant 2 résistances en parallèle : R1={0:.2g}k et R2={1:.2g}k".format(R1/1000,R2/1000))
            comp=-1 #pas print 2 fois le même couple de résistance
            
            
            
