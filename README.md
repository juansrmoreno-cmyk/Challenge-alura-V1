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
 
 contenido en carpeta prueba

📁 ACCESO AL PROYECTO 
https://github.com/juansrmoreno-cmyk/Challenge-alura-V1/tree/master

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

 📂 ESTRUCTURA DEL PROYECTO

Archivo / Carpeta	Descripción
app.py	Archivo principal de la aplicación. Contiene la interfaz desarrollada en Streamlit y gestiona la interacción entre el usuario y el sistema RAG.
rag_engine.py	Implementa la lógica del sistema RAG (Retrieval-Augmented Generation), incluyendo la creación de embeddings, la búsqueda en la base vectorial FAISS y la generación de respuestas mediante Google Gemini.
drive_sync.py	Se encarga de conectarse a Google Drive y descargar automáticamente el documento PDF que servirá como base de conocimiento del asistente.
docs/	Carpeta donde se almacenan los documentos PDF utilizados por el sistema como fuente de información.
vector_db/	Contiene la base de datos vectorial generada con FAISS, utilizada para realizar búsquedas semánticas sobre el contenido de los documentos.
requirements.txt	Archivo que lista todas las dependencias y bibliotecas necesarias para ejecutar correctamente el proyecto.
.env.example	Plantilla con las variables de entorno requeridas para configurar la aplicación sin exponer información confidencial.
.gitignore	Define los archivos y carpetas que Git debe ignorar para evitar subir información sensible o archivos temporales al repositorio.
credentials.json	Archivo con las credenciales de la cuenta de servicio de Google Cloud necesarias para acceder a Google Drive. No debe incluirse en el repositorio.
assets/	Carpeta destinada a almacenar imágenes, logotipos, capturas de pantalla y otros recursos gráficos utilizados en la aplicación o en el README.
README.md	Documento que describe el proyecto, su funcionamiento, instalación, tecnologías utilizadas y guía de uso para otros desarrolladores.
pycache/	Carpeta generada automáticamente por Python para almacenar archivos compilados, mejorando el rendimiento de la aplicación.

 

