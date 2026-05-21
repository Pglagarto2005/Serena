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

h1 {
    color: white;
    text-align:center;
    font-size:60px !important;
}

p {
    color:white;
    text-align:center;
    font-size:22px;
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
    0 0 80px #ff5e8a;

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

.instruccion {

    text-align:center;
    color:#F6E6B4;
    font-size:34px;
    margin-top:40px;
    font-weight:bold;

    animation: fade 8s infinite;
}

@keyframes fade {

    0% {
        opacity:0;
    }

    25% {
        opacity:1;
    }

    50% {
        opacity:1;
    }

    100% {
        opacity:0;
    }
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
Inhala... Exhala...
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.button("Comenzar ejercicio")
