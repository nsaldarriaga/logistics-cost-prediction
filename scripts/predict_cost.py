# predict_cost.py

import pandas as pd
import pickle

# 1. Cargar el modelo entrenado
with open('models/random_forest_regressor_cost.pkl', 'rb') as file:
    modelo = pickle.load(file)

# 2. Definir la plantilla de columnas
columnas_esperadas = [
    'package_weight_kg', 'package_value', 'delivery_days', 'distance_km',
    'is_peak_season', 'is_profitable', 'shipping_type_Express',
    'shipping_type_Normal', 'provider_EnvíaloYa', 'provider_FastCargo',
    'provider_LogisticX', 'provider_PerúGo', 'provider_RapidBox',
    'region_Amazonas', 'region_Ancash', 'region_Apurímac', 'region_Arequipa',
    'region_Ayacucho', 'region_Cajamarca', 'region_Callao', 'region_Cusco',
    'region_Huancavelica', 'region_Huánuco', 'region_Ica', 'region_Junín',
    'region_La Libertad', 'region_Lambayeque', 'region_Lima', 'region_Loreto',
    'region_Madre de Dios', 'region_Moquegua', 'region_Pasco', 'region_Piura',
    'region_Puno', 'region_San Martín', 'region_Tacna', 'region_Tumbes',
    'region_Ucayali', 'zone_Centro', 'zone_Norte', 'zone_Oriente',
    'zone_Sierra', 'zone_Sur', 'customer_type_frecuente', 'customer_type_nuevo',
    'customer_type_premium'
]

# 3. Crear un nuevo paquete (ejemplo de predicción)
nuevo_paquete = pd.DataFrame([{col: 0 for col in columnas_esperadas}])

# Ahora completamos manualmente los campos que correspondan:
nuevo_paquete['package_weight_kg'] = 3.2
nuevo_paquete['package_value'] = 55
nuevo_paquete['delivery_days'] = 2
nuevo_paquete['distance_km'] = 120
nuevo_paquete['is_peak_season'] = 0
nuevo_paquete['is_profitable'] = 1
nuevo_paquete['shipping_type_Normal'] = 1
nuevo_paquete['region_Lima'] = 1
nuevo_paquete['zone_Centro'] = 1
nuevo_paquete['customer_type_nuevo'] = 1

# 4. Realizar la predicción
costo_predicho = modelo.predict(nuevo_paquete)[0]

print(f'Costo de entrega predicho: ${costo_predicho:.2f}')