# logistics-cost-prediction
Proyecto de generación y modelado a partir de un dataset sintético de costos logísticos en Perú


# 📦 Synthetic Logistics Dataset & Cost Prediction (Machine Learning)

Este proyecto contiene un dataset sintético diseñado para modelar y predecir costos logísticos en el contexto de última milla en Perú. Se ha creado pensando en el análisis exploratorio, la ingeniería de características y la experimentación con modelos de regresión o clasificación.

---

## 📁 Estructura del proyecto

- `data/`: contiene el dataset en formato CSV.
- `notebooks/`: notebook de Google Colab con el código de generación del dataset.
- `README.md`: documentación principal del proyecto.

---

## 🧠 Variables del dataset

- `package_id`: ID único por paquete.
- `customer_id`: ID del cliente.
- `customer_type`: tipo de cliente (`nuevo`, `frecuente`, `premium`).
- `delivery_date`: fecha de entrega del paquete.
- `delivery_days`: días entre envío y entrega (distribución sesgada).
- `package_value`: valor del paquete en USD.
- `package_weight_kg`: peso del paquete en kilogramos.
- `delivery_cost`: costo del envío (distribución bimodal con picos en 2 y 4 USD).
- `region`: departamento real de Perú.
- `zone`: zona geográfica (Norte, Sur, Centro, Oriente, Sierra).
- `provider`: proveedor logístico ficticio.
- `shipping_type`: `Normal` o `Express`.
- `is_peak_season`: 1 si es noviembre o diciembre, 0 si no.
- `is_profitable`: target binario calculado con lógica de negocio.

---

## 🚀 Próximos pasos

- Realizar análisis exploratorio (EDA)
- Ingeniería de features
- Entrenamiento de modelos de ML:
  - Clasificación (`is_profitable`)
  - Regresión (`delivery_cost`)
- Evaluación de métricas y visualización de resultados

---

## ✍️ Autor

Este proyecto fue creado como parte de un portafolio personal de ciencia de datos.
