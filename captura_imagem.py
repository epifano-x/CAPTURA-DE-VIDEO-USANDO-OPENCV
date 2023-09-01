import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Função para atualizar as coordenadas
def atualizar_coordenadas(event):
    x, y = event.x, event.y
    coordenadas = f"Coordenadas do Mouse\nX: {x}  Y: {y}"
    coordenadas_label.config(text=coordenadas)

# Função para mostrar a cor RGB e atualizar a imagem editada
def mostrar_cor_rgb(event):
    x, y = event.x, event.y
    pixel = imagem_capturada.getpixel((x, y))
    cor_rgb = f"RGB: {pixel[0]}, {pixel[1]}, {pixel[2]}"
    
    # Atualizar a label com as coordenadas
    coordenadas_label.config(text=f"Coordenadas do Mouse\nX: {x}  Y: {y}")
    
    # Atualizar a label com a cor RGB
    rgb_label.config(text=cor_rgb)

    # Atualizar a cor do quadrado
    quadrado_cor.config(bg=f"#{pixel[0]:02X}{pixel[1]:02X}{pixel[2]:02X}")

    # Aplicar a cor na imagem editada
    imagem_editada.paste((pixel[0], pixel[1], pixel[2]), (x, y, x + 1, y + 1))
    img_editada = ImageTk.PhotoImage(imagem_editada)
    label_imagem_editada.config(image=img_editada)
    label_imagem_editada.image = img_editada

# Carregar a imagem capturada
imagem_capturada = Image.open("imagem_capturada_webcam.jpg")

# Criar uma cópia da imagem capturada para a imagem editada
imagem_editada = imagem_capturada.copy()

# Configurar a interface gráfica
root = tk.Tk()
root.title("Visualizador de Imagem Capturada")

# Configurar um Frame para a imagem original
frame_imagem = ttk.Frame(root)
frame_imagem.pack(side="left")

# Configurar a imagem original
img_capturada = ImageTk.PhotoImage(imagem_capturada)
label_imagem = ttk.Label(frame_imagem, image=img_capturada)
label_imagem.pack(side="top")

# Configurar um Frame para coordenadas e cor RGB
frame_direita = ttk.Frame(root)
frame_direita.pack(side="left")

# Configurar uma Label para as coordenadas
coordenadas_label = ttk.Label(frame_direita, text="Coordenadas do Mouse\nX: -  Y: -")
coordenadas_label.pack(side="top")

# Configurar uma Label para a cor RGB
rgb_label = ttk.Label(frame_direita, text="RGB: -")
rgb_label.pack(side="top")

# Configurar um Frame para mostrar a cor
quadrado_frame = ttk.Frame(frame_direita, width=20, height=20)
quadrado_frame.pack(side="top")

# Configurar um Label para a imagem editada
img_editada = ImageTk.PhotoImage(imagem_editada)
label_imagem_editada = ttk.Label(frame_imagem, image=img_editada)
label_imagem_editada.pack(side="top")

# Lidar com eventos de movimento do mouse na imagem
label_imagem.bind("<Motion>", atualizar_coordenadas)

# Lidar com eventos de clique do mouse na imagem
label_imagem.bind("<Button-1>", mostrar_cor_rgb)

root.mainloop()
