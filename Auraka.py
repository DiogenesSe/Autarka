########################import#######################
import sys
import time
import os
from tkinter import *
import subprocess
import threading
###########Variablen-Rechnung########################
WkSpeicherz = 0.6
WProd = WkSpeicherz 
WkProdz = 0.4
WBrenn = WkProdz
WkHProdz = 3
COP = WkHProdz
WkSolarz = 0.3
WPE = 0.15
WPB = 0.57
Aufschlüsselung_warme=[0.1620,0.1300,0.1250,0.0810,0.0350,0.0220,0.0170,0.0160,0.0520,0.0840,0.1220,0.1550]
####################Variablen########################
zahlkategorien = 4
lösunge = [[]]
labels = []
nn = []
ll = []
H2ein = []
Hg = []
H2aus =[]
zweid =[[]]
Startxtext = 2
Startytext = 1
####################Def###############################
def heiz():
    hiimum = Tk("Ergebnis")
    mium = Label(hiimum, text="Insgesamter Verbrauch",fg="gray")
    mium.grid(row=1,column=1)
    global ah
    ah= Text(hiimum, height=1,width=10)
    ah.grid(row=2, column=2)
    global jjm
    jjm =Button(hiimum, text="Eingeben", command=angabe)
    jjm.grid(row=3,column=1)
def angabe():
    zwischnwärme =  []
    zwischenwärme = zweid[4]
    for intwärme in range(0,12):
        zwwärmint = ah.get("1.0","end-1c")
        wärmerg = float(zwwärmint)*float(Aufschlüsselung_warme[intwärme])
        zwischenwärme[intwärme].insert(INSERT, str(wärmerg))
#####################Def-Berechnen#######################    
def Auslesen():
    nn= []
    lmn = []
    nn= zweid[1]
    for Kasm in range(0, zahlkategorien):
        nn = zweid[Kasm+1]
        for z in range(0,12):
            lmn.append(nn[z].get("1.0","end-1c"))
        lösunge.append(lmn)
        lmn = []
        nn = []
    print(lösunge)
    lmn =[]
    
def tester():
    lösunge.clear()
    bs = []
    for hjk in range(0, 7):
        bs = []
        for jk in range(0, 12):
            bs.append("1000")
        lösunge.append(bs)
def anders():
    Hg.clear()
    temp12=[]
    temp12.clear()
    temp12 =lösunge[1]
    temp32 =[]
    temp32.clear()
    temp32 =lösunge[3]
    temp42=[]
    temp42.clear()
    temp42=lösunge[4]
    
    for zum in range(0,12):
        GV = float(temp12[zum])
        WB = float(temp42[zum])
        EV = float(temp32[zum])
        Hg.append(EV+(GV-EV)/(WBrenn*WProd)+(WB-((GV-EV)/WBrenn*WPB+(GV-EV)/(WProd*WBrenn)*WPE))/(COP*WBrenn*WProd+WPB*WProd+WPE))
    print(Hg)
def darstellung():
    j1 = []
    j12 = []
    j19 =0
    j20 =0
    j12 = lösunge[2]
    j13 = 0
    j14 = 0
    j2 = Tk("Ergebnis")
    j2.title("Ergebnis")
    Label(j2,text="Monat:").grid(column=1,row=1)
    Label(j2, text="Stromverbraucht:").grid(column=2,row=1)
    Label(j2, text="Solarstrom produziert:").grid(column=3, row =1)
    j9 = ["Januar","Februar","März","April","Mai","Juni","Juli","August",
          "September","Oktober","November", "Dezember","Summe:","Autarkie","Größe Wasserstofftank:",
          "Größe der benötigten Solarfläche","Größe des Wasserstofftankes bei Autarkie"]    
    for j in range(0, 12):
        j13 = j13 + round(Hg[j], 2)
        if (j19 < Hg[j]):
            j19 = Hg[j]
        j3 = Label(j2, text=str(int(Hg[j])))
        j3.grid(row = 2+j,column=2)
        j1.append(j3)
        
    for j4 in range(0, 12):
        j14 = j14+ int(j12[j4])
        if (int(j20) < int(j12[j4])):
            j20 = j12[j4]
        j15 = Label(j2, text=str(j12[j4]))
        j15.grid(column=3, row=2+j4)
        j1.append(j15)
    
    for j8 in range(0,len(j9)):
        j10 = Label(j2,text=j9[j8])
        j10.grid(row=2+j8, column=1)
        j1.append(j8)
    Label(j2,text=str(round(j13))).grid(row=14, column= 2)
    Label(j2,text=str(round(j14,2 ))).grid(row=14,column=3)
    Label(j2,text=str(round(j14/j13,2))).grid(row=15,column=2)
    Label(j2, text = str(round((((float(j20)/(2.77/10000000))/(120*1000000)))/40.3,4))).grid(row=16,column=2)
    Label(j2, text = str(round((((float(j19)/(2.77/10000000))/(120*1000000)))/40.3,4))).grid(row=18,column=2)
    Label(j2, text= str(round( int(textpn.get("1.0","end-1c"))  / ( (j14/j13)*100)*100,2))).grid(column=2,row=17)
def berechnen():
    Auslesen()
    anders()
    darstellung()
def berechnen2():
    Auslesen()
    tester()
    anders()
    darstellung()
