import cv2

# Inicialize a câmera (use 0 para a câmera padrão, ou ajuste conforme necessário)
cap = cv2.VideoCapture(0)

# Crie uma janela
cv2.namedWindow("Câmera", cv2.WINDOW_NORMAL)

while True:
    # Capture um quadro
    ret, frame = cap.read()

    # Exiba o quadro
    cv2.imshow("Câmera", frame)

    # Encerrar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
