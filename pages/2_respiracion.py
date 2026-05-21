import streamlit as st

st.set_page_config(
    page_title="Respira | Serena",
    page_icon="Logo.png",
    layout="wide"
)

# ===== ESTADO =====

if "ejercicio" not in st.session_state:
    st.session_state.ejercicio = False

# ===== ESTILOS =====

st.markdown("""
<style>

.stApp {
    background-color: #2B0A57;
    color: white;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #220046;
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
    font-size: 72px !important;
    margin-top: 60px;
}

p {
    color:white;
    font-size:24px;
}

/* BOTÓN */

div.stButton > button {

    background-color:#FF5E8A;
    color:white;

    border:none;
    border-radius:25px;

    padding:18px 40px;

    font-size:22px;
    font-weight:bold;

    transition:0.3s;

    box-shadow: 0 0 20px rgba(255, 94, 138, 0.4);
}

div.stButton > button:hover {

    background-color:#ff7ca2;

    transform:scale(1.05);
}

/* CÍRCULO */

.circle-container {

    display:flex;
    justify-content:center;
    align-items:center;

    width:100%;
    height:80vh;
}

.circle {

    width: 260px;
    height: 260px;

    border-radius: 50%;

    background: radial-gradient(circle, #ff7ca2, #ff5e8a);

    box-shadow:
    0 0 30px rgba(255, 94, 138, 0.5),
    0 0 60px rgba(255, 94, 138, 0.3);

    animation: breathe 8s infinite ease-in-out;

    display:flex;
    justify-content:center;
    align-items:center;

    color:#F6E6B4;
    font-size:38px;
    font-weight:bold;
}

/* ANIMACIÓN */

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

.circle::after {

    content: "INHALA";

    animation: breathingText 8s infinite;
}

@keyframes breathingText {

    0% {
        content: "INHALA";
    }

    49% {
        content: "INHALA";
    }

    50% {
        content: "EXHALA";
    }

    100% {
        content: "EXHALA";
    }
}

</style>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====

col1, col2 = st.columns([1,1])

# ===== TEXTO =====

with col1:

    st.title("Respira conmigo")

    st.write("No necesitas resolver todo ahora.")

    st.markdown("<br><br>", unsafe_allow_html=True)

    if not st.session_state.ejercicio:

        if st.button("Comenzar ejercicio"):
            st.session_state.ejercicio = True
            st.rerun()

    else:

        if st.button("Pausar ejercicio"):
            st.session_state.ejercicio = False
            st.rerun()

        st.success("Sigue el ritmo de tu respiración.")

# ===== CÍRCULO =====

with col2:

    if st.session_state.ejercicio:

        audio_file = open("relax.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.markdown("""
        <div class="circle-container">
            <div class="circle"></div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="circle-container">
            <div class="circle" style="animation:none; opacity:0.5;">
                <span style="font-size:28px;">PAUSADO</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
