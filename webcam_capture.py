import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

# Função para capturar a imagem da webcam e abrir captura_imagem.py
def capturar_e_abrir_captura():
    ret, frame = cap.read()
    if ret:
        # Salvar a imagem capturada
        cv2.imwrite("imagem_capturada_webcam.jpg", frame)
        
        # Abrir captura_imagem.py com a imagem capturada
        subprocess.Popen(["python", "captura_imagem.py"])

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

# Verificar se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera. Verifique se ela está conectada e funcionando corretamente.")
else:
    # Configurar a interface gráfica
    root = tk.Tk()
    root.title("Captura de Webcam")

    frame_webcam = ttk.Frame(root)
    frame_webcam.grid(column=0, row=0)

    botao_captura = ttk.Button(frame_webcam, text="Capturar", command=capturar_e_abrir_captura)
    botao_captura.grid(column=0, row=0)

    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)

            # Exibir a imagem da webcam em uma label
            label_webcam = ttk.Label(frame_webcam, image=img)
            label_webcam.grid(row=1, column=0)

            label_webcam.img_ref = img

        root.update()

    # Liberar a captura de vídeo quando a janela for fechada
    cap.release()
    cv2.destroyAllWindows()

    root.mainloop()
