import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def obtener_datos():
    try:
        # Limpieza agresiva de la clave privada
        raw_key = st.secrets["private_key"]
        clean_key = raw_key.replace("\\n", "\n").replace("\r", "").strip()
        
        creds_dict = {
            "type": "service_account",
            "project_id": "vesave",
            "private_key_id": "75f7648fb07c1fba6d5ebdba7b6923e111ef0d16",
            "private_key": clean_key,
            "client_email": st.secrets["client_email"],
            "client_id": "109042466290475191662",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vesavebot%40vesave.iam.gserviceaccount.com"
        }
        
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        return datos[0]['Hora'], datos[0]['Precio']
        
    except Exception as e:
        return f"Error: {str(e)[:50]}", "Revisar configuración"

st.title("⚡ VE SAVE")
horario, precio = obtener_datos()
st.info(f"Hora más barata: {horario}")
st.success(f"Precio: {precio}")