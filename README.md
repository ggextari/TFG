# 📊 Predicción de Recobro de Facturas Vencidas — TFG

Este repositorio contiene el código y experimentos del Trabajo de Fin de Grado centrado en la **predicción de recobro de impagos mediante modelos de machine learning**, evaluando su implementación en **SAS Enterprise Miner** y **Databricks con Python**.

El objetivo principal fue replicar y comparar el rendimiento de distintos algoritmos en ambos entornos, valorando su precisión, interpretabilidad y viabilidad operativa.

---

## 🔍 Comparativa de Modelos: Tabla 4.1

| Modelo                        | Entorno       | Índice ROC | Comentario                                                                 |
|------------------------------|---------------|------------|----------------------------------------------------------------------------|
| Árbol de Decisión            | SAS Miner     | 0,712      | Rápido, pero con síntomas de sobreajuste                                  |
| **Random Forest**            | SAS Miner     | **0,807**  | Robusto, aunque menos interpretable                                       |
| Regresión Logística          | Databricks    | 0,715      | Transparente y estable. Buen punto de partida como *baseline*             |
| XGBoost + GridSearch         | Databricks    | 0,747      | Mejor ROC sin necesidad de *oversampling*. Buen equilibrio rendimiento/complejidad |
| **Random Forest (Python)**   | Databricks    | **0,742**  | Réplica exitosa del modelo SAS, con resultados consistentes               |

---

## 📌 Conclusiones Clave

- **Regresión Logística** es simple y explicativa, adecuada para entornos regulados o como modelo de referencia.
- **XGBoost** alcanza un mejor rendimiento tras ajuste con Grid Search, manteniendo interpretabilidad con SHAP.
- **Random Forest en Python** valida la portabilidad del modelo desarrollado en SAS, con rendimiento muy similar.

---

## 🧪 Entornos y Herramientas

- **SAS Enterprise Miner**: modelado inicial y análisis exploratorio.
- **Databricks + Python**: preprocesamiento, ingeniería de variables y modelado con `scikit-learn`, `xgboost` y `MLflow`.

---

## 📁 Estructura del repositorio

- `2024-11-27_Regresión_Logística.ipynb`
- `2024-12-05_XGBoost_ParametrosChurn.ipynb`
- `2025-01-17_CrearGraficoVariables.ipynb`
- `TE_Codigo_Segmentacion_V4.ipynb`
- `README.md`: descripción general y resumen de resultados

---

## 📫 Contacto

Autor: Sergio G.  
Universidad: [Nombre de tu universidad]  
Proyecto: Trabajo de Fin de Grado - 2025 - Optimización Inteligente de Modelos Predictivos para Recobro y Churn
