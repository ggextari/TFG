from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# División de datos en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Entrenamiento del modelo con hiperparámetros ajustados manualmente
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    scale_pos_weight=len(y_train[y_train == 0]) / len(y_train[y_train == 1])
)

model.fit(X_train, y_train)
preds = model.predict_proba(X_test)[:, 1]
roc = roc_auc_score(y_test, preds)
print(f"ROC AUC: {roc:.3f}")