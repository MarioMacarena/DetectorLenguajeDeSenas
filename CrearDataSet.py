import os
import pickle
import cv2
import mediapipe as mp
import numpy as np

# Configuración
DATA_DIR = './data'
DEBUG_DIR = './debug'  # Carpeta para imágenes de depuración
os.makedirs(DEBUG_DIR, exist_ok=True)

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

data = []
labels = []
discarded = 0  # Contador de imágenes descartadas

# Procesar imágenes
for class_dir in os.listdir(DATA_DIR):
    class_path = os.path.join(DATA_DIR, class_dir)
    if not os.path.isdir(class_path):
        continue

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if not results.multi_hand_landmarks:
            discarded += 1
            continue

        # Extraer landmarks y normalizar
        hand_landmarks = results.multi_hand_landmarks[0]  # Usamos la primera mano detectada
        x_ = [lm.x for lm in hand_landmarks.landmark]
        y_ = [lm.y for lm in hand_landmarks.landmark]

        # Normalizar (restar mínimo y dividir por rango)
        x_min, x_max = min(x_), max(x_)
        y_min, y_max = min(y_), max(y_)
        data_aux = []
        for lm in hand_landmarks.landmark:
            data_aux.append((lm.x - x_min) / (x_max - x_min))
            data_aux.append((lm.y - y_min) / (y_max - y_min))

        # Verificar que el tamaño sea el correcto
        if len(data_aux) != 42:
            discarded += 1
            continue

        data.append(data_aux)
        labels.append(class_dir)

        # Opcional: Guardar imagen con landmarks para depuración
        debug_img = img.copy()
        mp.solutions.drawing_utils.draw_landmarks(
            debug_img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imwrite(os.path.join(DEBUG_DIR, f"{class_dir}_{img_name}"), debug_img)

print(f"Dataset creado. Imágenes descartadas: {discarded}")

# Guardar datos
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
