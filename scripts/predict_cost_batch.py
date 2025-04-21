# predict_cost_batch.py

import pandas as pd
import pickle
import sys

# 1. Cargar el modelo entrenado
with open('models/random_forest_regressor_cost.pkl', 'rb') as file:
    modelo = pickle.load(file)

# 2. Definir las columnas esperadas (orden correcto)
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

# 3. Función principal para predecir en lote
def predecir_costos(input_csv, output_csv):
    # Leer nuevos paquetes
    df_nuevos = pd.read_csv(input_csv)

    # Asegurar que tengan todas las columnas necesarias
    for col in columnas_esperadas:
        if col not in df_nuevos.columns:
            df_nuevos[col] = 0  # Completar las faltantes con 0

    # Reordenar columnas
    df_nuevos = df_nuevos[columnas_esperadas]

    # Realizar predicción
    df_nuevos['predicted_delivery_cost'] = modelo.predict(df_nuevos)

    # Guardar resultados
    df_nuevos.to_csv(output_csv, index=False)
    print(f'✅ Predicciones guardadas en {output_csv}')

# 4. Si se ejecuta desde terminal
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python predict_cost_batch.py <input_csv> <output_csv>")
    else:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        predecir_costos(input_csv, output_csv)