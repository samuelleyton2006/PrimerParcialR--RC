import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Configuración del cliente
SERVER_IP = '127.0.0.1'  # Dirección del servidor
PORT = 7070

# Creación del socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((SERVER_IP, PORT))

# Función para recibir mensajes
def recibir_mensajes():
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if not mensaje:
                break
            actualizar_chat(mensaje)
        except:
            break

# Función para enviar mensajes desde la interfaz
def enviar_mensaje():
    mensaje = entrada_mensaje.get()
    if mensaje:
        cliente_socket.sendall(mensaje.encode('utf-8'))
        entrada_mensaje.delete(0, tk.END)

# Función para actualizar la interfaz con nuevos mensajes
def actualizar_chat(mensaje):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, mensaje + "\n")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Cliente Chat")

chat = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, width=50, height=20)
chat.pack()

entrada_mensaje = tk.Entry(ventana, width=40)
entrada_mensaje.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

# Hilo para recibir mensajes
hilo_recepcion = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_recepcion.start()

ventana.mainloop()
cliente_socket.close()
