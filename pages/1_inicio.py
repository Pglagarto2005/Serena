import streamlit as st

st.set_page_config(
    page_title="Serena",
    page_icon="Logo.png",
    layout="wide"
)

# ===== ESTILOS =====

st.markdown("""
<style>

.stApp {
    background-color: #2B0A57;
    color: white;
}

h1 {
    color: #F6E6B4;
    text-align:center;
    font-size:60px !important;
}

p {
    color:white;
    font-size:20px;
}

[data-testid="stSidebar"] {
    background-color: #220046;
}

div.stButton > button {
    width:100%;
    border-radius:20px;
    border:none;
    background-color:#FF5E8A;
    color:white;
    font-size:20px;
    font-weight:bold;
    padding:15px;
}

div.stButton > button:hover {
    background-color:#ff7ca2;
}

</style>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====

st.title("¿Cómo te sientes hoy?")

st.markdown("""
<div style="
text-align:center;
font-size:24px;
margin-bottom:40px;
">
Estoy aquí contigo.
</div>
""", unsafe_allow_html=True)

# ===== IMAGEN =====

st.image("Logo.png", width=280)

st.markdown("<br>", unsafe_allow_html=True)

# ===== BOTONES =====

col1, col2 = st.columns(2)

with col1:

    if st.button("😣 Ansiedad"):
        st.success("Respira conmigo. Esto pasará.")

    if st.button("😞 Tristeza"):
        st.info("No tienes que cargar todo sola.")

with col2:

    if st.button("😵 Abrumada"):
        st.warning("Vamos paso a paso.")

    if st.button("😤 Estrés"):
        st.success("Tu cuerpo necesita calma, no presión.")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
text-align:center;
font-size:28px;
color:#F6E6B4;
font-weight:bold;
">
No estás sola.
</div>
""", unsafe_allow_html=True)
