import cv2
import numpy as np

# Função para capturar a imagem da câmera
def capturar_imagem():
    cap = cv2.VideoCapture(0)  # Abrir a câmera padrão (0) ou uma câmera externa (por exemplo, 1)

    while True:
        ret, frame = cap.read()  # Capturar um quadro da câmera
        cv2.imshow("Imagem Original", frame)  # Mostrar a imagem original

        # Esperar até que a tecla 'c' seja pressionada para capturar a imagem
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("imagem_capturada.png", frame)  # Salvar a imagem capturada
            break

    cap.release()  # Fechar a câmera
    cv2.destroyAllWindows()

# Função para mostrar a cor ao clicar na imagem original
def mostrar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Verificar se o botão esquerdo do mouse foi clicado
        cor_pixel = frame[y, x]  # Obter a cor do pixel clicado
        print(f"A cor do pixel clicado é: {cor_pixel}")

# Função para aplicar filtros
def aplicar_filtros(banda):
    # Converter a imagem capturada para escala de cinza
    imagem_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar o filtro passa-baixa escolhido (por exemplo, filtro de média)
    if banda == 1:
        imagem_filtrada = cv2.blur(imagem_gray, (5, 5))  # Você pode ajustar o tamanho do kernel
    else:
        imagem_filtrada = cv2.GaussianBlur(imagem_gray, (5, 5), 0)  # Filtro Gaussiano

    # Aplicar o filtro passa-alta (por exemplo, filtro de Laplaciano)
    imagem_passa_alta = cv2.Laplacian(imagem_filtrada, cv2.CV_64F)

    # Binarizar a imagem usando um limite escolhido
    _, imagem_binaria = cv2.threshold(imagem_passa_alta, 30, 255, cv2.THRESH_BINARY)

    # Apresentar a imagem resultante
    cv2.imshow("Imagem Processada", imagem_binaria)

# Capturar a imagem
capturar_imagem()

# Carregar a imagem capturada
frame = cv2.imread("imagem_capturada.png")

# Mostrar a cor ao clicar na imagem
cv2.imshow("Imagem Original", frame)
cv2.setMouseCallback("Imagem Original", mostrar_cor)

# Criar janelas para os trackbars
cv2.namedWindow("Filtros")
cv2.createTrackbar("Banda", "Filtros", 1, 2, aplicar_filtros)

# Iniciar o loop principal
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

