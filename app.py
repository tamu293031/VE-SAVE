import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="VE SAVE", page_icon="⚡")

def obtener_datos():
    try:
        # Construimos el diccionario de credenciales desde los Secrets por separado
        # Esto evita errores de lectura de archivos JSON complejos
        creds_dict = {
            "type": "service_account",
            "project_id": "vesave",
            "private_key_id": "75f7648fb07c1fba6d5ebdba7b6923e111ef0d16",
            "private_key": st.secrets["private_key"].replace('\\n', '\n'),
            "client_email": st.secrets["client_email"],
            "client_id": "109042466290475191662",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vesavebot%40vesave.iam.gserviceaccount.com"
        }
        
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        
        # Autenticación
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Conexión a la hoja
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        
        if datos:
            return datos[0]['Hora'], datos[0]['Precio']
        return "Vacío", "Sin datos"
        
    except Exception as e:
        return f"Error: {str(e)[:50]}", "Revisar configuración"

# --- INTERFAZ ---
st.title("⚡ VE SAVE")
horario, precio = obtener_datos()

st.info(f"Hora más barata: {horario}")
st.success(f"Precio: {precio}")