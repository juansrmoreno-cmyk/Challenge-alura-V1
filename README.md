
BANCO KREA

Aleja es un asistente Inteligente basado en Inteligencia Artificial y Arquitectura RAG para responder consultas sobre la documentación del Banco Krea.

📖 INDICE

- Descripción del proyecto
- Estado del proyecto
- Funcionalidades
- Demostración
- Acceso al proyecto
- Tecnologías utilizadas
- Arquitectura
- Instalación
- Configuración
- Ejecución
- Estructura del proyecto
- Autor
- Licencia

📌 DESCRIPCION DEL PROYECTO

Banco Krea tiene una inteligencia artificial llamada aleja, es una aplicación web desarrollada en **Python** que implementa una arquitectura **RAG (Retrieval-Augmented Generation)** para responder preguntas sobre la documentación institucional del Banco Krea.

La aplicación descarga automáticamente documentos PDF desde Google Drive, procesa su contenido mediante embeddings de Google Gemini, almacena la información en una base vectorial FAISS y responde preguntas utilizando inteligencia artificial generativa.

Su objetivo es facilitar el acceso rápido a la información institucional sin necesidad de revisar manualmente documentos extensos.

🚧 ESTADO DEL PROYECTO
Actualmente el proyecto cuenta con las siguientes funcionalidades implementadas:

- ✅ Interfaz web desarrollada con Streamlit.
- ✅ Sincronización de documentos PDF desde Google Drive.
- ✅ Procesamiento y segmentación de documentos.
- ✅ Generación de embeddings mediante Google Gemini.
- ✅ Almacenamiento de información en una base vectorial FAISS.
- ✅ Recuperación semántica utilizando arquitectura RAG.
- ✅ Respuesta a preguntas basadas en el contenido de los documentos.

 Próximas mejoras

- 🔄 Optimizar el rendimiento de las consultas.
- 🔄 Mejorar el manejo de errores y excepciones.
- 🔄 Incorporar autenticación para administradores.
- 🔄 Permitir la carga de múltiples documentos PDF.
- 🔄 Despliegue en un servicio en la nube (Streamlit Community Cloud, Render o similar).

🔨FUNCIONALIDADES

✔️ Descarga automática del documento desde Google Drive.

✔️ Procesamiento del contenido del PDF.

✔️ División inteligente del documento en fragmentos.

✔️ Generación de embeddings utilizando Google Gemini.

✔️ Creación automática de una base vectorial FAISS.

✔️ Recuperación de información mediante búsqueda semántica.

✔️ Respuestas generadas por IA utilizando únicamente el contexto encontrado.

✔️ Interfaz web desarrollada con Streamlit.

 📷 DEMOSTRACION
 
 contenido en carpeta Demostraciones

📁 ACCESO AL PROYECTO 
https://github.com/juansrmoreno-cmyk/Challenge-alura-V1/tree/master
ADMIN_PASSWORD= Bancokrea1*

🔗LINK DEL PROYECTO 
https://challenge-alura-v1.streamlit.app/

🛠️ TECNOLOGIAS UTILIZADAS

- Python 3.11
- Streamlit
- LangChain
- Google Gemini API
- Google AI Embeddings
- Google Drive API
- FAISS
- PyPDF
- Python Dotenv
- Git
- GitHub

 🧠ARQUITECTURA

Usuario

     │

     ▼

Streamlit

     │

     ▼

Pregunta

     │

     ▼

Retriever (FAISS)

     │

     ▼

Fragmentos relevantes

     │

     ▼

Google Gemini

     │

     ▼

Respuesta

📂 Estructura del proyecto

| 📁 Archivo / Carpeta | 📄 Descripción |
|----------------------|----------------|
| `app.py` | Punto de entrada de la aplicación. Contiene la interfaz desarrollada con **Streamlit** y gestiona la interacción con el usuario. |
| `rag_engine.py` | Implementa la arquitectura **RAG**, realiza la búsqueda semántica en FAISS y genera respuestas utilizando **Google Gemini**. |
| `drive_sync.py` | Descarga y sincroniza automáticamente el documento PDF almacenado en Google Drive. |
| `docs/` | Contiene la documentación del Banco Krea utilizada como fuente de conocimiento del asistente. |
| `vector_db/` | Almacena la base de datos vectorial generada por **FAISS** para realizar búsquedas semánticas. |
| `requirements.txt` | Lista todas las dependencias necesarias para ejecutar el proyecto. |
| `.env.example` | Archivo de ejemplo con las variables de entorno requeridas para la configuración. |
| `.gitignore` | Define los archivos y carpetas que Git debe ignorar para proteger información sensible y archivos temporales. |
| `assets/` | Carpeta destinada a imágenes, capturas de pantalla y demás recursos utilizados en el README. |
| `README.md` | Documentación principal del proyecto, incluyendo instalación, uso y tecnologías empleadas. |
 

