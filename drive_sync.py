import os
import io
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv

load_dotenv()

# Configuración
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'
FILE_ID =('1Fi4BTt1UHzfNmHvAsq0LP6vntduW7yMj')
DOWNLOAD_PATH = "documento_empresa.pdf"

def download_pdf_from_drive():
    print("Conectando a Google Drive...")
    
    try:
        # Autenticación con la cuenta de servicio
        creds = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        service = build('drive', 'v3', credentials=creds)
        
        request = service.files().get_media(fileId=FILE_ID)
        
        # Descarga el archivo en memoria y lo guarda en disco
        fh = io.FileIO(DOWNLOAD_PATH, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Descarga al {int(status.progress() * 100)}%.")
            
        print("✅ Documento descargado exitosamente de Google Drive.")
        return DOWNLOAD_PATH
        
    except Exception as e:
        print(f"❌ Error al descargar de Google Drive: {e}")
        return None

if __name__ == "__main__":
    # Para probar el script de forma independiente
    download_pdf_from_drive()