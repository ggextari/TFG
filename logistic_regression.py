from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(max_iter=1000, solver='liblinear')
lr.fit(X_train, y_train)

y_pred_prob = lr.predict_proba(X_test)[:, 1]
print("ROC AUC:", roc_auc_score(y_test, y_pred_prob))
