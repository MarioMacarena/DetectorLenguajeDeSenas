import pickle
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Agregar Graphviz al PATH de Windows
os.environ["PATH"] += os.pathsep + "C:/Users/alber/Downloads/windows_10_cmake_Release_Graphviz-12.2.1-win64/Graphviz-12.2.1-win64/bin"
regularizers = keras.regularizers

# Cargar los datos
data_dict = pickle.load(open('./data.pickle', 'rb'))
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Codificar las etiquetas
encoder = LabelEncoder()
labels = encoder.fit_transform(labels)  # Convertir las etiquetas a valores numéricos
num_classes = len(np.unique(labels))  # Número de clases (por ejemplo, números de las carpetas)
y = keras.utils.to_categorical(labels, num_classes=num_classes)  # Convertir a formato one-hot

# Dividir los datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.2, stratify=y, random_state=42)

# Definir el modelo con regularización L2 y Dropout
model = keras.Sequential([
    keras.layers.Input(shape=(42,)),
    keras.layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)),  # Regularización L2
    keras.layers.Dropout(0.3),
    keras.layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)),  # Regularización L2
    keras.layers.Dropout(0.3),
    keras.layers.Dense(num_classes, activation='softmax')
])

tf.keras.utils.plot_model(model, to_file="modelo.png", show_shapes=True, show_layer_names=True)

# Compilar el modelo
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Definir los callbacks
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, verbose=1)
model_checkpoint = tf.keras.callbacks.ModelCheckpoint('best_model.keras', monitor='val_accuracy', save_best_only=True)

# Entrenar el modelo
history = model.fit(
    x_train, y_train,
    epochs=100,  # Reducir las épocas para evitar sobreajuste
    batch_size=64,  # Aumentar el tamaño del batch
    validation_data=(x_test, y_test),
    callbacks=[early_stopping, model_checkpoint],
    verbose=1
)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nPrecisión en test: {test_acc:.2f}")

# Guardar el modelo entrenado
model.save('modelo_entrenado.keras')
print("Modelo guardado.")
