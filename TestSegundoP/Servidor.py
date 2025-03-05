import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Configuración del servidor
HOST = "0.0.0.0"
PORT = 7070

# Creación del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clientes = []  # Lista de clientes conectados

# Función para manejar cada cliente
def manejar_cliente(cliente_socket, direccion):
    clientes.append(cliente_socket)
    actualizar_chat(f"Cliente conectado desde {direccion}")

    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            if not mensaje:
                break
            actualizar_chat(f"{direccion} dice: {mensaje}")
            enviar_a_todos(f"Cliente {direccion}: {mensaje}")
        except:
            break

    actualizar_chat(f"Cliente {direccion} desconectado")
    clientes.remove(cliente_socket)
    cliente_socket.close()

# Función para enviar mensajes a todos los clientes
def enviar_a_todos(mensaje):
    for cliente in clientes:
        try:
            cliente.sendall(mensaje.encode("utf-8"))
        except:
            clientes.remove(cliente)

# Función para enviar mensajes desde la interfaz
def enviar_mensaje():
    mensaje = entrada_mensaje.get()
    if mensaje:
        actualizar_chat(f"Servidor: {mensaje}")
        enviar_a_todos(f"Servidor: {mensaje}")
        entrada_mensaje.delete(0, tk.END)

# Función para actualizar la interfaz con nuevos mensajes
def actualizar_chat(mensaje):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, mensaje + "\n")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Servidor Chat")

chat = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, width=50, height=20)
chat.pack()

entrada_mensaje = tk.Entry(ventana, width=40)
entrada_mensaje.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

# Hilo para aceptar conexiones
def aceptar_conexiones():
    while True:
        cliente_socket, direccion = server_socket.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
        hilo.start()

hilo_servidor = threading.Thread(target=aceptar_conexiones, daemon=True)
hilo_servidor.start()

ventana.mainloop()
