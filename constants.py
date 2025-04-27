initial_dir = "./datos/1. inicial"
tratados_dir = "./datos/2. tratados"
converted_dir = "./datos/3. convertidos"
separated_dir = "./datos/4. separados"
scaled_dir = "./datos/5. escalados"
predicted_dir = "./datos/6. predichos"
models_dir = "./models"

# Predictor variables
predictor_vars = [
    "anio_registro",
    "millas_recorridas",
    "precio_vehiculo",
    "num_asientos",
    "num_puertas",
    "complejidad_reparacion",
    "costo_reparacion",
    "horas_reparacion",
    "marca_te",
    "transmision_encoded",
    "fuel_petrol",
    "fuel_diesel",
    "fuel_electric",
    "fuel_hybrid",
    "fuel_plugin",
    "fuel_other",
    "color_r",
    "color_g",
    "color_b",
    "tipo_vehiculo_te",
]
target_var = "fraude"
