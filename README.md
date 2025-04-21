# Logistics Cost Prediction 🚚📦

Proyecto de Machine Learning para predicción de costos logísticos usando datasets sintéticos realistas.

--

## 📁 Estructura del proyecto
data/: contiene distintos dataset en formato CSV
models/: contiene los modelos entrenados.
notebooks/: notebooks de Google Colab con códigos de entrenamientos y EDA.
scripts/: contiene scripts de test de los modelos elegidos.
README.md: documentación principal del proyecto.

--

## 🧠 Variables del dataset

- package_id: ID único por paquete.
- customer_id: ID del cliente.
- customer_type: tipo de cliente (nuevo, frecuente, premium).
- delivery_date: fecha de entrega del paquete.
- delivery_days: días entre envío y entrega (distribución sesgada).
- package_value: valor del paquete en USD.
- package_weight_kg: peso del paquete en kilogramos.
- delivery_cost: costo del envío (distribución bimodal con picos en 2 y 4 USD).
- region: departamento real de Perú.
- zone: zona geográfica (Norte, Sur, Centro, Oriente, Sierra).
- provider: proveedor logístico ficticio.
- shipping_type: Normal o Express.
- is_peak_season: 1 si es noviembre o diciembre, 0 si no.
- is_profitable: target binario calculado con lógica de negocio.

--

## 📦 Modelos Entrenados
Debido a las limitaciones de tamaño de archivos en GitHub (máximo 100MB), el archivo .pkl del modelo entrenado no está incluido en este repositorio.

Sin embargo, puedes reentrenar el modelo y generar tu propio archivo .pkl ejecutando el notebook notebooks/models_training.ipynb, donde encontrarás todo el proceso de entrenamiento, visualización de métricas y generación del modelo listo para producción.

--

## 📊 Funcionalidades

- Predicción de rentabilidad de paquetes (`is_profitable`) mediante clasificación.
- Predicción del costo futuro de entrega (`delivery_cost`) mediante regresión.

--

## 🚀 Cómo usar

# Correr notebooks de entrenamiento

- python predict_cost.py
- python predict_cost_batch.py data/nuevos_paquetes.csv output/predicciones.csv

--

## ⚙️ Tecnologías usadas
- Python
- Scikit-Learn
- XGBoost
- LightGBM
- Matplotlib / Seaborn

--

## ⚠️ Nota
- El dataset utilizado es sintético, generado para fines educativos y de práctica de Machine Learning.
