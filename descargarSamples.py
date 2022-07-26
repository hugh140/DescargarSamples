from pytube import YouTube
import os
import re
direccion = "D:/Música/SamplesCanciones/"

while True:
    print()
    link = input("Ingresar link: ")
    try:
        yt = YouTube(link)
        titulo = re.sub(r'[^\w]', ' ', yt.title)
        yt.title = titulo
        ys = yt.streams.filter(only_audio=True).first()
        archivo = ys.download(direccion)

        contarArchivos = 0
        for i in os.listdir(direccion):
            contarArchivos += 1
        contarArchivos += 1

        nombre, extension = os.path.splitext(archivo)
        convertirMp3 = nombre + ".mp3"
        os.rename(archivo, convertirMp3)

        nuevoNombre = direccion + str(contarArchivos) + "_" + yt.title + ".mp3"
        os.rename(direccion + yt.title + ".mp3", nuevoNombre)

        print("Se ha descargado correctamente.")
        print()
        os.startfile(direccion)
    except:
        print("ERROR: No se ha logrado efectuar la descarga.")
        print("Intenta ingresar correctamente el link.")
        print()

    print("¿Continuar con la descarga?\nSi. Pulsa 1\nNo. Pulsa cualquier tecla")
    seguirDescargando = input()
    if seguirDescargando == "1": continue
    else: break
