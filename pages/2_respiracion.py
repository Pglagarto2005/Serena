import streamlit as st
import time

st.title("Respiración Guiada")

st.write("Sigue el ritmo de respiración.")

if st.button("Iniciar respiración"):

    st.success("Inhala profundamente")

    time.sleep(4)

    st.info("Exhala lentamente")
