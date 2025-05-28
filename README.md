# Detección de Reportes Fraudulentos de Averías de Vehículos

## Descripción

Este proyecto utiliza técnicas de machine learning para identificar reportes fraudulentos de averías de vehículos, ayudando a la aseguradora "KLEY S.A." a reducir pérdidas por reclamaciones falsas o exageradas. El flujo abarca desde el análisis y tratamiento de datos hasta la implementación, optimización y evaluación de modelos de clasificación.

## Estructura del Proyecto

- **datos/**: Contiene los datasets en diferentes etapas de procesamiento:
  - `1. inicial/`: Datos originales
  - `2. tratados/`: Datos tratados (limpieza, imputación, etc.)
  - `3. convertidos/`: Variables categóricas convertidas a numéricas
  - `4. separados/`: Datasets separados para entrenamiento y prueba
  - `5. escalados/`: Datos escalados/normalizados
  - `6. predichos/`: Resultados de predicciones
- **models/**: Modelos entrenados (Random Forest, XGBoost, etc.)
- **best_model/**: Modelo con mejor desempeño según métricas de evaluación
- **optimized_model/**: Modelo optimizado mediante búsqueda de hiperparámetros
- **utils/model.py**: Funciones para guardar, cargar y gestionar modelos
- **constants/**: Rutas y variables constantes del proyecto
- **notebooks (.ipynb)**: Análisis exploratorio, procesamiento, entrenamiento, evaluación y explicación de modelos
- **requirements.txt**: Dependencias del proyecto

## Dataset

El dataset contiene información de vehículos y reportes de averías, incluyendo variables como:

- **marca**: Marca del vehículo
- **modelo**: Modelo del vehículo
- **color**: Color del vehículo
- **anio_registro**: Año de registro del vehículo
- **tipo_vehiculo**: Tipo del vehículo (SUV, Convertible, etc.)
- **millas_recorridas**: Millas recorridas por el vehículo
- **tamanio_motor**: Tamaño del motor
- **transmision**: Tipo de transmisión (Automática, Manual)
- **tipo_combustible**: Tipo de combustible (Gasolina, Diesel, etc.)
- **precio_vehiculo**: Precio del vehículo
- **num_asientos**: Número de asientos
- **num_puertas**: Número de puertas
- **problema_averia**: Tipo de daño reportado
- **id_problema_averia**: Identificador del daño reportado
- **fecha_averia**: Fecha en la que se reportó el daño
- **complejidad_reparacion**: Complejidad de la reparación
- **costo_reparacion**: Costo de la reparación
- **horas_reparacion**: Horas de reparación
- **fecha_reparacion**: Fecha en la que se reparó el daño
- **fraude**: Variable objetivo (1 si es fraude, 0 si no)

## Instalación

1. Clona el repositorio y entra a la carpeta del proyecto.
2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

El flujo principal del proyecto se encuentra en los notebooks numerados, que cubren:

1. **Revisión preliminar de los datos** (`0. Revision preliminar.ipynb`)
2. **Análisis univariado** (`1. Analisis univariado.ipynb`)
3. **Análisis multivariado** (`2. Analisis multivariado.ipynb`)
4. **Tratamiento de datos** (`3. Tratamiento de datos.ipynb`)
5. **Conversión de variables** (`4. Conversion de variables categoricas a numericas.ipynb`)
6. **Separación de datasets** (`5. Separacion de datasets.ipynb`)
7. **Escalado de los datasets** (`6. Escalado de los datasets.ipynb`)
8. **Implementación de modelos** (notebooks 7.x, 8.x, 9.x)
9. **Evaluación de modelos** (`10.1. Evaluacion de modelos.ipynb`)
10. **Optimización de modelos** (`10.2. Optimizando al mejor modelo.ipynb`)
11. **Predicciones y análisis final** (`11. Prediciones con el mejor modelo.ipynb`, `12. Prediciones con el mejor modelo copy.ipynb`)
12. **Explicabilidad con SHAP** (`13. Analisis SHAP.ipynb`)

Puedes ejecutar los notebooks en orden para reproducir el flujo completo del proyecto.

## Uso de scripts utilitarios

El archivo `utils/model.py` contiene funciones para:
- Guardar y cargar modelos (`save_model`, `load_model`)
- Gestionar el mejor modelo y el modelo optimizado (`save_best_model`, `open_best_model`, `save_optimized_model`, `open_optimized_model`)
- Notificar cuando termina la optimización (`notify_optimization_complete`)

### Ejemplo de uso de utilidades

```python
from utils.model import save_model, load_model

# Guardar un modelo entrenado
save_model(modelo_entrenado, "mi_modelo")

# Cargar un modelo
modelo = load_model("mi_modelo")
```

## Tecnologías y librerías principales

- Python 3.x
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- xgboost
- optuna (optimización de hiperparámetros)
- SHAP (explicabilidad)

## Créditos

Proyecto realizado para el Bootcamp de Machine Learning y Predicciones, ESPOL 2024-II.

---
