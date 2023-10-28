# EN EL CÓDIGO HAY MÁS COSAS PORQUE HE REUTILIZADO EL PROYECTO DE
# OTRO PROGRAMA QUE HABÍA HECHO PREVIAMENTE, ESTÁ EN MI GITHUB
# https://github.com/Tryop-X/videoLoader

from youtube_transcript_api import YouTubeTranscriptApi

# CARGAMOS LA LISTA DE VÍDEOS DE UN ARCHIVO
with open('listaVideos.txt', 'r') as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]
videos_fail = []

# OBTENTEMOS LAS TRANSCRIPCIONES CON EL API
def obtener_transcriptos(url):
    id_url = url.split('&')[0].split('://youtu.be/')[1]
    return YouTubeTranscriptApi.list_transcripts(id_url)

# GUARDADAMOS LAS TRANSCRIPCION EN DOS ARCHIVOS, UNO DE ELLOS
# SE HIZO CON LA INTENCIÓN DE ENTRENAR UN MODELO PERO NO SE COMPLETÓ
def guardar_transcripcion(transcripcion, url):

    with open('transcripciones.txt', 'a', encoding='utf-8') as file:
        for contenido in transcripcion:
            file.write(f"{contenido['text']}\n")
        file.write("\n")


    with open('detalle.txt', 'a', encoding='utf-8') as file:
        file.write(f"Url: {url}\n")
        for contenido in transcripcion:
            file.write(f"[{contenido['start']}]{contenido['text']}\n")
    print(f"{contenido['start']}: {contenido['duration']}\n")

def guardar_text(texto):
    with open('detalle.txt', 'a', encoding='utf-8') as file:
        file.write(f"{texto}\n")

    with open('transcripciones.txt', 'a', encoding='utf-8') as file:
        file.write(f"{texto}\n")

# RECORREMOS EL TXT Y SIEMPER QUE HAYA UN ENLACE OBTENEMOS LA TRANSCRIPCIÓN

for url in urls:
    try:

        if not (url.startswith("https://youtu.be")):
            guardar_text(url)
            continue

        transcriptos = obtener_transcriptos(url)
        transcripcion = next(transcripto.fetch() for transcripto in transcriptos if transcripto.language_code == 'es')

        guardar_transcripcion(transcripcion, url)
        print('[Hecho]', '<------')
    except Exception as e:
        print(e, '<---[ERROR]---', url)
        videos_fail.append(url)
        continue
