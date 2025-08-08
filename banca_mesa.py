import streamlit as st

st.set_page_config(page_title="Calculadora Banca Mesa", page_icon="🎲", layout="centered")

st.title("🎲 Calculadora Banca de Mesa")
st.write("Ingresa las cantidades de fichas, el Drop y la Banca Inicial para calcular la mesa.")

# Valores de las fichas (fijos)
denominaciones = {
    "1M": 1000000,
    "500K": 500000,
    "200K": 200000,
    "100K": 100000,
    "50K": 50000,
    "20K": 20000,
    "10K": 10000,
    "5K": 5000,
    "2K": 2000,
    "1K": 1000,
    "0.5K": 500
}

# Entrada de cantidades de fichas
st.subheader("Cantidad de Fichas")
cantidades = {}
for nombre, valor in denominaciones.items():
    cantidades[nombre] = st.number_input(
        f"{nombre} (${valor:,})", 
        min_value=0, 
        value=0, 
        step=1
    )

# Entradas de Drop y Banca Inicial
st.subheader("Datos de la Mesa")
banca_inicial = st.number_input("Banca Inicial ($)", min_value=0, value=0, step=1000, format="%d")
drop = st.number_input("Drop ($)", min_value=0, value=0, step=1000, format="%d")

# Calcular banca actual
banca_actual = sum(cantidades[nombre] * valor for nombre, valor in denominaciones.items())

# Calcular Win y Hold
win = banca_actual + drop - banca_inicial
hold = (win / drop * 100) if drop != 0 else 0

# Mostrar resultados
st.subheader("Resultados")
col1, col2, col3 = st.columns(3)
col1.metric("Banca Actual", f"${banca_actual:,.0f}")
col2.metric("WIN", f"${win:,.0f}")
col3.metric("HOLD", f"{hold:.2f}%")

# Mostrar tabla de detalle
st.subheader("Detalle de Cálculos")
st.table({
    "Denominación": list(denominaciones.keys()),
    "Valor": [f"${v:,.0f}" for v in denominaciones.values()],
    "Cantidad": [cantidades[n] for n in denominaciones.keys()],
    "Total": [f"${cantidades[n] * denominaciones[n]:,.0f}" for n in denominaciones.keys()]

})

