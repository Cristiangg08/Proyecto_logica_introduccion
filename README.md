#TU COACH VIRTUAL PARA MEJORAR TU SALUD Y BIENESTAR(Dashboard Interactivo)

Este proyecto es una aplicación web interactiva desarrollada en Python con Streamlit. Su objetivo es cruzar los datos biométricos de un usuario (peso, altura, género) con una base de datos real de 6,000 registros para generar recomendaciones personalizadas de rutinas de ejercicio, nutrición y tips de salud basados en el Índice de Masa Corporal (IMC) y los objetivos físicos del usuario.

##Contexto Académico
Proyecto Integrador de Primer Semestre
**Programa:** Ingeniería de Ciencia de Datos e Inteligencia Artificial
**Universidad:** Universidad Santo Tomás (Sede Tunja)
**Asignaturas Integradas:**
- Introducción a la Ingeniería de Datos e Inteligencia Artificial
- Lógica Computacional

**Autores:**
- Cristian Mauricio Flor Gómez
- Jose Samuel Mora Benitez
- Juan Esteban Castro Piza
- Sara Gabriela Martinez Viancha 

##Sobre el Dataset
Se utilizó un dataset público extraído de Kaggle enfocado en hábitos de dieta y consumo calórico. 
- **Volumen:** 6,000 registros.
- **Variables principales:** Edad, Género, Peso (kg), Altura (cm), IMC, Nivel de Actividad, Consumo Calórico y de Macronutrientes.
- El análisis exploratorio (EDA) de estos datos se encuentra documentado en el archivo de Google Colab adjunto al repositorio.

##Funcionalidades de la Aplicación (Streamlit)
1. **Calculadora de IMC y Clasificación:** Evalúa el estado físico actual del usuario mediante estructuras de control lógicas.
2. **Generador de Planes:** Arroja una ruta de dieta, rutina de gimnasio y tips basada en el objetivo seleccionado (Volumen, Definición, Fuerza, Bajar de Peso).
3. **Alertas Inteligentes (Validación cruzada):** Advierte al usuario si su objetivo físico choca con las recomendaciones médicas para su IMC actual.
4. **Exploración de Datos (EDA):** Visualizaciones interactivas usando Matplotlib sobre la distribución de IMC y calorías de la población del dataset original.

##Instrucciones de Uso (Ejecución Local)

Sigue estos pasos para correr la aplicación en tu propia máquina:

1. **Clona este repositorio** o descarga los archivos en una carpeta.
2. **Abre la terminal** en esa carpeta.
3. **Instala las dependencias necesarias** ejecutando el siguiente comando:
  pip install streamlit/pandas/matplotlib/numpy

4.**En la terminal ejecuta el comando 
  streamlit run app.py