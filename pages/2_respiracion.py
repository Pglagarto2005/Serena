import streamlit as st

st.set_page_config(
    page_title="Respira | Serena",
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

/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #2B0A57;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* HEADER */

[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    visibility:hidden;
}

/* TÍTULOS */

h1 {
    color: white;
    text-align:center;
    font-size:70px !important;
    margin-top: 20px;
}

p {
    color:white;
    text-align:center;
    font-size:24px;
}

/* CÍRCULO */

.circle {

    width: 320px;
    height: 320px;

    border-radius: 50%;

    margin: auto;
    margin-top: 60px;

    background: radial-gradient(circle, #ff7ca2, #ff5e8a);

    box-shadow:
    0 0 40px #ff5e8a,
    0 0 80px #ff5e8a,
    0 0 120px rgba(255, 94, 138, 0.5);

    animation: breathe 8s infinite ease-in-out;
}

@keyframes breathe {

    0% {
        transform: scale(0.8);
    }

    50% {
        transform: scale(1.2);
    }

    100% {
        transform: scale(0.8);
    }
}

/* TEXTO RESPIRACIÓN */

.instruccion {

    text-align:center;
    color:#F6E6B4;
    font-size:48px;
    margin-top:40px;
    font-weight:bold;
    letter-spacing: 2px;

    animation: pulseText 8s infinite;
}

@keyframes pulseText {

    0% {
        opacity:0.4;
        transform: scale(0.95);
    }

    50% {
        opacity:1;
        transform: scale(1.08);
    }

    100% {
        opacity:0.4;
        transform: scale(0.95);
    }
}

/* BOTÓN */

div.stButton > button {

    background-color:#FF5E8A;
    color:white;

    border:none;
    border-radius:25px;

    padding:16px 40px;

    font-size:22px;
    font-weight:bold;

    display:block;
    margin:auto;

    transition:0.3s;

    box-shadow: 0 0 20px rgba(255, 94, 138, 0.4);
}

div.stButton > button:hover {

    background-color:#ff7ca2;

    transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====

st.title("Respira conmigo")

st.write("No necesitas resolver todo ahora.")

st.markdown("""
<div class="circle"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="instruccion">
INHALA • EXHALA
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.button("Comenzar ejercicio")
