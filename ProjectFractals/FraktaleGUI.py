import turtle
from math import sqrt
import tkinter as tk
import random
glowne = tk.Tk()
glowne.geometry('800x643')
glowne.configure(bg='#7AC5CD')
zolw=tk.Canvas(glowne,width=800,height=500)
#zolw=turtle.ScrolledCanvas(glowne,width=800,height=470) #drugi sposób na canvas ze scrollem
t=turtle.RawTurtle(zolw)
class Fraktale:
    def wektor(self,A,B):
        return B[0]-A[0],B[1]-A[1]
    def punkt(self,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot(3,'blue')
    def kwadrat(self,dl,x=0,y=0):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.fd(dl)
            t.left(90)
        t.end_fill()
    def trojkat(self,dl,x=0,y=0):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.begin_fill()
        for i in range(3):
            t.fd(dl)
            t.left(120)
        t.end_fill()
    def dywansierp(self,dl,st,x=-250,y=-250):
        if st==0:
            self.kwadrat(dl,x,y)
        else:
            self.dywansierp(dl/3,st-1,x,y)
            self.dywansierp(dl/3,st-1,x+dl/3,y)
            self.dywansierp(dl/3,st-1,x+dl*2/3,y)
            self.dywansierp(dl/3,st-1,x+dl*2/3,y+dl/3)
            self.dywansierp(dl/3,st-1,x+dl*2/3,y+dl*2/3,)
            self.dywansierp(dl/3,st-1,x+dl/3,y+dl*2/3)
            self.dywansierp(dl/3,st-1,x,y+dl*2/3)
            self.dywansierp(dl/3,st-1,x,y+dl/3,)
    def trsierp(self,dl,st,x=-300,y=-250):
        if st==0:
            self.trojkat(dl,x,y)
        else:
            self.trsierp(dl/2,st-1,x,y)
            self.trsierp(dl/2,st-1,x+dl/2,y)
            self.trsierp(dl/2,st-1,x+dl/4,y+(dl*sqrt(3))/4)
    def grawchaos(self,dl,ile):
        A=(dl*(-1),dl*(-1))
        B=(dl,dl*(-1))
        C=(0,dl)
        tab=[A,B,C]
        D=(random.randint(0,250),random.randint(0,250))
        for i in range(ile):
            ran=random.randint(0,2)
            N=(tab[ran][0],tab[ran][1])
            wek=self.wektor(N,D)
            sr=(N[0]+(wek[0]/2),N[1]+(wek[1]/2))
            if i>15:
                self.punkt(sr[0],sr[1])
            D=sr

    def koha(self,dl,st):
        if st==0:
            t.fd(dl)
        else:
            self.koha(dl/3,st-1)
            t.left(60)
            self.koha(dl/3,st-1)
            t.right(120)
            self.koha(dl/3,st-1)
            t.left(60)
            self.koha(dl/3,st-1)
    def platkoha(self,dl,st,kat):
        for i in range(360//kat):
            self.koha(dl,st)
            t.right(kat)
    def drew1(self,dl,st,kat):
        if st==0:
            t.dot(5)
        else:
            t.fd(dl)
            t.right(kat)
            t.fd(dl/2)
            self.drew1(dl*0.7,st-1,kat)
            t.bk(dl/2)
            t.left(kat*2)
            t.fd(dl/2)
            self.drew1(dl*0.7,st-1,kat)
            t.bk(dl/2)
            t.right(kat)
            t.bk(dl)
    def drew(self,dl,st,kat):
        t.left(90)
        self.drew1(dl,st,kat)
    def ccurve(self,dl,st):
        if st==0:
            t.fd(dl)
        else:
            self.ccurve(dl/2,st-1)
            t.left(90)
            self.ccurve(dl/2,st-1)
            t.right(90)
    def ccurve2(self,dl,st):
        if st==0:
            t.fd(dl)
        else:
            self.ccurve2(dl/2,st-1)
            t.left(90)
            self.ccurve2(dl/2,st-1)
            t.left(90)
    def gosper(self,dl,st,tr='A'):
        if st==0:
            t.fd(dl)
        elif tr=='A':
            self.gosper(dl/2,st-1,'A')
            t.right(60)
            self.gosper(dl/2,st-1,'B')
            t.right(120)
            self.gosper(dl/2,st-1,'B')
            t.left(60)
            self.gosper(dl/2,st-1,'A')
            t.left(120)
            self.gosper(dl/2,st-1,'A')
            self.gosper(dl/2,st-1,'A')
            t.left(60)
            self.gosper(dl/2,st-1,'B')
            t.right(60)
        elif tr=='B':
            t.left(60)
            self.gosper(dl/2,st-1,'A')
            t.right(60)
            self.gosper(dl/2,st-1,'B')
            self.gosper(dl/2,st-1,'B')
            t.right(60)
            t.right(60)
            self.gosper(dl/2,st-1,'B')
            t.right(60)
            self.gosper(dl/2,st-1,'A')
            t.left(60)
            t.left(60)
            self.gosper(dl/2,st-1,'A')
            t.left(60)
            self.gosper(dl/2,st-1,'B')
    def cantor(self,dl,st,dl2,x=0,y=0):
        if st==0:
            t.fd(dl)
        else:
            t.fd(dl)
            t.penup()
            t.goto(x,y-dl2)
            t.pendown()
            self.cantor(dl/3,st-1,dl2,x,y-dl2)
            t.penup()
            t.goto(x+2*dl/3,y-dl2)
            t.pendown()
            self.cantor(dl/3,st-1,dl2,x+2*dl/3,y-dl2)

Frak=Fraktale()
#Ustawienia Turtla
UstTur=tk.LabelFrame(glowne,text='Ustawienia Turtla',bg='#5F9EA0')
tabco=['black','red','blue','green','fuchsia','white']
tabshape=['classic','arrow','turtle','circle','square','ukryj']
colo=tk.StringVar()
shap=tk.StringVar()
tlo=tk.StringVar()
wid=tk.Entry(UstTur,width=5,bg='#5F9EA0')
def SetTur():
    global colo
    global wid
    global shap
    global tlo
    ksz=shap.get()
    color=colo.get()
    tlolo=tlo.get()
    if tlo.get()=='':
        tlolo='white'
    if shap.get()=='':
        ksz='classic'
    if colo.get()=='':
        color='Black'
    wide=wid.get()
    if wid.get()=='':
        wide=1
    t.pencolor(color)
    t.pensize(wide)
    if ksz=='ukryj':
        t.hideturtle()
    else:
        t.showturtle()
        t.shape(ksz)
    t.screen.bgcolor(tlolo)
kolorki=tk.OptionMenu(UstTur,colo,*tabco)
tla=tk.OptionMenu(UstTur,tlo,*tabco)
ksztalty=tk.OptionMenu(UstTur,shap,*tabshape)
ksztalty.configure(bg='#5F9EA0')
kolorki.configure(bg='#5F9EA0')
tla.configure(bg='#5F9EA0')
UstTur.place(x=600,y=505)
kolorki.grid(column=1,row=0)
Save=tk.Button(UstTur,text='Zapisz',command=SetTur,bg='#5F9EA0')
tla.grid(column=1,row=2)
wid.grid(column=1,row=3)
ksztalty.grid(column=1,row=1)
lwid=tk.Label(UstTur,text='Grubość:',bg='#5F9EA0')
lksz=tk.Label(UstTur,text='Kształt:',bg='#5F9EA0')
lkol=tk.Label(UstTur,text='Kolor:',bg='#5F9EA0')
ltlo=tk.Label(UstTur,text='Tło:',bg='#5F9EA0')
lwid.grid(column=0,row=3)
lksz.grid(column=0,row=1)
lkol.grid(column=0,row=0)
ltlo.grid(column=0,row=2)
Save.grid(column=2,row=3)




#Frame z wartościami
VarFrame=tk.Frame(glowne)
st=tk.Entry(VarFrame,width=5)
dl=tk.Entry(VarFrame,width=5)
extra=tk.Entry(VarFrame,width=5)
lstop=tk.Label(VarFrame,text='Stopień:',bg='#5F9EA0')
lwiel=tk.Label(VarFrame,text='Wielkość:',bg='#5F9EA0')
lextra=tk.Label(VarFrame,text='Extra:',bg='#5F9EA0')
dstop=tk.Label(VarFrame,text='Def. 3',bg='#5F9EA0')
dwiel=tk.Label(VarFrame,text='Def. 400',bg='#5F9EA0')
dextra=tk.Label(VarFrame,text='Def. 0',bg='#5F9EA0')
lstop.grid(column=0,row=0)
lwiel.grid(column=0,row=1)
lextra.grid(column=0,row=2)
st.grid(column=1,row=0)
dl.grid(column=1,row=1)
extra.grid(column=1,row=2)
dstop.grid(column=2,row=0)
dwiel.grid(column=2,row=1)
dextra.grid(column=2,row=2)
VarFrame.configure(bg='#5F9EA0')
VarFrame.place(x=0,y=570)



def tele(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def zawsze():
    global valuetrac
    t.screen.tracer(int(valuetrac.get()))
    t.reset()
    SetTur()
def OdpalCantor(dl,st,extra):
    zawsze()
    xx=dl//2*(-1)
    tele(xx,0)
    Frak.cantor(dl,st,x=xx,dl2=30+extra)
def OdpalTrojSierp(dl,st):
    zawsze()
    xx=dl//2*(-1)
    Frak.trsierp(dl,st,x=xx,y=xx+40)
def OdpalGosper(dl,st):
    zawsze()
    dl=dl//4
    xx=dl//2*(-1)
    tele(xx,150)
    Frak.gosper(dl,st)
def OdpalDywan(dl,st):
    xx=dl//2*(-1)
    zawsze()
    Frak.dywansierp(dl,st,x=xx,y=xx)
def OdpalKKoha(dl,st):
    zawsze()
    xx=dl//2*(-1)
    tele(xx,0)
    Frak.koha(dl,st)
def OdpalPKoha(dl,st,extra):
    zawsze()
    dl=dl//3
    xx=dl//2
    tele(xx*(-1),xx*1.5)
    Frak.platkoha(dl,st,60+extra)
def OdpalDBinarne(dl,st,extra):
    zawsze()
    tele(0,-200)
    dl=dl//5
    Frak.drew(dl,st,30+extra)
def OdpalCcurve1(dl,st):
    zawsze()
    dl=dl+dl*(st-3)
    Frak.ccurve(dl,st)
def OdpalCcurve2(dl,st):
    zawsze()
    dl=dl+dl*(st-3)
    Frak.ccurve2(dl,st)
def OdpalGra(dl,extra):
    zawsze()
    dl=dl//2
    Frak.grawchaos(dl,3000+extra)


#Menu Fraktali
def menu(dl,st,extra):
    if dl=='':
        dl=400
    if st=='':
        st=3
    if extra=='':
        extra=0
    dl=int(dl)
    st=int(st)
    extra=int(extra)
    global wybor
    if wybor.get()== 'Trójkąt Sierpińskiego':
        OdpalTrojSierp(dl,st)
    elif wybor.get()== 'Krzywa Gospera':
        OdpalGosper(dl,st)
    elif wybor.get()== 'Zbiór Cantora':
        OdpalCantor(dl,st,extra)
    elif wybor.get()== 'Dywan Sierpińskiego':
        OdpalDywan(dl,st)
    elif wybor.get()== 'Krzywa Koha':
        OdpalKKoha(dl,st)
    elif wybor.get()== 'Platek Koha':
        OdpalPKoha(dl,st,extra)
    elif wybor.get()== 'Drzewo Binarne':
        OdpalDBinarne(dl,st,extra)
    elif wybor.get()== 'Ccurve (ver1)':
        OdpalCcurve1(dl,st)
    elif wybor.get()== 'Ccurve (ver2)':
        OdpalCcurve2(dl,st)
    elif wybor.get()== 'Gra w Chaos':
        OdpalGra(dl,extra)
    else:
        print('nic nie wybrano')
#Frame z generacją
FrameFrak=tk.Frame(glowne)
OdpalMenu=tk.Button(FrameFrak, text='Rysuj Fraktal',command=lambda: menu(dl.get(),st.get(),extra.get()),bg='#5F9EA0')
opcje=['Trójkąt Sierpińskiego','Dywan Sierpińskiego','Krzywa Koha','Platek Koha','Drzewo Binarne','Zbiór Cantora','Ccurve (ver1)','Ccurve (ver2)','Krzywa Gospera','Gra w Chaos']
wybor=tk.StringVar()
MenuFrak=tk.OptionMenu(FrameFrak,wybor,*opcje)
MenuFrak.config(bg='#5F9EA0',border=0,activebackground='#5F9EA0')
MenuFrak.grid(column=0,row=0)
OdpalMenu.grid(column=1,row=0)
FrameFrak.configure(bg='#7AC5CD')
FrameFrak.place(x=0,y=505)

#tracer(0) guzik
valuetrac=tk.IntVar()
TracerSwitch=tk.Checkbutton(glowne,text='Wyświetlaj odrazuj [aka: tracer(0)]',onvalue=0,offvalue=1,variable=valuetrac,selectcolor='#53868B',bg='#5F9EA0')
TracerSwitch.deselect()
TracerSwitch.place(x=0,y=535)

#Co to extra
def cte():
    global wybor
    if wybor.get() == '':
        opis=''
    elif wybor.get() == 'Zbiór Cantora':
        opis='Odstępy między liniami (30+Extra).'
    elif wybor.get() == 'Platek Koha':
        opis='Kąt zagięcia przy\n robieniu płatka (60+Extra).\nNajlepiej aby 360%(60+Extra)=0.'
    elif wybor.get() == 'Drzewo Binarne':
        opis='Kąt gałęzi (30+Extra).'
    elif wybor.get()== 'Gra w Chaos':
        opis='Ilość kropek (3000+Extra).'
    else:
        opis='Nic.\nRobi coś przy:\nZbiór Cantora, Platek Koha\nDrzewo Binarne, Gra w Chaos'
    return opis
ExtraFrame=tk.Frame(glowne)
ExtraFrame.configure(bg='#5F9EA0')
eopis=tk.StringVar()
bcte=tk.Button(ExtraFrame,text='Co robi Extra?',command=lambda: eopis.set(cte()),bg='#5F9EA0')
lcte=tk.Label(ExtraFrame,textvariable=eopis,bg='#5F9EA0')
nkpw=tk.Label(ExtraFrame,text='Kliknij po Wybraniu Fraktala:',bg='#5F9EA0')
nkpw.grid(column=0,row=0)
bcte.grid(column=0,row=1)
lcte.grid(column=0,row=2)
ExtraFrame.place(x=340,y=505)

zolw.pack()
glowne.mainloop()
