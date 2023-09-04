import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

# Função para atualizar as coordenadas
def atualizar_coordenadas(event):
    x, y = event.x, event.y
    coordenadas = f"Coordenadas do Mouse\nX: {x}  Y: {y}"
    coordenadas_label.config(text=coordenadas)

# Função para mostrar a cor RGB e atualizar a imagem editada
def mostrar_cor_rgb(event):
    x, y = event.x, event.y
    
    # Converter a imagem capturada para uma matriz numpy
    imagem_capturada_np = np.array(imagem_capturada)
    
    # Obter o pixel da imagem capturada
    pixel = imagem_capturada_np[y, x]
    
    cor_rgb = f"RGB: {pixel[0]}, {pixel[1]}, {pixel[2]}"
    
    # Atualizar a label com as coordenadas
    coordenadas_label.config(text=f"Coordenadas do Mouse\nX: {x}  Y: {y}")
    
    # Atualizar a label com a cor RGB
    rgb_label.config(text=cor_rgb)

    # Aplicar a cor na imagem editada
    imagem_editada[y, x] = pixel
    img_editada = ImageTk.PhotoImage(Image.fromarray(imagem_editada))
    label_imagem_editada.config(image=img_editada)
    label_imagem_editada.image = img_editada

# Função para aplicar os filtros com base nos valores das Trackbars
def aplicar_filtros(_=None):
    valor_media = int(float(filtro_media_var.get()))
    valor_threshold = int(float(filtro_threshold_var.get()))

    # Aplicar filtro passa-baixa média
    kernel_media = np.ones((valor_media, valor_media), dtype=np.float32) / (valor_media * valor_media)
    img_filtrada_media = cv2.filter2D(imagem_original_cv2, -1, kernel_media)

    # Aplicar filtro de threshold apenas se o valor do threshold for maior que 1
    if valor_threshold > 1:
        _, img_filtrada_threshold = cv2.threshold(img_filtrada_media, valor_threshold, 255, cv2.THRESH_BINARY)
        imagem_editada_cv2[:] = img_filtrada_threshold[:]
    else:
        # Se o valor do threshold for 1 ou menor, não aplicar o threshold
        imagem_editada_cv2[:] = img_filtrada_media[:]

    img_editada = ImageTk.PhotoImage(Image.fromarray(imagem_editada_cv2))
    label_imagem_editada.config(image=img_editada)
    label_imagem_editada.image = img_editada

# Carregar a imagem capturada (substitua pelo caminho correto)
imagem_capturada = Image.open("imagem_capturada_webcam.jpg")
imagem_original_cv2 = np.array(imagem_capturada)

# Criar uma cópia da imagem capturada para a imagem editada
imagem_editada = np.array(imagem_capturada)
imagem_editada_cv2 = imagem_editada.copy()

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
img_editada = ImageTk.PhotoImage(Image.fromarray(imagem_editada))
label_imagem_editada = ttk.Label(frame_imagem, image=img_editada)
label_imagem_editada.pack(side="top")

# Lidar com eventos de movimento do mouse na imagem
label_imagem.bind("<Motion>", atualizar_coordenadas)

# Lidar com eventos de clique do mouse na imagem
label_imagem.bind("<Button-1>", mostrar_cor_rgb)

# Criar um Frame para as Trackbars
frame_trackbar = ttk.Frame(frame_direita)
frame_trackbar.pack(side="top")

# Trackbar para filtro passa-baixa média
ttk.Label(frame_trackbar, text="Filtro Média").pack(side="top")
filtro_media_var = tk.StringVar()
filtro_media_var.set("1")  # Valor inicial
ttk.Scale(frame_trackbar, from_=1, to=20, variable=filtro_media_var, command=aplicar_filtros).pack(side="top")

# Trackbar para filtro de threshold
ttk.Label(frame_trackbar, text="Filtro Threshold").pack(side="top")
filtro_threshold_var = tk.StringVar()
filtro_threshold_var.set("1")  # Valor inicial
ttk.Scale(frame_trackbar, from_=1, to=255, variable=filtro_threshold_var, command=aplicar_filtros).pack(side="top")

root.mainloop()
