import os
import streamlit as st
from dotenv import load_dotenv

# Importamos las funciones de nuestros scripts anteriores
from drive_sync import download_pdf_from_drive
from rag_engine import update_vector_db, get_answer

load_dotenv()

# Configuración de la página web
st.set_page_config(page_title="Asistente Corporativo IA", page_icon="🤖", layout="wide")

# --- BARRA LATERAL (Panel de Administración) ---
st.sidebar.title("Configuración y Soporte")
st.sidebar.markdown("---")

# Sección de autenticación para el Administrador (Opción A)
st.sidebar.subheader("🔐 Área de Administración")
admin_password_input = st.sidebar.text_input("Contraseña de Admin", type="password")

# Validamos la contraseña contra la definida en el archivo .env
if admin_password_input == os.getenv("ADMIN_PASSWORD"):
    st.sidebar.success("Acceso concedido")
    st.sidebar.markdown("Use el siguiente botón para sincronizar la base de conocimiento con el documento oficial en Google Drive.")
    
    # Botón exclusivo para ejecutar la sincronización
    if st.sidebar.button("🔄 Sincronizar con Google Drive"):
        with st.sidebar.status("Procesando...", expanded=True) as status:
            st.write("Descargando el PDF desde Google Drive...")
            pdf_file = download_pdf_from_drive()
            
            if pdf_file:
                st.write("Actualizando base de datos vectorial (Embeddings)...")
                try:
                    update_vector_db()
                    status.update(label="Sincronización Exitosa ✅", state="complete", expanded=False)
                    st.sidebar.success("PDF descargado")
                except Exception as e:
                    status.update(label="Error en procesamiento ❌", state="error")
                    st.sidebar.error(f"Error al indexar el PDF: {e}")
            else:
                status.update(label="Error de descarga ❌", state="error")
                st.sidebar.error("No se pudo descargar el archivo de Drive. Revisa las credenciales.")
elif admin_password_input:
    st.sidebar.error("Contraseña incorrecta")

# --- CUERPO PRINCIPAL (Chat del Usuario) ---
st.title("🤖 Hola me llamo ALEJA asistente virtual de Banco Krea ")
st.markdown("Bienvenido al sistema de consultas internas. Pregúntame sobre cualquier normativa, proceso o documentación oficial de la organización.")
st.markdown("---")

# Verificar si la base de datos vectorial ya existe en el servidor
if not os.path.exists("./vector_db"):
    st.warning("⚠️ La base de conocimiento está vacía. Un administrador debe ingresar la contraseña en la barra lateral y sincronizar los datos por primera vez.")

# Inicializar el historial de conversación en la sesión de Streamlit si no existe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes anteriores del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar la pregunta del usuario
if user_query := st.chat_input("Escribe tu consulta aquí..."):
    # Mostrar la pregunta del usuario inmediatamente en pantalla
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Guardar la pregunta en el historial
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Generar la respuesta usando el motor RAG
    with st.chat_message("assistant"):
        with st.spinner("Buscando en la documentación oficial..."):
            try:
                response = get_answer(user_query)
                st.markdown(response)
                # Guardar la respuesta en el historial
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Lo siento, ocurrió un error al procesar tu consulta: {e}"
                st.markdown(error_msg)