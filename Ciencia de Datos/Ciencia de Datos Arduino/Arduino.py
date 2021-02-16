#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:28:51 2021

@author: david
"""
import tkinter as tk
import serial 
import tk_tools

arduino=serial.Serial("/dev/ttyACM0(Arduino Uno)",9600)


def led_encendido():
    arduino.write(b'0')
    led.to_green(True)
    boton_encendido.config(state='disabled')
    boton_apagado.config(state='normal')
    
def led_apagado():
    arduino.write(b'1')
    led.to_green()
    boton_encendido.config(state='normal')
    boton_apagado.config(state='disabled')
    
def cerrar_ventana():
    arduino.close()#Corta la comunicación
    window.destroy()
    
window = tk.Tk()#Creando ventana
window.title("Control de Led")
window.configure(background="white")


boton_encendido = tk.Button(window,text="ON",font=('Verdana',16),padx=50,pady=20
                          ,bg='green',fg='white',command=led_encendido)

boton_apagado = tk.Button(window,text="OFF",font=('Verdana',16),padx=50,pady=20
                          ,bg='red',fg='white',command=led_apagado)

boton_cerrar = tk.Button(window,text="CLOSE",font=('Verdana',16),padx=130,pady=20
                          ,bg='orange',fg='white',command=cerrar_ventana)

boton_encendido.grid(row=1,column=1)
boton_apagado.grid(row=1,column=2)
boton_apagado.config(state='disabled')
boton_cerrar.grid(row=2,column=1,columnspan=2)


led = tk_tools.Led(window,size=100)
led.to_green()
led.grid(row=0,column=1,columnspan=2)


#Ejecutando ventana


window.mainloop()
