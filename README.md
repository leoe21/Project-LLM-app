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

## 🚀 Despliegue en AWS EC2

### 1. Lanza una instancia EC2

- Elige **Amazon Linux 2023** o **Ubuntu 22.04** como AMI.
- Tipo de instancia recomendado: `t2.micro` (gratis primer año) o `t2.medium`.
- Crea un **par de claves (.pem)** y descárgalo.
- Abre los siguientes puertos en el grupo de seguridad:
  - **22** (SSH) — solo tu IP si es posible.
  - **8501** (Streamlit) — 0.0.0.0/0 para acceso público.
  - **(Opcional) 80/443** si usarás Nginx o HTTPS.

### 2. Conéctate por SSH

```bash
ssh -i streamlit.pem ec2-user@<IP_PUBLICA>
# Para Ubuntu, usa: ssh -i streamlit.pem ubuntu@<IP_PUBLICA>
```

### 3. Instala dependencias en la instancia

```bash
sudo yum update -y
sudo yum install -y python3 python3-pip git
sudo yum groupinstall -y "Development Tools"
sudo yum install -y python3-devel
```

### 4. Sube tu proyecto o clónalo desde GitHub

```bash
# Si tienes el proyecto en GitHub:
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

# O sube los archivos con SCP:
# scp -i streamlit.pem -r /ruta/a/tu/Project-LLM-app ec2-user@<IP_PUBLICA>:~/
```

### 5. Crea y activa un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Instala las dependencias del proyecto

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 7. Configura los secretos de Streamlit

```bash
mkdir -p .streamlit
nano .streamlit/secrets.toml
```
Agrega tu clave de OpenAI:
```toml
OPENAI_API_KEY = "tu-api-key"
```

### 8. Ejecuta la aplicación Streamlit

```bash
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

- Deja la terminal abierta mientras la app esté en uso.
- Accede desde tu navegador a:  
  `http://<IP_PUBLICA>:8501`

### 9. (Opcional) Deja la app corriendo en segundo plano

```bash
nohup streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0 &
```

---

**¡Listo! Tu aplicación Streamlit estará disponible públicamente en AWS EC2.**

## 🚀 Despliegue en AWS ECS con Docker y Fargate

### 1. Prepara tu proyecto para Docker

- Crea un archivo `Dockerfile` en la raíz del proyecto:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

- (Opcional) Crea un `.dockerignore` para evitar copiar archivos innecesarios:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.venv/
venv/
.env
*.db
*.sqlite3
.DS_Store
.git
```

### 2. Construye y prueba tu imagen Docker localmente

```bash
docker build -t my-streamlit-app .
docker run -p 8501:8501 my-streamlit-app
```

### 3. Sube tu imagen a Amazon ECR

- Crea un repositorio en ECR (ej: `my-streamlit-app`).
- Haz login en ECR:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 116981772459.dkr.ecr.us-east-1.amazonaws.com
```

- Etiqueta y sube tu imagen:

```bash
docker tag my-streamlit-app:latest 116981772459.dkr.ecr.us-east-1.amazonaws.com/my-streamlit-app:latest
docker push 116981772459.dkr.ecr.us-east-1.amazonaws.com/my-streamlit-app:latest
```

### 4. Crea un clúster en ECS (Fargate)

- Ve a ECS → Clústeres → Crear clúster → "Networking only (Fargate)".
- Ponle un nombre (ej: `streamlit-cluster`).

### 5. Crea una Task Definition

- Ve a ECS → Definiciones de tareas → Crear nueva definición de tarea → Fargate.
- Agrega un contenedor:
  - **Nombre:** streamlit
  - **Imagen:** `116981772459.dkr.ecr.us-east-1.amazonaws.com/my-streamlit-app:latest`
  - **Puerto:** 8501 (TCP)
  - **Variables de entorno:** Agrega `OPENAI_API_KEY` con tu clave de OpenAI.
- Asigna memoria y CPU según lo requiera tu app.

### 6. Crea un Servicio en ECS

- Ve a tu clúster → Crear servicio.
- Tipo de lanzamiento: Fargate
- Task Definition: la que creaste
- Número de tareas: 1
- Selecciona una VPC y subred pública
- Grupo de seguridad: permite el puerto 8501 (TCP, 0.0.0.0/0)
- (Opcional) Configura un Load Balancer si quieres acceso por HTTP estándar

### 7. Accede a tu aplicación

- Ve a la pestaña de tareas en tu servicio.
- Copia la IP pública de la tarea (o el DNS del Load Balancer si usaste uno).
- Accede en tu navegador a:
  ```
  http://<IP_PUBLICA>:8501
  ```
  o
  ```
  http://<DNS_DEL_ALB>
  ```

---

**¡Listo! Tu aplicación Streamlit estará disponible públicamente en AWS ECS usando Docker y Fargate.**

