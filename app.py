import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def obtener_datos():
    try:
        # Cargamos los secretos
        creds_dict = dict(st.secrets["gcp_service_account"])
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        
        # Autorización
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Abrir hoja
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        return datos[0]['Hora'], datos[0]['Precio']
    except Exception as e:
        return f"Error: {e}", "..."

st.title("⚡ VE SAVE")
horario, precio = obtener_datos()
st.info(f"Hora: {horario}")
st.success(f"Precio: {precio}")