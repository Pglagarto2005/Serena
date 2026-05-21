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

# ===== HERO SECTION =====

col1, col2 = st.columns([1,1])

with col1:

    st.title("SERENA")

    st.subheader("No estás sola.")

    st.write("""
    Aplicación multimodal para el acompañamiento emocional
    en momentos de ansiedad.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    st.button("Comenzar")

with col2:

    st.image("Logo.png", width=400)

st.markdown("---")

# ===== TARJETAS =====

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background-color:#3D1366;
        padding:20px;
        border-radius:20px;
        text-align:center;
        height:220px;
    ">
        <h3 style="color:#F6E6B4;">Respiración</h3>
        <p>Ejercicios guiados para ayudarte a recuperar la calma.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background-color:#3D1366;
        padding:20px;
        border-radius:20px;
        text-align:center;
        height:220px;
    ">
        <h3 style="color:#F6E6B4;">Audio</h3>
        <p>Sonidos relajantes y acompañamiento emocional.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background-color:#3D1366;
        padding:20px;
        border-radius:20px;
        text-align:center;
        height:220px;
    ">
        <h3 style="color:#F6E6B4;">Apoyo</h3>
        <p>Interacciones simples para momentos difíciles.</p>
    </div>
    """, unsafe_allow_html=True)
