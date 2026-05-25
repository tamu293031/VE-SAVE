import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="VE SAVE", page_icon="⚡")

def obtener_datos():
    try:
        # Cargar credenciales desde los Secrets de Streamlit
        creds_dict = dict(st.secrets["gcp_service_account"])
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Abrir tu hoja de cálculo
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        
        return datos[0]['Hora'], datos[0]['Precio']
    except Exception as e:
        return "Conectando...", "..."

# --- Interfaz ---
st.markdown("<style>.stApp { text-align: center; }</style>", unsafe_allow_html=True)
st.title("⚡ VE SAVE")
horario, precio = obtener_datos()
st.info(f"### Hora más barata: {horario}")
st.success(f"### Precio: {precio} €/kWh")