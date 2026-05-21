import streamlit as st

st.set_page_config(
    page_title="Serena",
    page_icon="Logo.png",
    layout="centered"
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
    text-align: center;
    font-size: 70px !important;
    font-weight: 800;
}

h2, h3 {
    color: #F6E6B4;
}

p {
    color: white;
    font-size: 20px;
}

[data-testid="stSidebar"] {
    background-color: #220046;
}

.stButton>button {
    background-color: #FF5E8A;
    color: white;
    border-radius: 20px;
    border: none;
    padding: 12px 30px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #ff7ca2;
    transform: scale(1.05);
}

.block-container {
    padding-top: 2rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====

st.title("SERENA")

st.subheader("No estás sola.")

st.write("""
Aplicación multimodal para el acompañamiento emocional
en momentos de ansiedad.
""")

st.image("Logo.png", width=300)

st.markdown("---")

st.write("""
SERENA utiliza:
- respiración guiada
- interacción visual
- sonidos relajantes
- apoyo emocional inmediato
""")

st.button("Comenzar")
