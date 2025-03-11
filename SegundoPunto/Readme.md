# Segundo Punto 

# Chat con Servidor y Clientes en Python usando Sockets y Tkinter

Este proyecto implementa un **chat basado en sockets TCP** en Python, donde múltiples clientes pueden conectarse a un servidor y comunicarse entre sí. Cada cliente ingresa su nombre antes de conectarse, y el servidor confirma la recepción de los mensajes.

## 📌 Características
- **Servidor en el puerto 2010** que acepta múltiples clientes.
- **Cada cliente ingresa su nombre** antes de conectarse.
- **Los mensajes son transmitidos a todos los clientes conectados.**
- **El servidor envía una confirmación** a cada cliente tras recibir su mensaje.
- **Interfaz gráfica (GUI) con Tkinter** para una experiencia de chat amigable.

---


## 🖥️ Código del Servidor (`server.py`)
```python
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = "0.0.0.0"
PORT = 2010

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
clientes = {}

def manejar_cliente(cliente_socket, direccion):
    try:
        nombre = cliente_socket.recv(1024).decode("utf-8")
        clientes[cliente_socket] = nombre
        actualizar_chat(f"{nombre} ({direccion}) se ha conectado.")
        enviar_a_todos(f"{nombre} se ha unido al chat.")
        while True:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            if not mensaje:
                break
            actualizar_chat(f"{nombre}: {mensaje}")
            cliente_socket.sendall(f"Servidor: Mensaje recibido, {nombre}.".encode("utf-8"))
            enviar_a_todos(f"{nombre}: {mensaje}", emisor=cliente_socket)
    except:
        pass
    actualizar_chat(f"{nombre} se ha desconectado.")
    enviar_a_todos(f"{nombre} ha salido del chat.")
    del clientes[cliente_socket]
    cliente_socket.close()

def enviar_a_todos(mensaje, emisor=None):
    for cliente in clientes.keys():
        if cliente != emisor:
            try:
                cliente.sendall(mensaje.encode("utf-8"))
            except:
                cliente.close()
                del clientes[cliente]

def actualizar_chat(mensaje):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, mensaje + "\n")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

ventana = tk.Tk()
ventana.title("Servidor Chat")
chat = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, width=50, height=20)
chat.pack()

def aceptar_conexiones():
    while True:
        cliente_socket, direccion = server_socket.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
        hilo.start()

hilo_servidor = threading.Thread(target=aceptar_conexiones, daemon=True)
hilo_servidor.start()
ventana.mainloop()
```

### **Explicación del Servidor**
- Inicia un servidor en el **puerto 2010**.
- Maneja múltiples clientes simultáneamente con **hilos**.
- Recibe el **nombre del cliente** al conectarse.
- **Envía confirmación** tras recibir un mensaje.
- **Notifica a todos** cuando un cliente envía un mensaje o se desconecta.
- Usa **Tkinter** para mostrar mensajes en una interfaz gráfica.

---

## 🖥️ Código del Cliente (`client.py`)
```python
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

SERVER_IP = '127.0.0.1'
PORT = 2010

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((SERVER_IP, PORT))

ventana_nombre = tk.Tk()
ventana_nombre.withdraw()
nombre = simpledialog.askstring("Nombre", "Ingresa tu nombre:")

cliente_socket.sendall(nombre.encode("utf-8"))

def recibir_mensajes():
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if not mensaje:
                break
            actualizar_chat(mensaje)
        except:
            break

def enviar_mensaje():
    mensaje = entrada_mensaje.get()
    if mensaje:
        cliente_socket.sendall(mensaje.encode('utf-8'))
        entrada_mensaje.delete(0, tk.END)

def actualizar_chat(mensaje):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, mensaje + "\n")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

ventana = tk.Tk()
ventana.title(f"Chat - {nombre}")
chat = scrolledtext.ScrolledText(ventana, state=tk.DISABLED, width=50, height=20)
chat.pack()

entrada_mensaje = tk.Entry(ventana, width=40)
entrada_mensaje.pack()

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

hilo_recepcion = threading.Thread(target=recibir_mensajes, daemon=True)
hilo_recepcion.start()
ventana.mainloop()
cliente_socket.close()
```

### **Explicación del Cliente**
- Solicita al usuario **su nombre** antes de conectarse.
- Se conecta al servidor en el **puerto 2010**.
- Envía y recibe mensajes de forma continua en un **hilo separado**.
- Muestra los mensajes en una **interfaz gráfica con Tkinter**.

---

## 📜 Demostracion del codigo en accion 

Este proyecto se desarrollo en conjunto buteando 5 pc de el salon F403 y conectando el proyector para usar ese pc como servidor y poder visualizar de manera mas sencilla lo que entra y sale del servidor .

![Ejemplo de imagen](src/Salon1.jpeg)

---

