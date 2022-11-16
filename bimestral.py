import tkinter as t
from tkinter import messagebox
from matplotlib.pyplot import*
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from math import*
win= t.Tk()
win.title("NAYARITH ZAMBRANO GOMEZ")
win.geometry("700x700")
style.use("fivethirtyeight")
fig=Figure()
ax=fig.add_subplot(111)

# print(style.available)

cvs=FigureCanvasTkAgg(fig,win)
cvs.draw()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)
tlb=NavigationToolbar2Tk(cvs,win)
tlb.update()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)

rang1=False
rang2=""
rang3=""

fun={"sin":"np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","log":"np.log","pi":"np.pi"}

def reemplaza(p):
    for i in fun:
        if i in p:
            p=p.replace(i,fun[i])
        return p

def animate(i):
    global rang1
    global rang2
    if rang1==True:
        try:
            min=float(rang3[0]);max=float(rang3[1])
            if min<max:
                x=np.arange(min,max,0.01)
                rang2=[min,max]
            else:
                rang1=False
        except:
                messagebox.showwarning("El rango es incorrecto")
                rang1=False
                entra_var.delete(0,len(entra_var.get()))
        else:
            if rang2!="":
                x=np.arange(rang2[0],rang2[1],0.01)
            else:
                x=np.arange(0,10,0.01)
        try:
            sl=eval(graf_dt)
            ax.clear()
            ax.plot(x,sl)
        except:
            ax.plot()
        ax.axhline(0,color="green")
        ax.axvline(0,color="green")
        ani.event_source.stop()
def represent():
    global graf_dt
    global rang3
    global rang1
    tx_origl=entra_func.get()
    if entra_var.get()!="":
        rann=entra_var.get()
        rang3=rann.split(",")
        rang1=True
    graf_dt=reemplaza(tx_origl)
    ani.event_source.start()
ani=anim.FuncAnimation(fig,animate ,interval=100)
show()

bo1=t.Button(win,text="Graficar",command=represent)
entra_func=t.Entry(win,width=30)
entra_var=t.Entry(win,width=20)
bo1.pack(side=t.BOTTOM)
entra_var.pack(side=t.RIGHT)
entra_func.pack(side=t.BOTTOM)

win.mainloop()

