# 🦜🔗 Ask the Doc App

Una aplicación simple construida con **Streamlit** y **LangChain** que permite hacer preguntas sobre un archivo de texto cargado, utilizando un modelo de lenguaje de OpenAI para responder de forma contextual.

---

## 🚀 Características
# 🦜🔗 Ask the Doc App

Una aplicación simple construida con **Streamlit** y **LangChain** que permite hacer preguntas sobre un archivo de texto cargado, utilizando un modelo de lenguaje de OpenAI para responder de forma contextual.

---

## 🚀 Características

* Carga archivos `.txt`
* Divide el texto en fragmentos manejables
* Utiliza embeddings de OpenAI
* Construye un vectorstore con FAISS para recuperación de contexto
* Permite hacer preguntas en lenguaje natural sobre el documento cargado

---

## 📦 Requisitos

### Entorno local

```bash
pip install -r requirements.txt
```

### Contenido del `requirements.txt`

```txt
streamlit
openai
tiktoken
langchain-community
langchain-openai
protobuf==3.20.3
faiss-cpu
langchain>=0.1.0
```

---

## 🛠 Estructura del Proyecto

```
project-llm-app/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🔐 Uso de Claves API con Streamlit Cloud

Para proteger tu clave API de OpenAI y evitar exponerla en el frontend o en el repositorio, este proyecto utiliza el sistema de **secrets** de [Streamlit Cloud](https://streamlit.io/cloud).

### Configurar secretos

1. **Usar variable de entorno en el código**

   En `streamlit_app.py`, reemplaza:

   ```python
   openai_api_key = st.text_input('OpenAI API Key', type='password')
   ```

   por:

   ```python
   import os
   openai_api_key = os.getenv("OPENAI_API_KEY")
   ```

2. **Agregar secreto en Streamlit Cloud**

   * Ve a tu app en [https://streamlit.io/cloud](https://streamlit.io/cloud)
   * Click en **"Manage app"** > **"Secrets"**
   * Pega el siguiente contenido:

     ```toml
     OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
     ```

3. **Guardar y reiniciar la app**

---

## ▶️ Ejecución local

```bash
streamlit run streamlit_app.py
```

Abre tu navegador en: `http://localhost:8501`

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Libre de usar, modificar y distribuir con fines educativos o comerciales.

---

## 🙌 Agradecimientos

* [Streamlit](https://streamlit.io)
* [LangChain](https://www.langchain.com/)
* [OpenAI](https://openai.com)

---

Hecho con 💡 para explorar el poder de los LLMs sobre documentos propios.

* Carga archivos `.txt`
* Divide el texto en fragmentos manejables
* Utiliza embeddings de OpenAI
* Construye un vectorstore con FAISS para recuperación de contexto
* Permite hacer preguntas en lenguaje natural sobre el documento cargado

---

## 📦 Requisitos

### Entorno local

```bash
pip install -r requirements.txt
```

### Contenido del `requirements.txt`

```txt
streamlit
openai
tiktoken
langchain-community
langchain-openai
protobuf==3.20.3
faiss-cpu
langchain>=0.1.0
```

---

## 🛠 Estructura del Proyecto

```
project-llm-app/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🔐 Uso de Claves API con Streamlit Cloud

Para proteger tu clave API de OpenAI y evitar exponerla en el frontend o en el repositorio, este proyecto utiliza el sistema de **secrets** de [Streamlit Cloud](https://streamlit.io/cloud).

### Configurar secretos

1. **Usar variable de entorno en el código**

   En `streamlit_app.py`, reemplaza:

   ```python
   openai_api_key = st.text_input('OpenAI API Key', type='password')
   ```

   por:

   ```python
   import os
   openai_api_key = os.getenv("OPENAI_API_KEY")
   ```

2. **Agregar secreto en Streamlit Cloud**

   * Ve a tu app en [https://streamlit.io/cloud](https://streamlit.io/cloud)
   * Click en **"Manage app"** > **"Secrets"**
   * Pega el siguiente contenido:

     ```toml
     OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
     ```

3. **Guardar y reiniciar la app**

---

## ▶️ Ejecución local

```bash
streamlit run streamlit_app.py
```

Abre tu navegador en: `http://localhost:8501`

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Libre de usar, modificar y distribuir con fines educativos o comerciales.

---

## 🙌 Agradecimientos

* [Streamlit](https://streamlit.io)
* [LangChain](https://www.langchain.com/)
* [OpenAI](https://openai.com)

---

Hecho con 💡 para explorar el poder de los LLMs sobre documentos propios.

