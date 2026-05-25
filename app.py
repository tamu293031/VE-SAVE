import streamlit as st

# Configuración de página
st.set_page_config(page_title="Smart Charge VE", page_icon="⚡")

# Estilos CSS
st.markdown("""
    <style>
    .stApp { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ LIMPIA ---
st.title("⚡ Smart Charge VE")
st.write("---")

# Aquí solo llamamos a los elementos una vez
st.subheader("Horario óptimo hoy:")
st.info("### 02:00 - 06:00")

st.subheader("Ahorro estimado:")
st.success("### 2.40€")