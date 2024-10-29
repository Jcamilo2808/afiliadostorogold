import streamlit as st
import base64

# Configuración de la página con el menú de navegación en la barra lateral
st.set_page_config(page_title="Torogold18k", layout="wide")

# Convertir el logo y la nueva imagen en la pantalla principal a base64
logo_path = "Diseño sin título.png"
main_image_path = "FreeSample-Vectorizer-io-Screenshot-2024-10-28-234219-removebg-preview.png"

with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

with open(main_image_path, "rb") as image_file:
    encoded_main_image = base64.b64encode(image_file.read()).decode()

# Configuración de estilo para aplicar color de fondo en la barra lateral y el diseño moderno del contenedor de la imagen principal
st.markdown(
    """
    <style>
    /* Cambiar el color de fondo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #5e100d;
        color: white;
    }
    
    .sidebar-logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .logo {
        width: 250px;  /* Tamaño aumentado del logo */
        border-radius: 0;  /* Sin borde redondeado */
    }
    
    /* Estilo del contenedor de la imagen principal */
    .main-image-container {
        background-color: #5e100d;
        padding: 20px;
        border-radius: 20px;  /* Bordes más redondeados */
        display: flex;
        justify-content: center;
        margin-top: 20px;
        box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.4);  /* Sombra más intensa */
        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transición suave */
    }

    .main-image-container:hover {
        transform: scale(1.02); /* Escala ligera al pasar el cursor */
        box-shadow: 0px 12px 32px rgba(0, 0, 0, 0.5); /* Sombra aún más intensa al pasar el cursor */
    }

    .main-image {
        width: 400px; /* Ajusta el tamaño de la imagen aquí */
    }
    
    /* Espacio extra sobre el formulario de login */
    .login-form {
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Mostrar solo el logo en la barra lateral, centrado y de tamaño ajustado
st.sidebar.markdown(
    f"""
    <div class="sidebar-logo">
        <img src="data:image/png;base64,{encoded_logo}" class="logo">
    </div>
    """, unsafe_allow_html=True
)

# Mostrar la nueva imagen principal en el contenedor estilizado
st.markdown(
    f"""
    <div class="main-image-container">
        <img src="data:image/png;base64,{encoded_main_image}" class="main-image">
    </div>
    """, unsafe_allow_html=True
)

# Formulario de login en la pantalla principal, con margen superior para separarlo de la imagen
st.markdown('<div class="login-form">', unsafe_allow_html=True)
with st.form("login_form"):
    username = st.text_input("USUARIO DEL AFILIADO")
    password = st.text_input("CONTRASEÑA DEL AFILIADO", type="password")
    submitted = st.form_submit_button("Ingresar")
    if submitted:
        st.success(f"Bienvenido, {username}!")
st.markdown('</div>', unsafe_allow_html=True)

