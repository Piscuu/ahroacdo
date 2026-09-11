# 🎯 Juego del Ahorcado

Juego del clásico **Ahorcado desarrollado en Python utilizando Streamlit**.

El jugador debe elegir una categoría y adivinar una palabra letra por letra antes de quedarse sin intentos.

## 📋 Características

* 🌎 Categoría **Países**
* 🎮 Categoría **Videojuegos**
* 🎬 Categoría **Películas**
* 📺 Categoría **Series**
* 🍥 Categoría **Anime**
* 🎵 Categoría **Música**
* 🎲 Palabra seleccionada aleatoriamente
* ❤️ 6 intentos por partida
* 🔤 Registro de letras utilizadas
* 🎉 Pantalla de victoria
* 💀 Pantalla de derrota
* 🔄 Opción para comenzar una nueva partida
* 🖥️ Interfaz web mediante Streamlit

## 🛠️ Tecnologías utilizadas

* **Python**
* **Streamlit**
* **Random**

## 📁 Estructura del proyecto

```text
ahorcado/
│
├── app.py
└── README.md
```

## ⚙️ Instalación

Primero hay que tener Python instalado.

Luego instalar Streamlit:

```bash
pip install streamlit
```

## ▶️ Ejecutar el juego

Desde la carpeta del proyecto ejecutar:

```bash
streamlit run app.py
```

Streamlit abrirá automáticamente el juego en el navegador.

## 🎮 Cómo jugar

1. Elegir una categoría.
2. El juego seleccionará una palabra aleatoria.
3. La palabra aparecerá representada mediante guiones bajos.
4. Escribir una letra.
5. Presionar **"Probar letra"**.
6. Si la letra pertenece a la palabra, se mostrará.
7. Si la letra no pertenece a la palabra, se pierde un intento.
8. Se dispone de **6 intentos**.
9. Si se descubren todas las letras antes de quedarse sin intentos, se gana.
10. Si se terminan los intentos, se pierde.

## 📚 Categorías

Las palabras están almacenadas directamente en el código dentro de un diccionario de Python:

```python
categorias = {
    "🌎 Países": [...],
    "🎮 Videojuegos": [...],
    "🎬 Películas": [...],
    "📺 Series": [...],
    "🍥 Anime": [...],
    "🎵 Música": [...]
}
```

Cada vez que comienza una partida, se utiliza `random.choice()` para seleccionar una palabra aleatoria de la categoría elegida.

## 🧩 Funciones principales

### `nuevo_juego()`

Inicia una nueva partida y selecciona una palabra aleatoria.

```python
def nuevo_juego():
    categoria = st.session_state.categoria
    palabra = random.choice(categorias[categoria])

    st.session_state.palabra = palabra
    st.session_state.letras = []
    st.session_state.intentos = 6
    st.session_state.estado = "jugando"
```

### `st.session_state`

Se utiliza para guardar los datos de la partida mientras Streamlit vuelve a ejecutar el programa.

Se almacenan:

* La categoría.
* La palabra.
* Las letras utilizadas.
* Los intentos restantes.
* El estado del juego.

## 🔮 Posibles mejoras

Para futuras versiones se pueden agregar:

* 🪢 Dibujo del ahorcado.
* 🏆 Sistema de puntuación.
* 📊 Ranking de jugadores.
* 🔊 Efectos de sonido.
* 🎨 Mejor diseño visual.
* 🔥 Diferentes niveles de dificultad.
* 🌐 Utilización de una API para obtener palabras automáticamente.
* 💾 Guardado de estadísticas.
* 👥 Modo multijugador.

## 👨‍💻 Autor

Proyecto desarrollado como aplicación educativa utilizando **Python + Streamlit**.
