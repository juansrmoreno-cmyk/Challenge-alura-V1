import io
import json
import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import streamlit as st

load_dotenv()

# Configuración
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FILE_ID = '19_fb-Gx2eGIS2bsCjb3gPjLYru-vtNeA'
DOWNLOAD_PATH = 'documento_empresa.pdf'


def get_credentials():
  """Obtiene las credenciales ya sea desde Streamlit Secrets (en la nube)

  o desde el archivo credentials.json local (en tu PC).
  """
  # 1. Si estamos en Streamlit Cloud y existen los secretos de GCP
  if hasattr(st, 'secrets') and 'gcp_service_account' in st.secrets:
    creds_dict = dict(st.secrets['gcp_service_account'])
    # Corregir saltos de línea de la llave privada si vienen con \n en texto
    if 'private_key' in creds_dict:
      creds_dict['private_key'] = creds_dict['private_key'].replace('\\n', '\n')
    return Credentials.from_service_account_info(creds_dict, scopes=SCOPES)

  # 2. Si estamos en local y existe el archivo físico
  elif os.path.exists('credentials.json'):
    return Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

  else:
    raise FileNotFoundError(
        'No se encontraron credenciales ni en st.secrets ni como archivo'
        ' local.'
    )


def download_pdf_from_drive():
  print('Conectando a Google Drive...')

  try:
    # Autenticación inteligente (Nube o Local)
    creds = get_credentials()

    service = build('drive', 'v3', credentials=creds)

    request = service.files().get_media(fileId=FILE_ID)

    # Descarga el archivo en memoria y lo guarda en disco
    fh = io.FileIO(DOWNLOAD_PATH, mode='wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print(f'Descarga al {int(status.progress() * 100)}%.')

    print('✅ Documento descargado exitosamente de Google Drive.')
    return DOWNLOAD_PATH

  except Exception as e:
    print(f'❌ Error al descargar de Google Drive: {e}')
    return None


if __name__ == '__main__':
  # Para probar el script de forma independiente
  download_pdf_from_drive()