# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:14:02 2024

@author: dmr_2
"""

import tkinter as tk 
import tkinter.ttk as ttk


pen=tk.Tk()
pen.geometry("620x450")
pen.title("SUDOKU")


# BASLİK
lbl=tk.Label(text="    SUDOKU ÇÖZELİM ",font="Arial 18 bold")
lbl.place(x=51,y=11)#(row=5,column=1)

satır=[]
x=[]
tekMi=True  #her bir sorgu için küme benzersiz 9 elemanlı olacak 
# satırları oluşturacak girişler
def forma_ciz():
    
    for i in range(9):
        satır.append([tk.Entry(width=4,text="") for i in range(9)])
        
    # forma yerleştir
    x=20 ; y=50 ; a=25  ; b=35
    for j in range(9):
        if j%3==0: y+=10
        else: a=30
        for k in range(9):
            if k%3==0:  #hücreler arası boşluk 
                x+=20
                satır[j][k].place(x=x+k*b,y=y+j*a)#grid(row=j+2,column=k+1,padx=5,pady=5) #pack(side="left",padx=5,anchor="n")
            else: 
                satır[j][k].place(x=x+k*b,y=y+j*a)#grid(row=j+2,column=k+1,padx=5,pady=5) #pack(side="left",padx=5,anchor="n")
        x=20
forma_ciz()

# sutunlar 
sutunlar=[]
def sutun_val():
    global sutunlar
    m=[]
    for i in range(9):
        for j in range(9):
            m.append(satır[j][i].get())
        sutunlar.append(m)
        m=[]
# print(sutunlar)

# deneme için 
# giris=tk.Entry()
# giris.place(x=200, y=200)      
# val=giris.get()      

lbl2=tk.Label()
lbl2.place(y=300)


#satır değerleri 
satırValues=[] ; 

def satırVal(): 
    global satırValues
    sat=[]
    for i in range(9):
        for j in range(9):
            s=satır[i][j].get()
            if s!="" and len(s)==1 and s is  str.isalpha(s) :
                print("girdi")
                # sat.append(s)
            sat.append(satır[i][j].get())
        satırValues.append(sat)
        # print(satırValues)
        sat=[]
        

# hucreler değer   # 


valSet=set()


lbl_eksik=tk.Label(text="Veri Durumu ",bg="#fda",font="Arial 14 italic")
lbl_eksik.place(x=400,y=55)

hucreVal=[]
hucreler=[]
def hucre_val():
    global tekMi , lbl_eksik
    global hucreler
    h1=[]; h2=[]; h3=[]
    for i in range(9):
        h1+=satır[i][0:3]
        h2+=(satır[i][3:6])
        h3+=(satır[i][6:9])
        if (i+1)%3==0:
            hucreler.append(h1)
            hucreler.append(h2)
            hucreler.append(h3)
            h1=[] ; h2=[]; h3=[]
    # print(hucreler) 
    lbl_eksik["text"]="Veri Durumu "
    for i in hucreler:
        for j in i:
            if j.get()=="" or len(j.get())>1 or str.isalpha(j.get()): #boş hucre kontrolu 
                j["bg"]="yellow"
                lbl_eksik["text"]="EKSİK VERİ VAR!!!\nSarı alanlar boş bırakılmış"
               
                # print("eksik veri var ")
            else: 
                valSet.add(j.get())
                lbl_eksik["text"]+="Veri girilmemiş hücre yok"
        print(len(valSet))
        # print(valSet)
        if len(valSet)!=9:
            # print("değil")
            tekMi=False
        valSet.clear()
    print("tek mi hucre",tekMi)
            # print(tekMi)

def satir_val_kontrol():
    global tekMi
    # print("satırValues",satırValues)
    for i in satırValues:
        # print(i)
        if len(set(i))!=9:
            tekMi=False
    print("tek mi satır",tekMi)
def sutun_val_kontrol():
    global tekMi
    for i in sutunlar:
        if len(set(i))!=9:
            tekMi=False
                
    print("tek mi sutun",tekMi)
            
        
            
# satir_val_kontrol()            
             
lbl2=tk.Label(text="SONUÇ:",bg="#da1",font="Arial 14 bold")
lbl2.place(x=400,y=120)        
def kontrol():
    global tekMi
    print("kontrol ")    
    hucre_val()
    satırVal()
    sutun_val()
    satir_val_kontrol()
    sutun_val_kontrol()
    lbl2["text"]="SONUÇ:" #BİR KAÇ KEZ KONTROL BUT. TIKLAYINCA DÜZELTME İÇİN
    if tekMi: 
        lbl2["text"]+=("\n\nTEBRİKLER....")
        lbl2["bg"]="green"
        forma_ciz()
    else: 
        lbl2["text"]+="\n\nÇÖZÜM HATALI "
        lbl2["bg"]="pink"
        forma_ciz()
    

btn_kontrol=tk.Button(text="Kontrol et",command=kontrol,font="Arial 14 bold",bg="#ac3")
btn_kontrol.place(x=120,y=355,width=212,height=40,)
       
# hucre_val()           
            
        
sp=ttk.Separator(pen,orient="vertical")
sp.grid()



pen.mainloop()


