#!/usr/bin/env python3
"""
Ejemplo de decodificación de audio utilizando GGWave

Este script demuestra cómo configurar un receptor que escucha
constantemente a través del micrófono para detectar y decodificar
mensajes transmitidos mediante la biblioteca GGWave.

Autor: Maxi Yommi
Fecha: Abril 2025
Asignatura: Señales y Sistemas
"""

# Importamos las bibliotecas necesarias
import ggwave     # Biblioteca para codificación/decodificación de datos en audio
import pyaudio    # Interfaz para reproducción y grabación de audio

def escuchar_mensajes():
    """
    Configura un receptor que escucha continuamente a través del micrófono
    para detectar y decodificar mensajes codificados con GGWave.
    
    El receptor se mantendrá escuchando hasta que el usuario presione Ctrl+C.
    """
    # Inicialización de PyAudio para manejo de audio
    p = pyaudio.PyAudio()
    
    # Configuración y apertura del stream de audio para grabación
    stream = p.open(
        format=pyaudio.paFloat32,    # Formato de punto flotante de 32 bits
        channels=1,                  # Audio mono (1 canal)
        rate=48000,                  # Frecuencia de muestreo de 48kHz (estándar para GGWave)
        input=True,                  # Stream de entrada (grabación)
        frames_per_buffer=1024       # Tamaño del buffer para mejor rendimiento
    )
    
    # Inicialización del decodificador GGWave
    print('Escuchando... Presiona Ctrl+C para detener')
    instance = ggwave.init()  # Creamos una instancia del decodificador
    
    try:
        # Bucle principal de escucha
        while True:
            # Lectura de datos de audio desde el micrófono
            # exception_on_overflow=False evita errores cuando el buffer se llena
            data = stream.read(1024, exception_on_overflow=False)
            
            # Intento de decodificación del fragmento de audio capturado
            res = ggwave.decode(instance, data)
            
            # Si se decodificó un mensaje (res no es None)
            if (res is not None):
                try:
                    # Convertimos los datos binarios a texto UTF-8
                    mensaje = res.decode("utf-8")
                    print('Mensaje recibido: ' + mensaje)
                except UnicodeDecodeError:
                    # En caso de error al decodificar el texto (datos corruptos)
                    print('Recibidos datos no válidos o incompletos')
                    pass
                    
    except KeyboardInterrupt:
        # Captura la pulsación de Ctrl+C para finalizar el programa limpiamente
        print('\nDetención solicitada por el usuario')
    
    # Liberación de recursos
    ggwave.free(instance)  # Liberamos la instancia del decodificador
    
    # Cerramos el stream de audio
    stream.stop_stream()
    stream.close()
    
    # Finalizamos la instancia de PyAudio
    p.terminate()
    
    print("Receptor detenido.")

# Si este script se ejecuta directamente (no se importa como módulo)
if __name__ == "__main__":
    # Iniciamos el proceso de escucha
    escuchar_mensajes()