import streamlit as st
import requests
import html
import random

# Categorías de Open Trivia DB
categorias = {
    "🌎 Países": 22,          # Geography
    "🎮 Videojuegos": 15,     # Video Games
    "🎬 Películas": 11,       # Film
    "📺 Series": 14,          # Television
    "🍥 Anime": 31,           # Japanese Anime & Manga
    "🎵 Música": 12           # Music
}


def obtener_palabra(categoria):
    id_categoria = categorias[categoria]

    url = f"https://opentdb.com/api.php?amount=10&category={id_categoria}&type=multiple"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        if datos["response_code"] == 0:
            pregunta = random.choice(datos["results"])

            palabra = html.unescape(pregunta["correct_answer"])

            return palabra, html.unescape(pregunta["question"])

    return None, None


def nuevo_juego():
    palabra, pregunta = obtener_palabra(st.session_state.categoria)

    if palabra:
        st.session_state.palabra = palabra.lower()
        st.session_state.pregunta = pregunta
        st.session_state.letras = []
        st.session_state.intentos = 6
        st.session_state.estado = "jugando"


# Iniciar
if "categoria" not in st.session_state:
    st.session_state.categoria = "🌎 Países"
    nuevo_juego()


st.title("🎯 Ahorcado")

# Categoría
categoria = st.selectbox(
    "Elegí una categoría:",
    list(categorias.keys())
)

# Si cambia la categoría
if categoria != st.session_state.categoria:
    st.session_state.categoria = categoria
    nuevo_juego()
    st.rerun()


palabra = st.session_state.palabra
letras = st.session_state.letras


# Mostrar palabra
mostrar = ""

for letra in palabra:

    if letra == " ":
        mostrar += "   "

    elif letra.lower() in letras:
        mostrar += letra + " "

    elif not letra.isalpha():
        mostrar += letra + " "

    else:
        mostrar += "_ "


st.subheader(mostrar)

st.write("❤️ Intentos:", st.session_state.intentos)

if letras:
    st.write("🔤 Letras usadas:", ", ".join(letras))


# Pregunta de la API
with st.expander("💡 Ver pregunta"):
    st.write(st.session_state.pregunta)


# Juego
if st.session_state.estado == "jugando":

    letra = st.text_input(
        "Ingresá una letra:",
        max_chars=1
    )

    if st.button("Probar letra"):

        letra = letra.lower()

        if not letra.isalpha():

            st.warning("Ingresá una letra válida.")

        elif letra in letras:

            st.warning("Ya usaste esa letra.")

        else:

            letras.append(letra)

            if letra not in palabra:
                st.session_state.intentos -= 1

            # Comprobar victoria
            gano = True

            for caracter in palabra.lower():

                if caracter.isalpha() and caracter not in letras:
                    gano = False

            if gano:
                st.session_state.estado = "gano"

            elif st.session_state.intentos <= 0:
                st.session_state.estado = "perdio"

            st.rerun()


# Ganó
elif st.session_state.estado == "gano":

    st.success("🎉 ¡GANASTE!")

    st.write("La respuesta era:", st.session_state.palabra)

    if st.button("🔄 Nueva partida"):
        nuevo_juego()
        st.rerun()


# Perdió
elif st.session_state.estado == "perdio":

    st.error("💀 ¡PERDISTE!")

    st.write("La respuesta era:", st.session_state.palabra)

    if st.button("🔄 Nueva partida"):
        nuevo_juego()
        st.rerun()
