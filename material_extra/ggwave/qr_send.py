#!/usr/bin/env python3
"""
Transmisión de Código QR a través de GGWave

Este script genera un código QR mínimo y lo transmite a través de
ondas sonoras utilizando GGWave, permitiendo demostrar la transmisión
de datos binarios de forma sencilla y pedagógica.

Autor: Maxi Yommi
Fecha: Abril 2025
Asignatura: Señales y Sistemas
"""

# Importamos las bibliotecas necesarias
import ggwave         # Para la codificación de audio
import pyaudio        # Para la reproducción de audio
import qrcode         # Para generar el código QR
import base64         # Para codificar la imagen en texto
import io             # Para manejar buffers de bytes
import numpy as np    # Para procesamiento de datos
import time           # Para pausas entre transmisiones
from PIL import Image # Para manipular imágenes

def generar_qr(datos, tamaño=1, borde=1):
    """
    Genera un código QR minimalista a partir de los datos proporcionados.
    
    Parámetros:
        datos (str): El contenido a codificar en el QR (URL, texto, etc.)
        tamaño (int): Tamaño de los módulos QR (1 = mínimo)
        borde (int): Tamaño del borde blanco alrededor del QR
        
    Retorna:
        Image: Imagen PIL del código QR generado
    """
    # Configuramos las opciones para un QR pequeño y simple
    qr = qrcode.QRCode(
        version=1,  # Versión más pequeña del QR (21x21 módulos)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel bajo de corrección
        box_size=tamaño,  # Tamaño de cada módulo
        border=borde  # Borde mínimo
    )
    
    # Agregamos los datos y generamos el QR
    qr.add_data(datos)
    qr.make(fit=True)
    
    # Creamos la imagen del QR (blanco y negro)
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    print(f"QR generado con éxito ({imagen_qr.size[0]}x{imagen_qr.size[1]} píxeles)")
    return imagen_qr

def codificar_qr_para_transmision(imagen_qr):
    """
    Convierte la imagen QR a formato de texto para transmisión.
    
    Parámetros:
        imagen_qr (Image): Imagen PIL del código QR
        
    Retorna:
        str: Representación en texto del QR con formato simple
    """
    # Convertimos a un array de numpy
    imagen_np = np.array(imagen_qr.convert('1'))  # Conversión a binario (blanco y negro)
    
    # Creamos una representación textual mínima (0 para blanco, 1 para negro)
    filas, columnas = imagen_np.shape
    representacion = f"{filas},{columnas};"  # Formato: "filas,columnas;datos"
    
    # Compresión básica: convertimos filas a cadenas de 0s y 1s
    for fila in imagen_np:
        # Convertimos valores booleanos (0=blanco, 1=negro) a caracteres
        representacion += ''.join(['1' if pixel else '0' for pixel in fila])
    
    return representacion

def transmitir_qr(url, protocolo=1, volumen=20, mostrar_qr=True):
    """
    Genera un código QR para la URL y lo transmite vía GGWave.
    
    Parámetros:
        url (str): URL a codificar en el QR
        protocolo (int): Protocolo GGWave a utilizar
        volumen (int): Volumen de la transmisión (0-100)
        mostrar_qr (bool): Si es True, muestra el QR generado
    """
    print(f"Generando código QR para: {url}")
    
    # Generamos el código QR
    imagen_qr = generar_qr(url)
    
    # Opcional: guardamos y mostramos el QR
    if mostrar_qr:
        imagen_qr.save("qr_generado.png")
        imagen_qr.show()
    
    # Codificamos el QR para transmisión
    datos_qr = codificar_qr_para_transmision(imagen_qr)
    print(f"QR codificado en formato de texto ({len(datos_qr)} bytes)")
    
    # Dividimos en fragmentos si es necesario (GGWave tiene límites de longitud)
    fragmentos = []
    max_longitud = 100  # Ajustar según el rendimiento de GGWave
    
    if len(datos_qr) <= max_longitud:
        fragmentos = [datos_qr]
    else:
        # Dividimos en fragmentos más pequeños
        for i in range(0, len(datos_qr), max_longitud):
            fragmento = datos_qr[i:i+max_longitud]
            fragmentos.append(fragmento)
    
    print(f"Transmitiendo QR en {len(fragmentos)} fragmentos...")
    
    # Inicializamos PyAudio
    p = pyaudio.PyAudio()
    
    # Transmitimos cada fragmento
    for i, fragmento in enumerate(fragmentos):
        # Añadimos metadatos para reconstrucción
        mensaje = f"QR:{i}:{len(fragmentos)}:{fragmento}"
        
        print(f"Transmitiendo fragmento {i+1}/{len(fragmentos)} ({len(mensaje)} bytes)")
        
        # Codificamos con GGWave
        waveform = ggwave.encode(mensaje, protocolId=protocolo, volume=volumen)
        
        if waveform is None:
            print(f"Error al codificar fragmento {i+1}")
            continue
        
        # Reproducimos el audio
        stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=48000,
            output=True,
            frames_per_buffer=4096
        )
        
        stream.write(waveform, len(waveform)//4)
        stream.stop_stream()
        stream.close()
        
        # Pausa entre fragmentos
        if i < len(fragmentos) - 1:
            time.sleep(1)  # Espera entre fragmentos
    
    p.terminate()
    print("Transmisión del código QR completada")

# Script principal
if __name__ == "__main__":
    # URL para codificar en el QR - puedes personalizarla para tu clase
    url = "https://github.com/maxiyommi/signal-systems"
    
    # Transmitimos el QR
    transmitir_qr(url, protocolo=1, volumen=30, mostrar_qr=True)