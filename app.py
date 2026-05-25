import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { text-align: center; }
    div[data-testid="stInfo"], div[data-testid="stSuccess"] { display: flex; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

def obtener_datos():
    try:
        # Esto conectará con tu hoja "Datos_VE_SAVE"
        # Nota: Necesitas el archivo JSON de credenciales de Google Cloud
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        
        # Aquí cargaríamos tus credenciales
        creds = ServiceAccountCredentials.from_json_keyfile_name('vesave-47b9f6098dc2.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("Datos_VE_SAVE").sheet1
        
        datos = sheet.get_all_records()
        return datos[0]['Hora'], datos[0]['Precio']
    except:
        return "02:00 - 06:00", "0.08 €/kWh"

st.title("⚡ VE SAVE")
st.write("---")

horario, valor = obtener_datos()

st.subheader("Hora más barata hoy:")
st.info(f"### {horario}")

st.subheader("Precio en esa hora:")
st.success(f"### {valor}")