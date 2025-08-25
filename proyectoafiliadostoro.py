import streamlit as st
import base64

# Configuración de la página con el menú de navegación en la barra lateral
st.set_page_config(page_title="Torogold18k", layout="wide")

# Credenciales del usuario
VALID_USERNAME = "1088331728"
VALID_PASSWORD = "1088331728"

# Actualiza la ruta de la imagen
logo_path = "C:/Users/juanc/Downloads/Diseño_sin_título-removebg-preview.png"
main_image_path = "C:/Users/juanc/Downloads/FreeSample-Vectorizer-io-Screenshot-2024-10-28-234219-removebg-preview.png"

with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

with open(main_image_path, "rb") as image_file:
    encoded_main_image = base64.b64encode(image_file.read()).decode()

# Configuración de estilo para la barra lateral, contenedor de imagen y formulario de login
st.markdown(
    """
    <style>
    /* Cambiar el color de fondo en la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #000000; /* Cambiado a negro */
        color: white;
    }
    
    .sidebar-logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .logo {
        width: 250px;
        border-radius: 0;
    }
    
    /* Estilo del contenedor de la imagen principal */
    .main-image-container {
        background-color: #000000; /* Cambiado a negro */
        padding: 20px;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        margin: 20px auto;
        width: 50%;
        box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .main-image-container:hover {
        transform: scale(1.02);
        box-shadow: 0px 12px 32px rgba(0, 0, 0, 0.5);
    }

    .main-image {
        width: 70%;
    }
    
    /* Estilo del formulario de login */
    .login-form {
        margin-top: 50px;
        width: 30%;
        margin-left: auto;
        margin-right: auto;
    }

    /* Estilo para los campos de entrada */
    .login-form input {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }

    /* Estilo para los botones del menú ajustados al ancho completo */
    .menu-button {
        display: block;
        width: 100%; /* Ancho completo */
        padding: 10px 20px; /* Espacio alrededor del texto y separación izquierda */
        border-radius: 10px;
        background-color: #000000;
        color: white;
        text-align: left; /* Justificado a la izquierda */
        margin: 10px 0; /* Espacio entre botones */
        font-size: 16px;
        transition: background-color 0.3s;
        border: 1px solid white; /* Borde blanco delgado */
        box-sizing: border-box; /* Incluye el borde en el ancho total */
    }
    .menu-button:hover {
        background-color: #333333; /* Color de fondo al pasar el cursor */
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

# Variable de estado para el inicio de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Si el usuario está autenticado, mostrar el módulo de navegación
if st.session_state.authenticated:
    st.sidebar.markdown("<div class='menu-button'>Trazabilidad de dinero</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div class='menu-button'>Inventarios</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div class='menu-button'>Facturas de venta</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div class='menu-button'>Órdenes de compra</div>", unsafe_allow_html=True)
else:
    # Mostrar la pantalla de login si no está autenticado
    st.markdown(
        f"""
        <div class="main-image-container">
            <img src="data:image/png;base64,{encoded_main_image}" class="main-image">
        </div>
        """, unsafe_allow_html=True
    )

    # Formulario de login
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    with st.form("login_form"):
        username = st.text_input("USUARIO DEL AFILIADO")
        password = st.text_input("CONTRASEÑA DEL AFILIADO", type="password")
        submitted = st.form_submit_button("Ingresar")
        
        # Validación de usuario y contraseña
        if submitted:
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                st.success(f"Bienvenido, {username}!")
                st.session_state.authenticated = True
            else:
                st.error("Usuario o contraseña incorrectos.")
    st.markdown('</div>', unsafe_allow_html=True)




