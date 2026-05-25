import streamlit as st

# Configuración de página
st.set_page_config(page_title="VE SAVE", page_icon="⚡")

# CSS para forzar centrado total en todos los elementos
st.markdown("""
    <style>
    /* Centra el contenedor principal */
    .stApp { text-align: center; }
    
    /* Centra los bloques de información de Streamlit */
    div[data-testid="stInfo"] { display: flex; justify-content: center; }
    div[data-testid="stSuccess"] { display: flex; justify-content: center; }
    
    /* Centra los textos */
    h1, h2, h3 { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ ---
st.title("⚡ VE SAVE")
st.write("---")

st.subheader("Horario óptimo hoy:")
st.info("### 02:00 - 06:00")

st.subheader("Ahorro estimado:")
st.success("### 2.40€")