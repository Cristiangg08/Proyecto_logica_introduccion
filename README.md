# TU COACH VIRTUAL PARA MEJORAR TU SALUD Y BIENESTAR (Dashboard Interactivo)

Este proyecto es una aplicación web interactiva desarrollada en Python con Streamlit. Su objetivo es cruzar los datos biométricos de un usuario (peso y altura) con una base de datos real depurada para generar recomendaciones personalizadas de rutinas de ejercicio, nutrición y tips de salud basados en el Índice de Masa Corporal (IMC) y los objetivos físicos del usuario.

**Enlace a la aplicación desplegada:** [\[Abrir Dashboard en Streamlit\]([](https://proyectologicaintroduccion-bcyzexo8dzs3o8uyh5qfjh.streamlit.app/))]
## Contexto Académico
* **Proyecto Integrador de Primer Semestre**
* **Programa:** Ingeniería de Ciencia de Datos e Inteligencia Artificial
* **Universidad:** Universidad Santo Tomás (Sede Tunja)
* **Asignaturas Integradas:**
  * Introducción a la Ingeniería de Datos e Inteligencia Artificial
  * Lógica Computacional
* **Autores:**
  * Cristian Mauricio Flor Gómez
  * Jose Samuel Mora Benitez
  * Juan Esteban Castro Piza
  * Sara Gabriela Martinez Vianchá

## Sobre el Dataset
Se utilizó un dataset público extraído de Kaggle (`healthy_diet_calorie_intake.csv`), sometido a un proceso de limpieza y estructuración (`healthy_diet_limpio.csv`) enfocado en hábitos de dieta y consumo calórico.
* **Volumen:** ~6,000 registros depurados.
* **Variables principales seleccionadas:** Edad (`Age`), IMC (`BMI`), Nivel de Actividad (`Activity_Level`), Consumo Calórico Diario (`Daily_Calorie_Consumed`), Peso (`Weight_kg`) y Consumo de Proteína (`Protein_Intake_g`).
* El análisis exploratorio (EDA) y limpieza de estos datos se encuentra documentado en el cuaderno de Google Colab del proyecto.

## Funcionalidades de la Aplicación (Streamlit)
1. **Calculadora de IMC y Clasificación:** Evalúa el estado físico actual del usuario mediante estructuras de control lógicas (`if/elif/else`).
2. **Generador de Planes:** Arroja una ruta de dieta, rutina de gimnasio y tips basada en el objetivo seleccionado (Volumen, Definición, Fuerza, Bajar de Peso).
3. **Alertas Inteligentes (Validación cruzada):** Advierte al usuario si su objetivo físico choca con las recomendaciones médicas para su IMC actual.
4. **Exploración de Datos (EDA):** Visualizaciones interactivas usando Matplotlib sobre la distribución de IMC, consumo calórico por nivel de actividad y relación entre peso y consumo de proteína.

## Instrucciones de Uso (Ejecución Local)
Sigue estos pasos para correr la aplicación en tu propia máquina:

1.**Clona este repositorio o descarga los archivos en una carpeta:**
   
   git clone [https://github.com/Cristiangg08/Proyecto_logica_introduccion.git](https://github.com/Cristiangg08/Proyecto_logica_introduccion.git)
2. **En la terminal ejecuta el comando:** 
  streamlit run App.py