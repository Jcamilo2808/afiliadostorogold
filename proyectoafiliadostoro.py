import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO

st.set_page_config(page_title="COTIZADOR PRODUCTO ARTESANAL", page_icon="💎", layout="wide")

# === (Opcional) Logo ===
LOGO_PATH = r"C:/Users/juanc/Downloads/Diseño_sin_título-removebg-preview.png"

def encode_img_b64(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

encoded_logo = encode_img_b64(LOGO_PATH)

# ===== Estilos (fondo blanco, acentos vino/dorado, título moderno y más pequeño) =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;600&display=swap');
:root{ --vino:#5a0f1d; --vino-osc:#3f0b16; --dorado:#c7a75b; --dorado-osc:#a9914e;
       --negro:#111111; --radio:14px; --shadow:0 8px 24px rgba(0,0,0,.08); }
.stApp, main.stAppViewContainer{ background:#ffffff; color:var(--negro); }
.block-container{ padding-top: .6rem; }
h1,h2,h3,h4{ font-family:"Poppins","Inter",system-ui; color:var(--negro)!important; letter-spacing:.2px; }
/* Header */
.brand-wrap{ display:flex; align-items:center; gap:12px; padding:8px 12px; border-radius:12px;
  border:1px solid rgba(0,0,0,.06); background:#fff; box-shadow:var(--shadow); margin-top:10px;}
.brand-logo{ height:48px; width:auto; border-radius:10px; border:1px solid rgba(0,0,0,.06);}
.brand-name{ font-weight:800; letter-spacing:.8px; color: var(--vino); font-family:"Poppins",sans-serif; }
.page-title{ text-align:center; margin:10px 0 4px; font-size:28px; line-height:1.25; font-weight:700; }
/* Botones */
.stButton>button, .stDownloadButton>button{
  border-radius:12px; border:1px solid var(--dorado-osc);
  background:linear-gradient(180deg,var(--dorado),var(--dorado-osc));
  color:var(--negro); font-weight:700; padding:.6rem 1rem; box-shadow:var(--shadow);
}
.stButton>button:hover, .stDownloadButton>button:hover{ filter:brightness(1.05); transform:translateY(-1px); }
/* Inputs */
[data-baseweb="select"]>div, .stNumberInput input{
  border-radius:10px !important; border:1px solid rgba(0,0,0,.2) !important;
  background:#fff !important; color:var(--negro)!important;
}
/* Métricas y tabla */
[data-testid="stMetricValue"]{ color:var(--vino)!important; font-weight:800; }
[data-testid="stMetricLabel"]{ color:#444!important; }
.stDataFrame{ background:#fff; border:1px solid rgba(0,0,0,.08); border-radius:var(--radio); box-shadow:var(--shadow); overflow:hidden; }
/* Sidebar con tarjeta vinotinto para logo */
section[data-testid="stSidebar"]{ background:#fff; border-right:1px solid rgba(0,0,0,.06);}
.sidebar-head{ background:linear-gradient(90deg,var(--vino),var(--vino-osc)); color:#fff; padding:14px; border-radius:12px; margin:14px; box-shadow:var(--shadow);}
.sidebar-logo{ display:flex; align-items:center; gap:12px;}
.sidebar-logo img{ height:38px; width:auto; border-radius:8px;}
.sidebar-brand{ font-weight:800; letter-spacing:.3px;}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
col_a, col_b, col_c = st.columns([1,3,1])
with col_a:
    if encoded_logo:
        st.markdown(
            f'<div class="brand-wrap"><img class="brand-logo" src="data:image/png;base64,{encoded_logo}" />'
            f'<div class="brand-name">TORO GOLD</div></div>', unsafe_allow_html=True
        )
    else:
        st.markdown('<div class="brand-wrap"><div class="brand-name">TORO GOLD</div></div>', unsafe_allow_html=True)
with col_b:
    st.markdown("<h1 class='page-title'>COTIZADOR PRODUCTO ARTESANAL</h1>", unsafe_allow_html=True)
with col_c:
    st.markdown("&nbsp;")

# ===== PRECIOS embebidos (exacto a tu lista + nuevos ítems) =====
DEFAULT_COSTS = [
    # ORO LAMINADO 18K
    {"tipo": "Liso Dorado", "diametro_mm": 3, "precio_mayorista_unitario": 1600},
    {"tipo": "Italiano",    "diametro_mm": 3, "precio_mayorista_unitario": 1300},
    {"tipo": "Italy",       "diametro_mm": 3, "precio_mayorista_unitario": 1700},
    {"tipo": "Rosado",      "diametro_mm": 3, "precio_mayorista_unitario": 1700},

    {"tipo": "Liso Dorado", "diametro_mm": 4, "precio_mayorista_unitario": 2800},
    {"tipo": "Italiano",    "diametro_mm": 4, "precio_mayorista_unitario": 2600},
    {"tipo": "Italy",       "diametro_mm": 4, "precio_mayorista_unitario": 3100},
    {"tipo": "Roma",        "diametro_mm": 4, "precio_mayorista_unitario": 3000},
    {"tipo": "Liso Rosado", "diametro_mm": 4, "precio_mayorista_unitario": 3100},

    {"tipo": "Liso Dorado", "diametro_mm": 5, "precio_mayorista_unitario": 4050},
    {"tipo": "Italiano",    "diametro_mm": 5, "precio_mayorista_unitario": 4050},
    {"tipo": "Italy",       "diametro_mm": 5, "precio_mayorista_unitario": 4050},
    {"tipo": "Roma",        "diametro_mm": 5, "precio_mayorista_unitario": 4050},

    {"tipo": "Liso Dorado", "diametro_mm": 6, "precio_mayorista_unitario": 6750},
    {"tipo": "Italiano",    "diametro_mm": 6, "precio_mayorista_unitario": 6900},
    {"tipo": "Italy",       "diametro_mm": 6, "precio_mayorista_unitario": 6950},
    {"tipo": "Rosado",      "diametro_mm": 6, "precio_mayorista_unitario": 6900},

    {"tipo": "Italiano",    "diametro_mm": 8, "precio_mayorista_unitario": 10000},

    # PLATERÍA LEY 925
    {"tipo": "Diamantado",  "diametro_mm": 3, "precio_mayorista_unitario": 1600},
    {"tipo": "Diamantado",  "diametro_mm": 4, "precio_mayorista_unitario": 2000},
    {"tipo": "Diamantado",  "diametro_mm": 5, "precio_mayorista_unitario": 3800},

    # ===== Nuevos ítems (según solicitud) =====
    {"tipo": "balin combinacion shakras", "diametro_mm": 6, "precio_mayorista_unitario": 5000},
    {"tipo": "piedra agata",              "diametro_mm": 6, "precio_mayorista_unitario":  600},
    {"tipo": "neopreno",                  "diametro_mm": 6, "precio_mayorista_unitario":  400},
    {"tipo": "neopreno",                  "diametro_mm": 8, "precio_mayorista_unitario":  500},
]

# ------- DataFrame y mapa de DISPONIBILIDAD EXACTA por tipo -------
PRECIOS = pd.DataFrame(DEFAULT_COSTS)
PRECIOS["tipo"] = PRECIOS["tipo"].astype(str)
PRECIOS["diametro_mm"] = pd.to_numeric(PRECIOS["diametro_mm"], errors="coerce").astype("Int64")
PRECIOS["precio_mayorista_unitario"] = pd.to_numeric(PRECIOS["precio_mayorista_unitario"], errors="coerce")

# Mapa explícito de disponibilidad (lo que verá el usuario en el combo de diámetros)
AVAIL = {
    "Liso Dorado": [3,4,5,6],
    "Italiano":    [3,4,5,6,8],
    "Italy":       [3,4,5,6],
    "Roma":        [4,5],
    "Rosado":      [3,6],
    "Liso Rosado": [4],
    "Diamantado":  [3,4,5],
    # Nuevos:
    "balin combinacion shakras": [6],
    "piedra agata":              [6],
    "neopreno":                  [6,8],
}

# ===== Sidebar parámetros (con logo como antes) =====
with st.sidebar:
    st.markdown(
        '<div class="sidebar-head"><div class="sidebar-logo">'
        + (f'<img src="data:image/png;base64,{encoded_logo}"/>' if encoded_logo else '<div style="height:36px;width:36px;border-radius:8px;background:#fff;color:#000;display:flex;align-items:center;justify-content:center;font-weight:900;">TG</div>')
        + '<div class="sidebar-brand">TORO GOLD</div></div></div>', unsafe_allow_html=True
    )
    canal = st.radio("Canal", ["Mayorista", "Cliente final (x2)"], index=0)
    mano_obra = st.number_input("Mano de obra (COP)", min_value=0.0, value=8000.0, step=500.0)

FACTOR_CLIENTE_FINAL = 2.0

# ===== Ítems dinámicos =====
if "n_items" not in st.session_state:
    st.session_state.n_items = 1

bar = st.container()
with bar:
    c_add, c_rem, c_reset = st.columns([1,1,1])
    if c_add.button("➕ Agregar ítem"): st.session_state.n_items += 1
    if c_rem.button("🗑️ Quitar último", disabled=(st.session_state.n_items<=1)):
        if st.session_state.n_items>1: st.session_state.n_items -= 1
    if c_reset.button("🧹 Nueva cotización"):
        for k in list(st.session_state.keys()):
            if k.startswith(("tipo_","diam_","unidad_","cant_")): del st.session_state[k]
        st.session_state.n_items = 1

st.subheader("Ítems del diseño")
tipos_disponibles = list(AVAIL.keys())  # exactamente los tipos de la lista + nuevos

with st.form("form_items"):
    items = []
    for i in range(st.session_state.n_items):
        st.markdown(f"**Ítem #{i+1}**")
        c1, c2, c3, c4 = st.columns([1.7, 1.2, 1, 1.2])

        tipo = c1.selectbox("Tipo", tipos_disponibles, key=f"tipo_{i}")

        # Diámetros REALES por tipo desde AVAIL (conserva selección previa si sigue válida)
        diams = AVAIL.get(tipo, [])
        prev = st.session_state.get(f"diam_{i}")
        idx = diams.index(prev) if (isinstance(prev, int) and prev in diams) else 0
        diam = c2.selectbox("Diámetro (mm)", diams, index=idx, key=f"diam_{i}")

        unidad = c3.selectbox("Unidad", ["balines", "otros"], key=f"unidad_{i}")
        cantidad = c4.number_input("Cantidad", min_value=1, max_value=2000, value=1, step=1, key=f"cant_{i}")

        # Precio mayorista exacto (tipo, diámetro) desde la tabla
        fila = PRECIOS[(PRECIOS["tipo"]==tipo) & (PRECIOS["diametro_mm"]==diam)]
        if fila.empty:
            st.error(f"No hay precio para {tipo} {diam} mm en la lista. Revisa DEFAULT_COSTS.")
            st.stop()
        pm = float(fila["precio_mayorista_unitario"].iloc[0])

        items.append({
            "tipo": tipo,
            "diametro_mm": int(diam),
            "unidad": unidad,
            "cantidad": int(cantidad),
            "precio_mayorista_unitario": pm
        })
        st.divider()

    submitted = st.form_submit_button("Calcular cotización")

# ===== Cálculo + Resultados =====
if submitted:
    df = pd.DataFrame(items)

    df["precio_unitario_canal"] = np.where(
        canal.startswith("Mayorista"),
        df["precio_mayorista_unitario"],
        df["precio_mayorista_unitario"] * FACTOR_CLIENTE_FINAL
    )
    df["importe"] = df["cantidad"] * df["precio_unitario_canal"]

    subtotal_materiales = float(df["importe"].sum())
    precio_final = subtotal_materiales + float(mano_obra)

    m1, m2 = st.columns(2)
    m1.metric("Subtotal materiales (COP)", f"{subtotal_materiales:,.0f}")
    m2.metric("Precio final (incluye mano de obra)", f"{precio_final:,.0f}")

    st.subheader("Detalle de la cotización")
    mostrar = df.copy()
    mostrar["precio_mayorista_unitario"] = mostrar["precio_mayorista_unitario"].round(0)
    mostrar["precio_unitario_canal"] = mostrar["precio_unitario_canal"].round(0)
    mostrar["importe"] = mostrar["importe"].round(0)
    st.dataframe(
        mostrar[["tipo","diametro_mm","unidad","cantidad",
                 "precio_mayorista_unitario","precio_unitario_canal","importe"]],
        use_container_width=True
    )

    def to_excel(df_det, resumen):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_det.to_excel(writer, index=False, sheet_name="Detalle")
            pd.DataFrame([resumen]).to_excel(writer, index=False, sheet_name="Resumen")
        return output.getvalue()

    excel_bytes = to_excel(
        mostrar,
        {
            "canal": canal,
            "factor_cliente_final": 2.0 if canal.startswith("Cliente") else 1.0,
            "subtotal_materiales": round(subtotal_materiales, 0),
            "mano_obra": round(float(mano_obra), 0),
            "precio_final": round(precio_final, 0),
        },
    )
    filename = "cotizacion_cliente_final.xlsx" if canal.startswith("Cliente") else "cotizacion_mayorista.xlsx"
    st.download_button("⬇️ Descargar cotización en Excel", data=excel_bytes, file_name=filename, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


