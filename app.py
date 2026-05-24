import streamlit as st

st.title("Mi SaaS en la Nube")
st.write("¡Esto funciona sin instalar nada en mi Windows 7!")

nombre = st.text_input("¿Cómo te llamas?")
if st.button("Saludar"):
    st.write(f"Hola {nombre}, bienvenido a tu SaaS.")
