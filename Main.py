import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp

# Cargar el modelo entrenado
try:
    model = tf.keras.models.load_model('modelo_entrenado.keras') 
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Configuración de MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Mapeo de clases a letras
class_map = {
    0: "A",
    1: "B",
    2: "C",
    # Añadir más letras según tu dataset
}

# Iniciar cámara
cap = cv2.VideoCapture(0)
cv2.namedWindow("Detector de Señas", cv2.WINDOW_NORMAL)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # Convertir a RGB y procesar
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar landmarks y conexiones
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),  # Conexiones (verde)
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)   # Landmarks (rojo)
            )

            # Extraer coordenadas de los landmarks
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y])

            if len(landmarks) == 42:
                landmarks = np.array(landmarks)

                # Predicción
                prediction = model.predict(np.expand_dims(landmarks, axis=0))
                predicted_class = np.argmax(prediction)
                confidence = np.max(prediction)

                # Mostrar la letra predicha si la confianza es alta
                if confidence > 0.4:
                    predicted_char = class_map.get(predicted_class, "?")
                    cv2.putText(
                        frame,
                        f"Letra: {predicted_char} ({confidence:.2f})",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

    # Mostrar frame
    cv2.imshow("Detector de Señas", frame)

    # Salir con ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
