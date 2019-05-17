from tkinter import *

Ventana =Tk()
canvas = Canvas (Ventana, width = 600, height = 480)
canvas.pack()

x=200
y=170

cancha = PhotoImage(file = "cancha.gif")
canvas.create_image(0, 0, anchor = NW, image = cancha)

jugador = PhotoImage(file = "jugador.gif")
canvas.create_image(x, y, anchor = NW, image = jugador)

arco = PhotoImage(file = "arco.gif")
canvas.create_image(400, 205, anchor = NW, image = arco)


def moverjugador (event):

    global x

    if event.keysym =='Up':
        canvas.move(2,0,-3)
        
    elif event.keysym =='Down':
        canvas.move(2,0,3)
    elif event.keysym =='Left':
        canvas.move(2,-3,0)
        x-=3
    elif event.keysym =='Right':
        canvas.move(2,3,0)
        x+=3

    if x>=368:
        canvas.create_text(100,100, text="GOOOOOL...!!", anchor="nw", font= "Time 30 italic bold")
    
        
canvas.bind_all('<KeyPress-Up>', moverjugador )
canvas.bind_all('<KeyPress-Down>', moverjugador )
canvas.bind_all('<KeyPress-Left>', moverjugador )
canvas.bind_all('<KeyPress-Right>', moverjugador )




Ventana.mainloop()

