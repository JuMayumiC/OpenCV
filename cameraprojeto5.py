import cv2

# Palavra específica a ser reconhecida
palavra_especifica = "exemplo"

# Limiar de densidade de caracteres
limiar_densidade = 0.5

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Cria a janela de visualização
cv2.namedWindow("Detecção de Palavras", cv2.WINDOW_AUTOSIZE)

while True:
    # Lê um frame da câmera
    ret, frame = cap.read()

    # Inverte as cores para destacar o texto branco sobre fundo preto
    inverted_frame = cv2.bitwise_not(frame)

    # Converte o frame invertido para escala de cinza
    gray = cv2.cvtColor(inverted_frame, cv2.COLOR_BGR2GRAY)

    # Aplica um limiar para binarizar a imagem
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Encontra contornos na imagem binarizada
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Para cada contorno encontrado
    for contour in contours:
        # Calcula o retângulo delimitador
        x, y, w, h = cv2.boundingRect(contour)

        # Critérios para considerar um contorno como palavra
        area = cv2.contourArea(contour)
        aspect_ratio = w / h
        density = area / (w * h) if w * h > 0 else 0

        # Verifica se a região atende aos critérios
        if 100 < area < 10000 and 2 < aspect_ratio < 10 and density > limiar_densidade:
            # Extrai a região da imagem contendo a palavra
            word_region = frame[y:y+h, x:x+w]

            # Converte a região da palavra para escala de cinza
            word_gray = cv2.cvtColor(word_region, cv2.COLOR_BGR2GRAY)

            # Aplica OCR "simplificado" (extraindo caracteres)
            text = ''.join([chr(c) for c in word_gray.flatten() if 32 < c < 127])

            # Se a palavra detectada é a palavra específica
            if palavra_especifica.lower() in text.lower():
                print(f"Palavra específica '{palavra_especifica}' detectada!")

            # Desenha um retângulo ao redor da palavra
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibe a imagem resultante
    cv2.imshow("Detecção de Palavras", frame)

    # Aguarda 100 milissegundos (ajuste este valor conforme necessário)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
