import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="VE SAVE", page_icon="⚡")

def obtener_datos():
    try:
        # Convertimos los secretos a diccionario
        creds_dict = dict(st.secrets["gcp_service_account"])
        
        # Scope necesario para Google Sheets
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        
        # Conexión
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Acceso a la hoja (asegúrate de que el nombre sea el mismo en Drive)
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        
        if datos:
            return datos[0]['Hora'], datos[0]['Precio']
        return "Sin datos", "..."
        
    except Exception as e:
        return f"Error: {e}", "..."

st.title("⚡ VE SAVE")
horario, precio = obtener_datos()
st.info(f"Hora más barata: {horario}")
st.success(f"Precio: {precio}")