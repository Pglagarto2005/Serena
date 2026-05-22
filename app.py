import streamlit as st
import paho.mqtt.client as mqtt
import time

st.set_page_config(
    page_title="Serena",
    page_icon="🌸",
    layout="centered"
)

# ===== MQTT CONFIG =====
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT   = 1883
MQTT_TOPIC  = "serena/calma"

def publicar_mqtt(mensaje):
    """Publica un mensaje MQTT al broker usando paho v2."""
    try:
        client_id = f"SerenaApp_{int(time.time())}"
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2,
            client_id=client_id
        )
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=10)
        client.loop_start()
        result = client.publish(MQTT_TOPIC, mensaje, qos=1)
        result.wait_for_publish()
        client.loop_stop()
        client.disconnect()
        return True
    except Exception as e:
        st.error(f"Error MQTT: {e}")
        return False

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
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ===== ESTADO =====
if "activo" not in st.session_state:
    st.session_state.activo = False

# ===== HERO SECTION =====
col1, col2 = st.columns([1, 1])

with col1:
    st.title("SERENA")
    st.subheader("No estás sola.")
    st.write("""
    Aplicación multimodal para el acompañamiento emocional
    en momentos de ansiedad.
    """)
    st.markdown("<br>", unsafe_allow_html=True)

    if not st.session_state.activo:
        if st.button("🌸 Comenzar"):
            with st.spinner("Conectando con el dispositivo..."):
                ok = publicar_mqtt("INICIAR")
            if ok:
                st.session_state.activo = True
                st.success("✅ Dispositivo activado")
                st.rerun()
    else:
        st.markdown("""
        <div style="
            background-color:#4a1166;
            padding:12px 20px;
            border-radius:12px;
            margin-bottom:10px;
            border: 1px solid #FF5E8A;
        ">
            <p style="margin:0;font-size:16px;">💜 Modo calma activado</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⏹ Detener"):
            with st.spinner("Deteniendo..."):
                ok = publicar_mqtt("DETENER")
            if ok:
                st.session_state.activo = False
                st.rerun()

with col2:
    st.markdown("""
    <div style="
        display:flex;
        align-items:center;
        justify-content:center;
        height:300px;
        font-size:120px;
    ">🌸</div>
    """, unsafe_allow_html=True)

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
        <h3 style="color:#F6E6B4;">Luz suave</h3>
        <p>LED cambia de color en tonos morados y rosados para acompañarte.</p>
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

# ===== DEBUG =====
with st.expander("🔧 Estado de conexión"):
    st.code(f"""
Broker : {MQTT_BROKER}:{MQTT_PORT}
Topic  : {MQTT_TOPIC}
Estado : {"🟢 Activo" if st.session_state.activo else "⚫ Inactivo"}
""")
