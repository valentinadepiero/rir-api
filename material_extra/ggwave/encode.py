#!/usr/bin/env python3
"""
Ejemplo de codificación de audio utilizando GGWave

Este script demuestra cómo codificar un mensaje de texto en una señal
acústica utilizando la biblioteca GGWave y reproducirlo a través
de los altavoces del sistema.

Autor: Maxi Yommi
Fecha: Abril 2025
Asignatura: Señales y Sistemas
"""

# Importamos las bibliotecas necesarias
import ggwave     # Biblioteca para codificación/decodificación de datos en audio
import pyaudio    # Interfaz para reproducción y grabación de audio
import wave       # Para guardar archivos de audio WAV
import numpy as np # Para manipulación de arrays

def transmitir_mensaje(mensaje, protocolo=1, volumen=20, guardar=False):
    """
    Codifica y transmite un mensaje a través de ondas sonoras.
    
    Parámetros:
        mensaje (str): El texto que se desea transmitir
        protocolo (int): ID del protocolo de transmisión GGWave
                         1 = normal (más confiable, más lento)
                         2 = fast (más rápido, menos confiable)
                         otros valores según documentación GGWave
        volumen (int): Nivel de volumen de la transmisión (0-100)
        guardar (bool): Si es True, guarda el audio en un archivo WAV
    """
    # Inicialización de PyAudio para manejo de audio
    p = pyaudio.PyAudio()
    
    # Generamos la forma de onda (waveform) codificada con el mensaje
    # protocolId: determina la velocidad/confiabilidad de la transmisión
    # volume: controla la amplitud de la señal generada (volumen)
    print(f"Codificando mensaje: '{mensaje}'")
    waveform = ggwave.encode(mensaje, protocolId=protocolo, volume=volumen)
    
    if waveform is None:
        print("Error: No se pudo codificar el mensaje")
        return
    
    # Si se solicita guardar el audio, lo guardamos en un archivo WAV
    if guardar:
        # Nombre del archivo a guardar
        nombre_archivo = "encode_ggwave.wav"
        
        # Convertir waveform a array numpy
        muestras = np.frombuffer(waveform, dtype=np.float32)
        
        # Guardar como archivo WAV
        with wave.open(nombre_archivo, 'wb') as wavefile:
            wavefile.setnchannels(1)                # Mono
            wavefile.setsampwidth(2)                # 16 bits por muestra
            wavefile.setframerate(48000)            # 48kHz
            
            # Convertir a int16 para compatibilidad
            muestras_int16 = (muestras * 32767).astype(np.int16)
            wavefile.writeframes(muestras_int16.tobytes())
        
        print(f"Audio guardado en: {nombre_archivo}")
    
    # Configuración y apertura del stream de audio para reproducción
    print(f"Transmitiendo mensaje usando protocolo {protocolo}...")
    stream = p.open(
        format=pyaudio.paFloat32,    # Formato de punto flotante de 32 bits
        channels=1,                  # Audio mono (1 canal)
        rate=48000,                  # Frecuencia de muestreo de 48kHz (estándar para GGWave)
        output=True,                 # Stream de salida (reproducción)
        frames_per_buffer=4096       # Tamaño del buffer para mejor rendimiento
    )
    
    # Reproducción del audio codificado
    stream.write(waveform, len(waveform)//4)  # len(waveform)//4 es necesario porque cada muestra de punto flotante, ocupa 4 bytes en memoria
    
    # Cerramos el stream de audio
    stream.stop_stream()
    stream.close()
    
    # Finalizamos la instancia de PyAudio
    p.terminate()
    
    print("Transmisión completada.")

# Si este script se ejecuta directamente (no se importa como módulo)
if __name__ == "__main__":
    # Mensaje que queremos transmitir
    mensaje = "Este mensaje viaja a 343 m/s a través del aire, sorteando obstáculos y ruido ambiente. Si puedes recibirlo misión completa!."
    
    # Transmitimos el mensaje
    transmitir_mensaje(mensaje, protocolo=1, volumen=20, guardar=True)  # Con guardar=True para guardar el audio