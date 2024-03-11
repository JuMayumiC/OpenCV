import cv2
import numpy as np

# Define a cor a ser rastreada (neste exemplo, vermelho)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Cria a janela de visualização
cv2.namedWindow("Detecção de Objeto", cv2.WINDOW_AUTOSIZE)

while True:
    # Lê um frame da câmera
    ret, frame = cap.read()

    # Converte o frame para o espaço de cores HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Cria uma máscara para a cor vermelha
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Encontra contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Se houver pelo menos um contorno
    if contours:
        # Encontra o maior contorno
        max_contour = max(contours, key=cv2.contourArea)

        # Calcula o retângulo delimitador
        x, y, w, h = cv2.boundingRect(max_contour)

        # Desenha um retângulo ao redor do objeto detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calcula o centro do retângulo
        centro_x = x + w // 2
        centro_y = y + h // 2

        # Se o centro estiver em uma região específica
        if 100 < centro_x < 300 and 100 < centro_y < 300:
            print("Objeto no centro!")

    # Exibe a imagem resultante
    cv2.imshow("Detecção de Objeto", frame)

    # Aguarda 100 milissegundos (ajuste este valor conforme necessário)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
