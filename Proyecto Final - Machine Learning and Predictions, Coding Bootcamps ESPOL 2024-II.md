  
Detección de Reportes Fraudulentos de   
Averías de Vehículos

**Descripción del Proyecto**

**Introducción**

La empresa de seguros de vehículos “KLEY S.A.” lo ha contratado a usted y a **su equipo de analitica conformado por 3 científicos de datos (incluyéndolo a usted)** para desarrollar un modelo de machine learning capaz de identificar reportes fraudulentos de averías de vehículos. Las aseguradoras reciben numerosos reportes de averías y reparaciones de vehículos diariamente. Aunque la mayoría de los reportes son legítimos, un pequeño porcentaje de ellos son fraudulentos, donde los clientes exageran los daños o presentan reclamaciones falsas para obtener mayores pagos. Detectar estas transacciones fraudulentas es crucial para la sostenibilidad financiera de las aseguradoras. La empresa “KLEY S.A.” enfrenta pérdidas significativas debido a estos reportes fraudulentos y la misión de su equipo de científicos de datos será construir una solución que ayude a mitigar estos costos utilizando Inteligencia Artificial. El rol de su equipo incluirá desde el análisis y tratamiento de los datos hasta la implementación y evaluación de modelos de ML, pasando por la comunicación de sus resultados. Para ello, la empresa le ha proporcionado un conjunto de datos en donde han detectado manualmente los reportes fraudulentos.

**Descripción del Dataset**

La empresa le ha proporcionado un conjunto de datos con las siguientes columnas:

* **marca**: Marca del vehículo  
* **modelo**: Modelo del vehículo  
* **color**: Color del vehículo  
* **anio\_registro**: Año de registro del vehículo  
* **tipo\_vehiculo**: Tipo del vehículo. Ej. SUV, Convertible  
* **millas\_recorridas**: Millas recorridas por el vehículo  
* **tamanio\_motor**: Tamaño del motor del vehículo  
* **transmision**: Tipo de transmisión del vehículo (Automática, Manual)  
* **tipo\_combustible**: Tipo de combustible del vehículo. Ej. Gasolina, Diesel  
* **precio\_vehiculo**: Precio del vehículo  
* **num\_asientos**: Número de asientos del vehículo  
* **num\_puertas**: Número de puertas del vehículo  
* **problema\_averia**: Tipo de daño reportado  
* **id\_problema\_averia**: Identificador del daño reportado  
* **fecha\_averia**: Fecha en la que se reportó el daño  
* **complejidad\_reparacion**: Complejidad de la reparación  
* **costo\_reparacion**: Costo de la reparación  
* **horas\_reparacion**: Horas de reparación  
* **fecha\_reparacion**: Fecha en la que se reparó el daño  
* **fraude**: Variable objetivo que indica si la reparación fue un fraude o no

**Modelo Baseline**

Su equipo cuenta con un modelo baseline basado en Random Forest y un procesamiento de datos simple, elaborado por la aseguradora de vehículos. Idealmente usted y su equipo deberán proveer un modelo que funcione mejor para detectar reportes fraudulentos. El modelo baseline se encuentra en [este enlace](https://drive.google.com/file/d/13Csb-4vOoQp8ECstK1ZywkrQtAzvuUeV/view?usp=sharing).

**Evaluación del Modelo**  
La métrica principal que utilizará para evaluar sus modelos resultantes será el balanced accuracy ([https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced\_accuracy\_score.html](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html) ). Todos los equipos trabajando en el modelo solicitado contarán con un conjunto de datos de test, del cual no poseerán la variable target. Cada equipo contará con un repositorio en donde podrá colocar sus predicciones sobre el conjunto de test proporcionado. Todos los martes y viernes previo a las clases se actualizará la [tabla de posiciones](https://docs.google.com/spreadsheets/d/1ulcZv19fZ_0FMB_7yG6xy63zRAYu29n7/edit?usp=sharing&ouid=117258840351252297072&rtpof=true&sd=true) en donde podrá comparar el mejor rendimiento alcanzado por su equipo con los rendimientos obtenidos por otros equipos sobre el conjunto de test, como se muestra en la figura siguiente.

![][image1]

Adicionalmente, su equipo es libre de determinar otras métricas de evaluación que muestren el rendimiento de sus modelos, especialmente a mostrar en la presentación final del proyecto.

**Evaluación del Proyecto**  
El proyecto consistirá de dos entregables que serán parte de la nota final del proyecto, así como de una presentación final a través de un video. La distribución de los puntos se realizará de la siguiente manera:

* Entregable  1 — 30%  
* Entregable 2 — 50%  
* Presentación (video) — 20%

Puntos extras: Los dos equipos con el mejor rendimiento **sobre los datos de test** tendrán puntos adicionales en la calificación final del proyecto.

Las descripciones de los entregables se publicarán semanalmente en este documento, que será regularmente actualizado con nueva información.

**Entregable 1 (plazo de entrega 25/04/2024)**

Suba a Aula Virtual un (1) Jupyter notebook con las siguientes tareas:

* Revisión preliminar de los datos. Identifique el número de características, sus tipos de datos.  
* Análisis Univariado:  
  * Seleccione al menos tres variables y realice un análisis univariable en cada una.  
  * Proporcione visualizaciones (por ejemplo, histogramas, diagramas de caja) para cada variable seleccionada e interprételas.  
* Análisis Multivariado:  
  * Elija al menos dos pares de variables (no considere la variable target) y realice un análisis multivariable para cada par.  
  * Elija al menos dos variables de variables y realice un análisis multivariable entre las variables elegidas y la variable target.  
  * Utilice visualizaciones adecuadas (por ejemplo, diagramas de dispersión, gráficos de barras).  
  * Explique cualquier relación observada entre los pares de variables analizados.  
* Implemente al menos 3 modelos de clasificación e intente superar al baseline compartido. Para los 3 modelos utilice el mismo algoritmo de clasificación (elija uno aprendido en clases) con diferentes configuraciones. Distintas configuraciones pueden incluir distintos valores de hiperparámetros o técnicas de procesamiento de los datos de entrada. Para las distintas configuraciones puede considerar lo siguiente:  
  * Sus datos podrían ser estandarizados/normalizados o no.  
  * Puede definir alguna estrategia para codificar variables categóricas (puede utilizar One-hot-encoding, Target encoding, u otra estrategia).  
  * Identifique valores faltantes y defina una estrategia (de ser necesario) para la imputación de datos.  
  * Analice las variables categóricas y determine si es necesario tratar categorías poco frecuentes (por ejemplo, a veces agrupar categorías raras puede ser útil). Explique sus decisiones en el tratamiento de los datos.  
  * Detecte valores atípicos y defina una estrategia para tratarlos. Considere que eliminar los registros outliers (del set de entrenamiento) no es la única estrategia posible (puede considerar la regla del rango intercuartil, Local Outlier Factor, u otra estrategia). Explique sus decisiones en el tratamiento de los datos.  
* Evalúe y compare todos los modelos. Interprete los resultados y concluya cuál modelo es el mejor. Puede considerar más de una métrica de evaluación para su conclusión.

Suba sus predicciones sobre los datos de test a la carpeta de Google Drive asignada a su equipo.

[image1]: <data:image/png;base64,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>