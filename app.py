import streamlit as st
import requests

st.set_page_config(page_title="VE SAVE", page_icon="⚡")

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

def obtener_datos():
    try:
        # Usamos una API alternativa de confianza (precio luz hoy)
        url = "https://api.precioluz.com/v1/prices/all?zone=PCB"
        # Quitamos el timeout para dar margen de respuesta
        respuesta = requests.get(url).json()
        
        # Filtramos para buscar la hora más barata
        # Buscamos la hora con el precio mínimo
        mas_barata = min(respuesta, key=lambda x: float(x['price']))
        
        return f"{mas_barata['hour']}", f"{mas_barata['price']}€/kWh"
    except Exception as e:
        return "Error API", "Reintentar"

st.title("⚡ VE SAVE")
st.write("---")

horario, valor = obtener_datos()

st.subheader("Hora más barata hoy:")
st.info(f"### {horario}")

st.subheader("Precio en esa hora:")
st.success(f"### {valor}")