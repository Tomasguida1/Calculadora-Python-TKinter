#importamos todos los módulos de tkinter

from tkinter import *

#modulo que inicia la ventana
root = Tk()

#establecemos el titulo
root.title  ("calculadora")


#muestra una caja de texto para ingresar los numeros 
display = Entry(root)
display.grid(row = 1 , columnspan = 6, sticky = W + E)

#hace que no se pueda cambiar el tamaño
root.resizable(False, False)

i = 0
    
#obtiene los numeros que se ingresan
def get_num (n):
    global i
    display.insert(i ,n)
    i += 1
#para obtener la operacion que se va a realizar

def get_ope(op):
    global i
    larg = len(op)
    display.insert (i, op)
    i += larg
    
#borra todo el contenido en pantalla   
def clear_disp():
    display.delete(0, END)

#borra un espacio, como la tecla back del teclado    
def borrar():
    display.state = display.get()
    if len(display.state) :
        display_new_state = display.state[:-1]
        clear_disp()
        display.insert (0, display_new_state)
    else:
        clear_disp()
        display.insert(0, 'Error')

#calcula el resultado de la operación, al tocar al boton =
def calcular():
    borrar = display.get()
    try:
     result = eval(borrar)
     clear_disp()
     display.insert(0, result)
    except Exception:
     clear_disp()
     display.insert(0, 'Error')



    
    
#botones
Button(root, text = "7", command=lambda: get_num(7)).grid(row = 2 , column = 0 ,sticky = W + E)
Button(root, text = "8", command=lambda: get_num(8)).grid(row = 2 , column = 1 ,sticky = W + E)
Button(root, text = "9", command=lambda: get_num(9)).grid(row = 2 , column = 2 ,sticky = W + E)
Button(root, text = "DEL", command=lambda:borrar()).grid(row = 2 , column = 3 ,sticky = W + E)
Button(root, text = "AC", command=lambda: clear_disp()).grid(row = 2 , column = 4 ,sticky = W + E)


Button(root, text = "4", command=lambda: get_num(4)).grid(row = 3 , column = 0 ,sticky = W + E)
Button(root, text = "5", command=lambda: get_num(5)).grid(row = 3 , column = 1 ,sticky = W + E)
Button(root, text = "6", command=lambda: get_num(6)).grid(row = 3 , column = 2 ,sticky = W + E)
Button(root, text = "X", command=lambda: get_ope("*")).grid(row = 3 , column = 3 ,sticky = W + E)
Button(root, text = "÷", command=lambda: get_ope("/")).grid(row = 3 , column = 4 ,sticky = W + E)


Button(root, text = "1", command=lambda: get_num(1)).grid(row = 4 , column = 0 ,sticky = W + E)
Button(root, text = "2", command=lambda: get_num(2)).grid(row = 4 , column = 1 ,sticky = W + E)
Button(root, text = "3", command=lambda: get_num(3)).grid(row = 4 , column = 2 ,sticky = W + E)
Button(root, text = "+", command=lambda: get_ope("+")).grid(row = 4 , column = 3 ,sticky = W + E) 
Button(root, text = "-", command=lambda: get_ope("-")).grid(row = 4 , column = 4 ,sticky = W + E)
Button(root, text = "0", command=lambda: get_num(0)).grid(row = 4 , column = 4 ,sticky = W + E)


Button(root, text = ".", command=lambda: get_num(".")).grid(row = 5 , column = 0 ,sticky = W + E)
Button(root, text = "=", command=lambda: calcular()).grid(row = 5 , column = 1 ,sticky = W + E)
Button(root, text = "√", command=lambda: get_ope("** (0.5)")).grid(row = 5 , column = 2 ,sticky = W + E)
Button(root, text = "^2", command=lambda: get_ope("*2")).grid(row = 5 , column = 3 ,sticky = W + E)
Button(root, text = "%", command=lambda: get_ope("%")).grid(row = 5 , column = 4 ,sticky = W + E)

root.mainloop()


