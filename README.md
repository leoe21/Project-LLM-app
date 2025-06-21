# 🦜🔗 Ask the Doc App

Una aplicación web construida con [Streamlit](https://streamlit.io/) que permite subir un archivo `.txt` y hacerle preguntas utilizando un modelo de lenguaje (OpenAI GPT) mediante recuperación de información.

---

## 🚀 ¿Qué hace esta app?

1. Carga un archivo `.txt` con contenido.
2. Lo divide en fragmentos para facilitar el procesamiento.
3. Usa **embeddings de OpenAI** para vectorizar el contenido.
4. Almacena los vectores en **FAISS** (vector store).
5. Permite al usuario hacer preguntas y recupera la respuesta relevante del texto.

---

## 📦 Requisitos

Se instalan automáticamente en [Streamlit Cloud](https://streamlit.io/cloud), pero si lo ejecutas localmente:

```bash
pip install -r requirements.txt
