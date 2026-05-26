import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de la página
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

def obtener_datos():
    try:
        # Construimos el diccionario de credenciales utilizando los secretos
        # Usamos replace('\\n', '\n') para asegurar que la clave privada sea válida
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
        
        # Definimos los alcances necesarios para Google Sheets
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        
        # Autenticación y conexión
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Abrimos la hoja de cálculo por su nombre exacto
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        
        # Retornamos los valores de la primera fila
        if datos:
            return datos[0]['Hora'], datos[0]['Precio']
        return "Sin datos", "..."
        
    except Exception as e:
        # Mostramos el error resumido para poder depurar
        return f"Error: {str(e)[:50]}", "Revisar configuración"

# --- INTERFAZ DE USUARIO ---
st.title("⚡ VE SAVE")

# Obtenemos los datos
horario, precio = obtener_datos()

# Mostramos los resultados
st.info(f"Hora más barata: {horario}")
st.success(f"Precio: {precio}")