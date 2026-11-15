import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Dashboard Salud y Bienestar", layout="wide")

@st.cache_data
def cargar_datos():
    return pd.read_csv('healthy_diet_limpio.csv')

df = cargar_datos()

st.title("TU COACH VIRTUAL PARA MEJORAR TU SALUD Y BIENESTAR")
st.write("Generador de planes personalizados basado en análisis de datos reales.")

st.sidebar.header("Calcula tu plan ideal")

peso_usuario = st.sidebar.number_input("Ingresa tu peso (kg):", min_value=30.0, max_value=200.0, value=70.0)
altura_usuario = st.sidebar.slider("Ingresa tu altura (m):", min_value=1.00, max_value=2.30, value=1.70, step=0.01)
genero_usuario = st.sidebar.selectbox("Selecciona tu género:", ["Hombre", "Mujer"])

objetivo_usuario = st.sidebar.selectbox(
    "¿Cuál es tu objetivo en el gimnasio?", 
    ["Ganar Volumen (Masa Muscular)", "Definición (Quemar Grasa)", "Fuerza Pura", "Bajar de Peso general"]
)

imc_usuario = peso_usuario / (altura_usuario ** 2)

st.sidebar.markdown("---")
st.sidebar.subheader(f"Tu IMC: {imc_usuario:.2f}")

if imc_usuario < 18.5:
    categoria = "Bajo Peso"
    st.sidebar.warning(categoria)
elif 18.5 <= imc_usuario <= 24.9:
    categoria = "Normal"
    st.sidebar.success(categoria)
elif 25.0 <= imc_usuario <= 29.9:
    categoria = "Sobrepeso"
    st.sidebar.warning(categoria)
else:
    categoria = "Obesidad"
    st.sidebar.error(categoria)

tab1, tab2 = st.tabs(["MI PLAN PERSONALIZADO", "Estadísticas del Dataset"])

with tab1:
    st.header(f"Tu ruta para: {objetivo_usuario}")
    st.write(f"**Análisis de estado:** Según tu altura y peso, tu IMC indica **{categoria}**.")
    
    if objetivo_usuario == "Ganar Volumen (Masa Muscular)":
        dieta = "Mantén un **superávit calórico** (come entre 300 y 500 calorías más de las que quemas). Prioriza carbohidratos complejos (avena, arroz) para tener energía, y asegúrate de consumir suficiente proteína."
        rutina = "**Hipertrofia (4 a 5 días/semana)**. Enfócate en un rango de 8 a 12 repeticiones, llegando cerca del fallo muscular. Divide tu rutina (ej. Empuje, Tirón, Pierna)."
        tips = "Duerme al menos 8 horas para la recuperación muscular. Puedes apoyarte con un suplemento de Proteína Whey después de entrenar si te falta llegar a tus requerimientos diarios."
        
    elif objetivo_usuario == "Definición (Quemar Grasa)":
        dieta = "Aplica un **déficit calórico leve** (-300 kcal). Mantén tu consumo de proteína alto (aprox 2g por kilo de peso) para proteger tu masa muscular mientras pierdes la grasa."
        rutina = "**Fuerza Pesada + Cardio**. Sigue entrenando pesado en el gimnasio (no bajes los pesos). Añade 2 sesiones de cardio HIIT de 20 min o caminatas rápidas (LISS) post-entrenamiento."
        tips = "No intentes perder peso muy rápido o perderás músculo. Toma mucha agua y ten paciencia."
        
    elif objetivo_usuario == "Fuerza Pura":
        dieta = "**Calorías de Mantenimiento**. Come justo lo que quemas, asegurando una buena comida rica en carbohidratos unas horas antes de entrenar."
        rutina = "**Rutinas de Fuerza (Ej. 5x5 o 3x3)**. Trabaja a bajas repeticiones con cargas muy altas (85-95% de tu RM). Enfócate en ejercicios compuestos: Sentadilla, Peso Muerto y Press Banca."
        tips = "La técnica es innegociable. Descansa entre 3 y 5 minutos entre cada serie pesada para recuperar tu sistema nervioso."
        
    else: 
        dieta = "**Déficit Calórico Moderado/Alto** (-500 kcal). Prioriza alimentos con mucho volumen pero bajas calorías: ensaladas, verduras, caldos, y proteínas magras (pollo, pescado) para dar saciedad."
        rutina = "**Circuito Full Body y Cardio**. 3 días de entrenamiento de cuerpo completo para acelerar el metabolismo, combinados con natación, bicicleta o elíptica frecuente."
        tips = "Enfócate en tu NEAT (tu actividad fuera del gimnasio): intenta llegar a 10,000 pasos diarios. Evita los azúcares líquidos."

    if categoria in ["Sobrepeso", "Obesidad"] and objetivo_usuario == "Ganar Volumen (Masa Muscular)":
        st.error("**Alerta:** Debido a tu IMC actual, se recomienda enfocarse primero en 'Bajar de Peso' o 'Definición' para mejorar tu sensibilidad a la insulina antes de hacer un volumen.")
    elif categoria == "Bajo Peso" and objetivo_usuario in ["Bajar de Peso general", "Definición (Quemar Grasa)"]:
        st.error("**Alerta:** Tu IMC es bajo. Entrar en un déficit calórico podría afectar tu salud y sistema hormonal. Te recomendamos cambiar tu objetivo a 'Ganar Volumen'.")

    st.markdown("---")
    colA, colB, colC = st.columns(3)
    
    with colA:
        st.success("**NUTRICION IDEAL**")
        st.write(dieta)
        
    with colB:
        st.info("**RUTINA RECOMENDADA**")
        st.write(rutina)
        
    with colC:
        st.warning("**TIPS Y SUPLEMENTACIÓN**")
        st.write(tips)

with tab2:
    st.subheader(f"Análisis exploratorio en una población limpia de {len(df):,} usuarios")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**1. Distribución del IMC en el mundo real**")
        fig1, ax1 = plt.subplots(figsize=(5,3))
        ax1.hist(df['BMI'], bins=30, color='skyblue', edgecolor='black')
        ax1.set_xlabel("Índice de Masa Corporal (IMC)")
        ax1.set_ylabel("Frecuencia")
        st.pyplot(fig1)

    with col2:
        st.markdown("**2. Consumo Calórico vs Nivel de Actividad**")
        fig2, ax2 = plt.subplots(figsize=(5,3))
        df.groupby('Activity_Level')['Daily_Calorie_Consumed'].mean().plot(kind='bar', color='coral', ax=ax2)
        ax2.set_ylabel("Calorías Promedio")
        plt.xticks(rotation=45)
        st.pyplot(fig2)

    st.markdown("**3. Relación entre Peso y Consumo de Proteína**")
    fig3, ax3 = plt.subplots(figsize=(10, 3))
    ax3.scatter(df['Weight_kg'], df['Protein_Intake_g'], alpha=0.5, color='green')
    ax3.set_xlabel("Peso (kg)")
    ax3.set_ylabel("Proteína Consumida (g)")
    st.pyplot(fig3)