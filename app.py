
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


# Dibujo del ahorcado
def dibujo_ahorcado(intentos):

    dibujos = [
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """
    ]

    return dibujos[intentos]


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


# Si cambia la categoría
if categoria != st.session_state.categoria:

    st.session_state.categoria = categoria

    nuevo_juego()

    st.rerun()


# Datos del juego
palabra = st.session_state.palabra
letras = st.session_state.letras
intentos = st.session_state.intentos


# Mostrar dibujo y datos
col1, col2 = st.columns(2)

with col1:
    st.code(dibujo_ahorcado(intentos))

with col2:
    st.write("❤️ Intentos restantes:", intentos)

    if letras:
        st.write("🔤 Letras usadas:", ", ".join(letras))
    else:
        st.write("🔤 Letras usadas: ninguna")


# Mostrar palabra
mostrar = ""

for letra in palabra:

    if letra in letras:
        mostrar += letra + " "
    else:
        mostrar += "_ "


st.subheader(mostrar)


# Teclado
st.write("### 🔤 Elegí una letra:")

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Crear 9 columnas
columnas = st.columns(9)

for i, letra in enumerate(alfabeto):

    with columnas[i % 9]:

        # Si la letra ya fue usada, desactivar botón
        desactivado = letra in letras or st.session_state.estado != "jugando"

        if st.button(
            letra.upper(),
            key="letra_" + letra,
            disabled=desactivado
        ):

            letras.append(letra)

            # Si la letra no está en la palabra
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


# Victoria
if st.session_state.estado == "gano":

    st.success("🎉 ¡GANASTE!")

    st.write("La palabra era:", palabra)

    if st.button("🔄 Jugar otra vez"):

        nuevo_juego()

        st.rerun()


# Derrota
elif st.session_state.estado == "perdio":

    st.error("💀 ¡PERDISTE!")

    st.write("La palabra era:", palabra)

    if st.button("🔄 Jugar otra vez"):

        nuevo_juego()

        st.rerun()

