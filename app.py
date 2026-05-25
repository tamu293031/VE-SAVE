import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración básica
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

def obtener_datos():
    try:
        # 1. Verificar si existen los secretos
        if "gcp_service_account" not in st.secrets:
            return "Error: Secrets no encontrados", "Revisar configuración en Streamlit"

        # 2. Cargar credenciales
        creds_dict = dict(st.secrets["gcp_service_account"])
        # Necesario corregir saltos de línea en la clave privada
        creds_dict['private_key'] = creds_dict['private_key'].replace('\\n', '\n')
        
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # 3. Conectar a la hoja (asegúrate de que el nombre sea exacto)
        sheet = client.open("Datos_VE_SAVE").sheet1
        datos = sheet.get_all_records()
        
        if not datos:
            return "Hoja vacía", "Revisar datos en Sheets"
            
        return datos[0]['Hora'], datos[0]['Precio']

    except Exception as e:
        # Esto nos mostrará el error exacto en pantalla si algo falla
        return f"Error: {type(e).__name__}", str(e)

# --- INTERFAZ ---
st.markdown("<style>.stApp { text-align: center; }</style>", unsafe_allow_html=True)
st.title("⚡ VE SAVE")
horario, precio = obtener_datos()

st.info(f"### Hora más barata: {horario}")
st.success(f"### Precio: {precio}")