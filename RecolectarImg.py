import os
import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3 
dataset_size = 100    
resolution = (640, 480)  

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Recolectando datos para la clase {j}')

    # Mensaje de preparación
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Guía visual para el usuario
        cv2.putText(frame, f'Clase {j}: Presiona "Q" para empezar', (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (100, 100), (540, 380), (0, 255, 0), 2)  # Área de la mano
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('q'):
            break

    # Captura de imágenes
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue

        # Recortar la región de la mano (área definida previamente)
        hand_region = frame[100:380, 100:540]  # Recorta el área de interés
        resized = cv2.resize(hand_region, resolution)

        # Guardar la imagen en la carpeta correspondiente
        img_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, resized)

        # Mostrar feedback en la pantalla
        cv2.putText(frame, f"Imagen {counter + 1}/{dataset_size}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        cv2.waitKey(100)  # Pausa breve para evitar duplicados

        counter += 1

        # Mostrar el frame
        cv2.imshow('frame', frame)

    print(f"Recolección completada para la clase {j}.")

cap.release()
cv2.destroyAllWindows()
print("Proceso de recolección de datos finalizado.")

