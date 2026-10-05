#!/usr/bin/env python3
"""
Recepción y Reconstrucción de Código QR desde GGWave

Este script escucha a través del micrófono para detectar fragmentos de un 
código QR transmitido mediante GGWave, los reconstruye y muestra 
el QR resultante.

Autor: Maxi Yommi
Fecha: Abril 2025
Asignatura: Señales y Sistemas
"""

# Importamos las bibliotecas necesarias
import ggwave         # Para la decodificación de audio
import pyaudio        # Para la captura de audio
import numpy as np    # Para procesamiento de datos
import time           # Para gestión de tiempo
from PIL import Image # Para manipular el QR reconstruido
import io             # Para operaciones de entrada/salida
import webbrowser     # Para abrir la URL del QR

def recibir_qr():
    """
    Escucha fragmentos de un código QR transmitido vía GGWave y lo reconstruye.
    
    Retorna:
        bool: True si se reconstruyó correctamente, False en caso contrario
    """
    fragmentos = {}  # Diccionario para almacenar los fragmentos
    total_fragmentos = None  # Se actualizará cuando recibamos el primer fragmento
    tiempo_ultimo_fragmento = time.time()  # Para control de tiempo de espera
    
    # Inicializamos PyAudio para captura
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=48000,
        input=True,
        frames_per_buffer=1024
    )
    
    # Inicializamos el decodificador GGWave
    instance = ggwave.init()
    print("Escuchando fragmentos de código QR... Presiona Ctrl+C para cancelar")
    
    try:
        # Escuchamos hasta completar todos los fragmentos o agotar el tiempo de espera
        while (total_fragmentos is None or len(fragmentos) < total_fragmentos):
            # Comprobamos si han pasado más de 20 segundos desde el último fragmento
            if time.time() - tiempo_ultimo_fragmento > 20:
                if total_fragmentos is not None:
                    print(f"Tiempo de espera agotado. Recibidos {len(fragmentos)}/{total_fragmentos} fragmentos")
                else:
                    print("Tiempo de espera agotado. No se detectaron fragmentos")
                break
                
            # Capturamos audio
            data = stream.read(1024, exception_on_overflow=False)
            res = ggwave.decode(instance, data)
            
            # Procesamos el resultado si hay decodificación
            if res is not None:
                try:
                    mensaje = res.decode("utf-8")
                    
                    # Verificamos si es un fragmento de QR (formato: "QR:índice:total:datos")
                    if mensaje.startswith("QR:"):
                        partes = mensaje.split(":", 3)
                        if len(partes) == 4:
                            _, indice, total, datos = partes
                            indice = int(indice)
                            total = int(total)
                            
                            # Almacenamos el fragmento
                            fragmentos[indice] = datos
                            total_fragmentos = total
                            
                            # Actualizamos el tiempo del último fragmento recibido
                            tiempo_ultimo_fragmento = time.time()
                            
                            print(f"Recibido fragmento {indice+1}/{total} ({len(datos)} bytes)")
                        else:
                            print("Formato de mensaje incorrecto")
                except Exception as e:
                    print(f"Error al procesar mensaje: {str(e)}")
                    
    except KeyboardInterrupt:
        print("\nRecepción interrumpida por el usuario")
    
    # Liberamos recursos
    ggwave.free(instance)
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Verificamos si tenemos todos los fragmentos
    if total_fragmentos is not None and len(fragmentos) == total_fragmentos:
        print(f"Recibidos todos los fragmentos ({total_fragmentos}). Reconstruyendo QR...")
        
        # Reconstruimos los datos del QR
        datos_qr = ""
        for i in range(total_fragmentos):
            if i in fragmentos:
                datos_qr += fragmentos[i]
            else:
                print(f"Falta el fragmento {i+1}. Reconstrucción incompleta.")
                return False
        
        # Procesamos los datos recibidos
        if ";" in datos_qr:
            # Formato esperado: "filas,columnas;datos"
            try:
                dim, datos_binarios = datos_qr.split(";", 1)
                filas, columnas = map(int, dim.split(","))
                
                # Verificamos si tenemos suficientes datos
                if len(datos_binarios) != filas * columnas:
                    print(f"Error: Datos incompletos. Esperados {filas*columnas}, recibidos {len(datos_binarios)}")
                    return False
                
                # Creamos una matriz para el QR
                matriz_qr = np.zeros((filas, columnas), dtype=np.uint8)
                
                # Rellenamos la matriz con los datos recibidos (0=blanco, 1=negro)
                for i in range(filas):
                    for j in range(columnas):
                        indice = i * columnas + j
                        if indice < len(datos_binarios):
                            matriz_qr[i, j] = 255 if datos_binarios[indice] == '0' else 0
                
                # Creamos la imagen del QR
                imagen_qr = Image.fromarray(matriz_qr, mode='L')
                
                # Guardamos y mostramos el QR reconstruido
                imagen_qr.save("qr_recibido.png")
                imagen_qr.show()
                
                print("Código QR reconstruido con éxito. Guardado como 'qr_recibido.png'")
                
                # Opcionalmente, preguntamos si quiere abrir la URL del QR
                respuesta = input("¿Deseas abrir la URL del código QR? (s/n): ")
                if respuesta.lower() == 's':
                    try:
                        # Utilizamos una biblioteca de escaneo QR (requiere instalación adicional)
                        # Aquí podrías usar bibliotecas como pyzbar o qreader
                        # Por simplicidad, mostramos cómo abrirla manualmente
                        url = input("Ingresa la URL que contiene el QR para abrirla: ")
                        if url:
                            webbrowser.open(url)
                    except:
                        print("No se pudo abrir la URL automáticamente")
                
                return True
                
            except Exception as e:
                print(f"Error al reconstruir el QR: {str(e)}")
                return False
        else:
            print("Formato de datos QR incorrecto")
            return False
    else:
        if total_fragmentos is not None:
            print(f"Reconstrucción incompleta: {len(fragmentos)}/{total_fragmentos} fragmentos recibidos")
        else:
            print("No se recibieron fragmentos de QR")
        return False

# Script principal
if __name__ == "__main__":
    print("Receptor de código QR vía GGWave")
    print("--------------------------------")
    print("Este programa escucha a través del micrófono para detectar")
    print("un código QR transmitido mediante ondas sonoras.")
    
    # Intentamos recibir un QR
    recibir_qr()