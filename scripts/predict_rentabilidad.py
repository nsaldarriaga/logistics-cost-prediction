# scripts/predict_rentabilidad_random_forest.py

import joblib # type: ignore
import pandas as pd # type: ignore

# 1. Cargar el modelo Random Forest entrenado
modelo_path = 'models/random_forest_classifier.pkl'
rf_model = joblib.load(modelo_path)

#  2. Crear un nuevo paquete a predecir
nuevo_paquete = pd.DataFrame({
    'delivery_days': [2],
    'package_value': [20.0],
    'package_weight_kg': [1.5],
    'delivery_cost': [3.0],
    'cost_per_kg': [3.0/1.5],
    'value_per_kg': [20.0/1.5],
    'is_heavy': [0],
    'is_high_value': [0],
    'provider_EnvíaLoYa': [0],
    'provider_FastCargo': [1],
    'provider_LogisticX': [0],
    'provider_PerúGo': [0],
    'provider_RapidBox': [0],
    'shipping_type_Express': [0],
    'shipping_type_Normal': [1],
    'customer_type_frecuente': [0],
    'customer_type_nuevo': [1],
    'customer_type_premium': [0]
})

#  3. Predecir si el paquete es rentable o no
prediccion = rf_model.predict(nuevo_paquete)

#  4. Interpretar la predicción
if prediccion[0] == 1:
    print(" El paquete sería RENTABLE según el modelo.")
else:
    print(" El paquete sería NO RENTABLE según el modelo.")