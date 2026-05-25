import streamlit as st
import requests

# 1. Configuración obligatoria al principio
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

# 2. CSS forzado para centrar todo
st.markdown("""
    <style>
    .stApp { text-align: center; }
    div[data-testid="stInfo"], div[data-testid="stSuccess"] { 
        display: flex; 
        justify-content: center; 
    }
    h1, h2, h3 { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. Función de datos
def obtener_datos():
    try:
        url = "https://api.precioluz.com/v1/prices/cheapesthour?zone=PCB"
        # Ajustamos el timeout para que no bloquee la web
        respuesta = requests.get(url, timeout=10).json()
        
        hora = respuesta.get('hour', 'Error')
        precio = respuesta.get('price', '0.00')
        return f"{hora}:00", f"{precio}€/kWh"
    except:
        return "Sin conexión", "Revisando..."

# 4. Interfaz
st.title("⚡ VE SAVE")
st.write("---")

horario, valor = obtener_datos()

st.subheader("Hora más barata hoy:")
st.info(f"### {horario}")

st.subheader("Precio en esa hora:")
st.success(f"### {valor}")