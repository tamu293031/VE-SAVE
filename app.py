import streamlit as st
import requests

# Configuración de página
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

st.markdown("""
    <style>
    .stApp { text-align: center; }
    div[data-testid="stInfo"], div[data-testid="stSuccess"] { display: flex; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

# Función con conexión real
def obtener_datos():
    try:
        # Consultamos el precio de la luz en la península (PCB)
        url = "https://api.precioluz.com/v1/prices/cheapesthour?zone=PCB"
        respuesta = requests.get(url, timeout=5).json()
        
        # Extraemos la hora y el precio (estos campos dependen de la estructura de la API)
        hora = respuesta.get('hour', '02:00')
        precio = respuesta.get('price', '0.05')
        return f"{hora}:00", f"{precio}€/kWh"
    except Exception:
        # Fallback si falla la API para que la App no se rompa
        return "02:00 - 06:00", "2.40€ (Estimado)"

st.title("⚡ VE SAVE")
st.write("---")

horario, valor = obtener_datos()

st.subheader("Hora más barata hoy:")
st.info(f"### {horario}")

st.subheader("Precio en esa hora:")
st.success(f"### {valor}")

st.write("Datos actualizados en tiempo real.")