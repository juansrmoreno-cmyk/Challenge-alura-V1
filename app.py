import os
import streamlit as st
from dotenv import load_dotenv

# Importamos las funciones de nuestros scripts anteriores
from drive_sync import download_pdf_from_drive
from rag_engine import update_vector_db, get_answer

load_dotenv()

# Configuración de la página web
st.set_page_config(page_title="Banco Crea", page_icon="🏢", layout="wide")

# --- BARRA LATERAL
st.sidebar.title("Configuración y Soporte")
st.sidebar.markdown("---")

# Sección de autenticación para el Administrador 
st.sidebar.subheader("🔐 Área de Administración")
admin_password_input = st.sidebar.text_input("Contraseña de Admin", type="password")

# Validamos la contraseña contra la definida en el archivo 
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
st.title("🏢 Banco Krea ")
st.markdown("🧔🏼‍♀️ Hola me llamo ALEJA asistente virtual de Banco Krea.")
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
                st.markdown(error_msg),
                import streamlit as st

st.markdown("""
<style>

/* ===== Fondo principal ===== */
.stApp{
    background:
        radial-gradient(circle at top right, rgba(37,99,235,0.35), transparent 35%),
        radial-gradient(circle at bottom left, rgba(14,165,233,0.20), transparent 35%),
        linear-gradient(135deg,#071426 0%,#0B1F3A 45%,#123A6D 100%);
    background-attachment: fixed;
}
            
            /* ======= Barra Lateral =====*/
section[data-testid="stSidebar"]{
    min-width:420px !important;
    max-width:420px !important;
    background: rgba(8,18,35,.92);
    backdrop-filter: blur(18px);
}

section[data-testid="stSidebar"] > div{
    width:420px !important;
}

.titulo-principal{
    color:white;
    font-size:70px;
    font-weight:800;
    margin-left:300px;
}
/* Subtítulo */
.subtitulo{
    color:#E2E8F0;
    font-size:22px;
    font-weight:600;
    text-align:center;
    margin-bottom:20px;
}

/* Título de la barra lateral */
.titulo-sidebar{
    color:white;
    font-size:38px;
    font-weight:800;
    text-align:center;
}

/* Área de administración */
.titulo-admin{
    color:white;
    font-size:28px;
    font-weight:700;
}

/* Texto normal */
.descripcion{
    color:#d1d5db;
    font-size:18px;
}
}

/* ===== Texto ===== */
p,span,label{
    color:#E2E8F0 !important;
    font-size:16px;
}

/* ===== Tarjetas ===== */
div[data-testid="stVerticalBlock"]{
    background:rgba(255,255,255,.04);
    border-radius:18px;
    padding:15px;
}

/* ===== Chat ===== */
.stChatMessage{
    background:rgba(255,255,255,.07);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.10);
    border-radius:10px;
    padding:15px;
    margin-bottom:10px;
}

/* Contenedor principal */
[data-testid="stChatInput"]{
    max-width: 900px !important;
    margin: auto !important;
}

/* Contenedor interno */
[data-testid="stChatInput"] > div{
    max-width: 900px !important;
    margin: auto !important;
}
}

/* ===== Botones ===== */
.stButton>button{
    background:linear-gradient(90deg,#1D4ED8,#2563EB,#3B82F6);
    color:white;
    border:black;
    border-radius:10px;
    padding:10px 10px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0 10px 25px rgba(37,99,235,.45);
}

/* ===== Inputs ===== */
input{
    border-radius:12px !important;
}

/* ===== Alertas ===== */
.stAlert{
    border-radius:15px;
}

/* ===== Scroll ===== */
::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#2563EB;
    border-radius:10px;
}
            /* Campo de contraseña */
.stTextInput{
    max-width: 320px;
}

.stTextInput > div > div > input{
    height: 40px;
    border-radius: 10px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)