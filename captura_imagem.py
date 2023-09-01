import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def atualizar_coordenadas(event):
    x, y = event.x, event.y
    coordenadas = f"Coordenadas do Mouse\nX: {x}  Y: {y}"
    coordenadas_label.config(text=coordenadas)

# Configurar a interface gráfica
root = tk.Tk()
root.title("Visualizador de Imagem Capturada")

# Carregar a imagem capturada
imagem_capturada = Image.open("imagem_capturada_webcam.jpg")
img_capturada = ImageTk.PhotoImage(imagem_capturada)

# Configurar a imagem
label_imagem = ttk.Label(root, image=img_capturada)
label_imagem.pack(side="left")

# Configurar uma Label para a barra de coordenadas à esquerda
coordenadas_label = ttk.Label(root, text="Coordenadas do Mouse")
coordenadas_label.pack(side="left")

# Lidar com eventos de movimento do mouse na imagem
label_imagem.bind("<Motion>", atualizar_coordenadas)

root.mainloop()
