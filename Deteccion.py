from ultralytics import YOLO
import cv2

#cargar el modelo YOLO
model = YOLO('yolov8m.pt')

#defino ruta del video
source = "./data/completo.mp4"

cap = cv2.VideoCapture(source)

#cordenadas de lugares de estacionamiento
coordenadas = [
    (50, 500),
    (158, 500),
    (262, 490),
    (366, 484),
    (483, 477),
    (588, 461),
    (692, 450),
    (800, 433),
    (901, 414),
    (1000, 417),
    (1071, 407),
    (1200, 398)
]


# Configurar la salida de video
output_video_path = "./data/salida.mp4"
fps = 25
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))


while cap.isOpened():
    ret, frame = cap.read()
    contador_libres = 12
    if not ret or frame is None:
        break

    #realiza traking de los autos del video
    results = model.track(frame, save=True ,conf=0.6, classes=[2], agnostic_nms=True)


    for coord in coordenadas:
        cv2.circle(frame, coord, 15, (0, 0, 255), -1)  # Dibujar los lugares vacios en rojo


    for result in results:
        contador_ocupados=0
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2, _, _, _ = map(int, r)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            for coord in coordenadas:
                # Coordenadas del centro del círculo
                cx, cy = coord

                # Verificar si el centro del círculo está dentro del rectángulo
                if x1 < cx < x2 and y1 < cy < y2:
                    cv2.circle(frame, coord, 15, (0, 255, 0), -1)  # Dibujar el círculo en verde si esta ocupado
                    contador_ocupados+=1

        cv2.rectangle(frame, (0, 0), (400, 50), (0, 0, 0), -1)
        cv2.putText(frame, text=f'Espacios Ocupados: {contador_ocupados}', org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

    # Mostrar el video con las detecciones y los puntos
    cv2.imshow('Video con detecciones y puntos', frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()