import streamlit as st
import random

# Palabras por categoría
categorias = {
    "🌎 Países": [
        "argentina", "brasil", "españa", "italia", "japon",
        "canada", "alemania", "francia", "mexico", "chile"
    ],

    "🎮 Videojuegos": [
        "minecraft", "fortnite", "pokemon", "zelda", "mario",
        "godofwar", "undertale", "terraria", "sonic"
    ],

    "🎬 Películas": [
        "avatar", "titanic", "gladiador", "matrix", "shrek",
        "rocky", "batman", "superman", "alien", "joker"
    ],

    "📺 Series": [
        "friends", "lost", "dark", "dexter", "breakingbad",
        "strangerthings", "theoffice", "vikings", "merlina"
    ],

    "🍥 Anime": [
        "naruto", "dragonball", "onepiece", "bleach", "pokemon",
        "deathnote", "evangelion", "demonslayer", "jujutsukaisen"
    ],

    "🎵 Música": [
        "queen", "metallica", "nirvana", "beatles", "coldplay",
        "eminem", "shakira", "sodastereo", "abba", "bonjovi"
    ]
}


# Crear una nueva partida
def nuevo_juego():
    categoria = st.session_state.categoria

    st.session_state.palabra = random.choice(categorias[categoria])
    st.session_state.letras = []
    st.session_state.intentos = 6
    st.session_state.estado = "jugando"


# Inicializar el juego
if "palabra" not in st.session_state:
    st.session_state.categoria = "🌎 Países"
    nuevo_juego()


# Título
st.title("🎯 Juego del Ahorcado")

# Elegir categoría
categoria = st.selectbox(
    "Elegí una categoría:",
    list(categorias.keys())
)


# Si cambia la categoría, comienza una nueva partida
if categoria != st.session_state.categoria:
    st.session_state.categoria = categoria
    nuevo_juego()
    st.rerun()


# Obtener datos del juego
palabra = st.session_state.palabra
letras = st.session_state.letras


# Mostrar palabra
mostrar = ""

for letra in palabra:

    if letra in letras:
        mostrar += letra + " "
    else:
        mostrar += "_ "


st.subheader(mostrar)

# Mostrar intentos
st.write("❤️ Intentos restantes:", st.session_state.intentos)

# Mostrar letras usadas
if letras:
    st.write("🔤 Letras usadas:", ", ".join(letras))


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

            # Si la letra no está, pierde un intento
            if letra not in palabra:
                st.session_state.intentos -= 1

            # Comprobar si ganó
            gano = True

            for caracter in palabra:
                if caracter not in letras:
                    gano = False

            if gano:
                st.session_state.estado = "gano"

            # Comprobar si perdió
            elif st.session_state.intentos <= 0:
                st.session_state.estado = "perdio"

            st.rerun()


# Si ganó
elif st.session_state.estado == "gano":

    st.success("🎉 ¡GANASTE!")

    st.write("La palabra era:", palabra)

    if st.button("🔄 Jugar otra vez"):
        nuevo_juego()
        st.rerun()


# Si perdió
elif st.session_state.estado == "perdio":

    st.error("💀 ¡PERDISTE!")

    st.write("La palabra era:", palabra)

    if st.button("🔄 Jugar otra vez"):
        nuevo_juego()
        st.rerun()
