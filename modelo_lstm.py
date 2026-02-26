import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Construção da Arquitetura LSTM
def build_lstm_model(input_shape):
    model = Sequential([
        # 1ª Camada Oculta LSTM (Retorna sequências)
        LSTM(50, return_sequences=True, input_shape=input_shape, activation='tanh'),
        Dropout(0.2), # Regularização de 20%
        
        # 2ª Camada Oculta LSTM
        LSTM(50, return_sequences=False, activation='tanh'),
        Dropout(0.2),
        
        # Camada de Saída (Classificação binária: Normal vs Anomalia)
        Dense(1, activation='sigmoid') 
    ])
    
    # Compilação do modelo
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy']) # Métrica de acurácia
    return model