#########################Wirkungsgrade##################
def wöffnen():
    wöffnenwin=Tk("Wirkungsgrade")
    
    WkSpeicher=Label(wöffnenwin, text="Wirkungsgrad im speichern:")
    WkSpeicher.grid(row=1,column=1)
    global WkSpeichert
    WkSpeichert=Text(wöffnenwin,height=1,width=10)
    WkSpeichert.grid(row=1, column=2)
    WkSpeichert.insert(INSERT, str(WkSpeicherz))
    
    WkProd=Label(wöffnenwin, text="Wirkungsgrad im produzieren:")
    WkProd.grid(row=2, column=1)
    global WkProdt
    WkProdt=Text(wöffnenwin,height=1,width=10)
    WkProdt.grid(row=2, column =2)
    WkProdt.insert(INSERT, str(WkProdz))
    
    WkHeiz=Label(wöffnenwin,text="Wirkungsgrad Heitzung:")
    WkHeiz.grid(row=3,column=1)
    global WkHeizt
    WkHeizt=Text(wöffnenwin,height=1,width=10)
    WkHeizt.grid(row=3,column=2)
    WkHeizt.insert(INSERT, str(WkHProdz))
                               
    WkSolar=Label(wöffnenwin, text="Wirkungsgrad der Solaranlagen:")
    WkSolar.grid(row=4,column=1)
    global WkSolart
    WkSolart=Text(wöffnenwin,height=1,width=10)
    WkSolart.grid(row=4,column=2)
    WkSolart.insert(INSERT, str(WkSolarz))

    Label(wöffnenwin,text="Wärmewirkungsgrad Brennstoffzelle").grid(row=5,column=1)
    global WkWBrenn
    WkWBrenn=Text(wöffnenwin,height=1,width=10)
    WkWBrenn.grid(row=5,column=2)
    WkWBrenn.insert(INSERT, str(WPB))

    Label(wöffnenwin,text="Wärmewirkungsgrad Elektrolyseur").grid(row=6,column=1)
    global WkWElek
    WkWElek=Text(wöffnenwin,height=1,width=10)
    WkWElek.grid(row=6,column=2)
    WkWElek.insert(INSERT, str(WPE))
                               
    WkSpeichern=Button(wöffnenwin,text="Eingeben",command=ändern)
    WkSpeichern.grid(row=7,column=1)
    
def ändern():
    global WkSpeicherz,WkProdz,WkHProdz,WkSolarz,WPE,WPB
    WkSpeicherz = float(WkSpeichert.get("1.0","end-1c"))
    WkProdz = float(WkProdt.get("1.0","end-1c"))
    WkHProdz = float(WkHeizt.get("1.0","end-1c"))
    WkSolarz = float(WkSolart.get("1.0","end-1c"))
    WPE = float(WkWElek.get("1.0","end-1c"))
    WPB = float(WkWBrenn.get("1.0","end-1c"))
#####################TK-Setup#########################
root=Tk()
root.title("Wasserstoffautarkie Rechner")
#####################Monate###########################
labeljan=Label(root, text="Januar")
labeljan.grid(row=2, column=1)
labelfeb=Label(root, text="Februar")
labelfeb.grid(row=3, column=1)
labelma=Label(root, text="März")
labelma.grid(row=4, column=1)
labelap=Label(root, text="April")
labelap.grid(row=5, column=1)
labelmai=Label(root, text="Mai")
labelmai.grid(row=6, column=1)
labeljun=Label(root, text="Juni")
labeljun.grid(row=7, column=1)
labeljul=Label(root, text="Juli")
labeljul.grid(row=8, column=1)
labelaug=Label(root, text="August")
labelaug.grid(row=9, column=1)
labelok=Label(root, text="Oktober")
labelok.grid(row=10, column=1)
labelsep=Label(root, text="September")
labelsep.grid(row=11, column=1)
labelnov=Label(root, text="November")
labelnov.grid(row=12, column=1)
labeldez=Label(root, text="Dezember")
labeldez.grid(row=13, column=1)
#####################Kategorien#######################
label1=Label(root, text="Monat:")
label1.grid(row=1, column=1)
labelSV=Label(root, text="Stromverbrauch:")
labelSV.grid(row=1, column=2)
labelSP=Label(root, text="Solaranlage Produziert:")
labelSP.grid(row=1, column=3)
LabelEV=Label(root, text="Eigenverbrauch Solar:")
LabelEV.grid(row=1, column=4)
labelHZ=Label(root, text="Heitzverbrauch:")
labelHZ.grid(row=1, column=5)
Labelpn =Label(root, text="Größe der Solarfläche:")
Labelpn.grid(row=1, column=6)
global textpn
textpn = Text(root, height=1,width=10)
textpn.grid(row= 2, column= 6)
Labelppn = Label(root, text= "Mögliche Solarflächengröße:")
Labelppn.grid(row= 3, column=6)
textppn = Text(root, height=1,width=10)
textppn.grid(row= 4, column= 6)
#####################Ausfüllen######################
for xi in range(0, zahlkategorien):
    for x in range(0, 12): 
        text = Text(root,height=1,width=10)
        text.grid(row=x+Startxtext, column= xi+1+Startytext)
        labels.append(text)
        op=x
        ll.append(text)
    zweid.append(ll)
    ll =[]
lp = []
lp = zweid[1]
#########################Knöpfe#####################
buttonberechnen=Button(root, text="Autarkie berechnen(mit aktueller Solarfläche)",command=berechnen)
buttonberechnen.grid(row=14, column= 1)
buttonheizung=Button(root, text="Monatlicher Heitzverbrauch", command=heiz)
buttonheizung.grid(row= 14, column= 2)
buttonberechen2= Button(root, text="Autarkie berechnen(mit max Solarfläche)",command=berechnen2)
buttonberechen2.grid(row=14, column = 3)
buttonWgrade=Button(root, text="Wirkungsgrade öffnen",command=wöffnen)
buttonWgrade.grid(row=14, column=4)
####################mainloop########################
root.mainloop()
