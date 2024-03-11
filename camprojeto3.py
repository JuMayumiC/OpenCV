import cv2

def draw_rectangle(event, x, y, flags, param):
    global drawing, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_pt = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bottom_right_pt = (x, y)
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 2)
        cv2.imshow("Rastreamento de Objetos", img)

drawing = False
top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)

# Crie uma janela
cv2.namedWindow("Rastreamento de Objetos")
cv2.setMouseCallback("Rastreamento de Objetos", draw_rectangle)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow("Rastreamento de Objetos", img)

    # Aumente ou diminua o valor (por exemplo, de 100 para 500) para alterar o tempo que o retângulo permanece na tela
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()